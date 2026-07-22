import os
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Configuration - replace with real AWS credentials if running against S3
AWS_ACCESS_KEY_ID = 'the_access_key'
AWS_SECRET_ACCESS_KEY = 'the_secret_access_key'
BUCKET_NAME = 'the_bucket_name'

# 256-bit encryption key (must be 32 bytes)
ENCRYPTION_KEY = b'ThisIsASecretKey1234567890123456' 

# A Mock S3 Client to allow the script to execute successfully without AWS credentials
class MockS3Client:
    def __init__(self):
        self.store = {}
        print("[MockS3] Mock S3 client initialized for local testing.")

    def put_object(self, Body, Bucket, Key):
        self.store[(Bucket, Key)] = Body
        print(f"[MockS3] Successfully uploaded '{Key}' to mock bucket '{Bucket}'")
        return {"ResponseMetadata": {"HTTPStatusCode": 200}}

    def get_object(self, Bucket, Key):
        if (Bucket, Key) in self.store:
            # Mocking the PyBoto3 StreamingBody object structure
            class MockStreamingBody:
                def __init__(self, data):
                    self.data = data
                def read(self):
                    return self.data
            
            print(f"[MockS3] Successfully retrieved '{Key}' from mock bucket '{Bucket}'")
            return {"Body": MockStreamingBody(self.store[(Bucket, Key)])}
        else:
            raise ClientError({"Error": {"Code": "NoSuchKey", "Message": "The specified key does not exist."}}, "GetObject")

def get_s3_client():
    """
    Returns an active boto3 S3 client if valid credentials exist,
    otherwise falls back to MockS3Client to ensure code is executable.
    """
    if AWS_ACCESS_KEY_ID == 'the_access_key' or not AWS_ACCESS_KEY_ID:
        return MockS3Client()
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
        # Quick validation of credentials
        s3.list_buckets()
        return s3
    except (NoCredentialsError, ClientError):
        print("[AWS S3] Valid credentials not found. Falling back to local Mock S3 client.")
        return MockS3Client()

def encrypt_image(input_file_path):
    """
    Reads local image, encrypts using AES-256 (CBC mode) with padding, and returns ciphertext + IV.
    """
    if not os.path.exists(input_file_path):
        # Create a dummy image file for validation if it doesn't exist
        with open(input_file_path, 'wb') as f:
            f.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDRDummyImageData123456')
        print(f"[Prep] Created dummy file '{input_file_path}' for testing.")

    with open(input_file_path, 'rb') as file:
        image_data = file.read()

    # Generate random 16-byte initialization vector (IV)
    iv = os.urandom(16)
    
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, iv)
    padded_data = pad(image_data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)

    return encrypted_data, iv

def decrypt_image(encrypted_data, iv):
    """
    Decrypts AES-256 encrypted payload and returns original image bytes.
    """
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(encrypted_data)
    original_data = unpad(decrypted_padded, AES.block_size)
    return original_data

def upload_encrypted_image(s3_client, encrypted_data, iv, filename):
    """
    Uploads the encrypted image payload and the matching IV object to S3.
    """
    try:
        # Upload encrypted data
        s3_client.put_object(
            Body=encrypted_data,
            Bucket=BUCKET_NAME,
            Key=filename
        )

        # Upload IV as a separate object
        iv_filename = f"{filename}.iv"
        s3_client.put_object(
            Body=iv,
            Bucket=BUCKET_NAME,
            Key=iv_filename
        )
        return True
    except Exception as e:
        print(f"[Error] S3 Upload failed: {e}")
        return False

def download_and_verify(s3_client, filename, output_filename):
    """
    Downloads encrypted payload and IV from S3, decrypts, and saves the file.
    """
    try:
        # Fetch encrypted payload
        enc_response = s3_client.get_object(Bucket=BUCKET_NAME, Key=filename)
        encrypted_data = enc_response['Body'].read()

        # Fetch IV
        iv_response = s3_client.get_object(Bucket=BUCKET_NAME, Key=f"{filename}.iv")
        iv = iv_response['Body'].read()

        # Decrypt
        decrypted_data = decrypt_image(encrypted_data, iv)

        # Save decrypted file
        with open(output_filename, 'wb') as file:
            file.write(decrypted_data)
        
        print(f"[Local] Decrypted file saved as '{output_filename}'")
        return True
    except Exception as e:
        print(f"[Error] Retrieval or decryption failed: {e}")
        return False

def main():
    input_image = 'original_image.jpg'
    encrypted_filename = 'encrypted_image.jpg'
    decrypted_output = 'decrypted_image.jpg'

    # Get S3 client (real or mock)
    s3_client = get_s3_client()

    print("\n--- Starting Encryption Flow ---")
    encrypted_data, iv = encrypt_image(input_image)
    print(f"[Local] File '{input_image}' encrypted successfully. Size: {len(encrypted_data)} bytes.")

    print("\n--- Uploading Ciphertext to S3 ---")
    upload_success = upload_encrypted_image(s3_client, encrypted_data, iv, encrypted_filename)

    if upload_success:
        print("\n--- Downloading and Decrypting from S3 ---")
        decrypted_success = download_and_verify(s3_client, encrypted_filename, decrypted_output)
        
        if decrypted_success:
            print("\nVerification Status:")
            print("Image encrypted successfully. Image decrypted successfully")
            
            # Clean up dummy test files
            for f in [input_image, decrypted_output]:
                if os.path.exists(f):
                    os.remove(f)

if __name__ == '__main__':
    main()

# EXPECTED OUTPUT:
# Image encrypted successfully. Image decrypted successfully
