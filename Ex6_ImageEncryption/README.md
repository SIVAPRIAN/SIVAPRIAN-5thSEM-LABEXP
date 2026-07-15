# Implement Any Encryption Algorithm To Protect The Images

## Aim
To implement image file encryption using the Advanced Encryption Standard (AES) algorithm in CBC mode, and securely transfer the encrypted payload and Initialization Vector (IV) objects to and from Amazon Web Services (AWS) S3.

## Theory
Images containing sensitive, private, or medical details must be protected against tampering and unauthorized disclosure during cloud storage.
- **Symmetric Encryption (AES)**: Standard encryption where the same key is used to encrypt and decrypt.
- **AES CBC Mode**: Cipher Block Chaining uses an Initialization Vector (IV) to randomize the ciphertext blocks. Even identical blocks of plaintext yield different ciphertext, neutralizing dictionary attacks.
- **IV Management**: The IV is generated using a cryptographically secure random source (`os.urandom`) and must be stored along with the ciphertext (often as a metadata field or a matching secondary storage object) to permit successful decryption.
- **AWS S3**: Cloud storage bucket where the encrypted payloads are hosted.

## Algorithm
1. **Initialize Cryptographic Parameters**: Define a 256-bit encryption key and specify S3 bucket parameters.
2. **Read Image Data**: Fetch binary data from the input image.
3. **AES CBC Encryption**:
   - Generate a random 16-byte IV.
   - Instaniate the AES block cipher in CBC mode.
   - Pad the image binary payload to align with the 16-byte block size constraint.
   - Encrypt the padded plaintext to retrieve the ciphertext.
4. **AWS Transfer / Upload**:
   - Establish connection to AWS S3 using `boto3`.
   - Upload the encrypted binary file to the bucket.
   - Upload the IV payload as a companion file (e.g. `filename.iv`).
5. **AWS Transfer / Download & Decrypt**:
   - Retrieve both the ciphertext and IV from the bucket.
   - Instantiate the AES block cipher with the matching key and retrieved IV.
   - Decrypt the ciphertext and strip the padding to reconstruct the original image.
6. **Verify Result**: Compare original image data with decrypted data.

## Requirements
- Python 3.x
- boto3 (`pip install boto3`)
- pycryptodome (`pip install pycryptodome`)

## How to Run
1. Configure real AWS credentials in the script headers (optional; if left as default, the script defaults to a local mock client for testing).
2. Execute the python script:
   ```bash
   python image_encryption.py
   ```

## Sample Output
```
[MockS3] Mock S3 client initialized for local testing.

--- Starting Encryption Flow ---
[Prep] Created dummy file 'original_image.jpg' for testing.
[Local] File 'original_image.jpg' encrypted successfully. Size: 48 bytes.

--- Uploading Ciphertext to S3 ---
[MockS3] Successfully uploaded 'encrypted_image.jpg' to mock bucket 'the_bucket_name'
[MockS3] Successfully uploaded 'encrypted_image.jpg.iv' to mock bucket 'the_bucket_name'

--- Downloading and Decrypting from S3 ---
[MockS3] Successfully retrieved 'encrypted_image.jpg' from mock bucket 'the_bucket_name'
[MockS3] Successfully retrieved 'encrypted_image.jpg.iv' from mock bucket 'the_bucket_name'
[Local] Decrypted file saved as 'decrypted_image.jpg'

Verification Status:
Image encrypted successfully. Image decrypted successfully
```

## Result
Image encryption was successfully implemented in Python using AES-256. The file encryption, simulated S3 storage operations, and decryption logic were executed and verified successfully.
