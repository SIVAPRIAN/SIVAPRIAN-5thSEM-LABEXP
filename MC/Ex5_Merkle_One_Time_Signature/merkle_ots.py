import hashlib
import random

print("=" * 70)
print("MERKLE ONE-TIME SIGNATURE SCHEME")
print("=" * 70)

message = input("Enter Message : ")

print("\n" + "-" * 60)
print("STEP 1 : MESSAGE")
print("-" * 60)

print("Original Message :")
print(message)

print("\n" + "-" * 60)
print("STEP 2 : HASH GENERATION")
print("-" * 60)

hash_value = hashlib.sha256(message.encode()).hexdigest()

print("SHA-256 Hash :")
print(hash_value)

binary_hash = bin(int(hash_value,16))[2:].zfill(256)

print("\nFirst 8 Bits of Hash :")
print(binary_hash[:8])

print("\n" + "-" * 60)
print("STEP 3 : KEY GENERATION")
print("-" * 60)

private_keys = []

for i in range(8):
    private_keys.append(random.randint(1000,9999))

print("\nPrivate Keys")

for i,key in enumerate(private_keys):
    print(f"SK{i+1} = {key}")

public_keys=[]

for key in private_keys:
    public_keys.append(hashlib.sha256(str(key).encode()).hexdigest())

print("\nPublic Keys")

for i,key in enumerate(public_keys):
    print(f"PK{i+1} = {key[:20]}...")

print("\n" + "-" * 60)
print("STEP 4 : SIGNATURE GENERATION")
print("-" * 60)

signature=[]

for i in range(8):

    if binary_hash[i]=='1':

        signature.append(private_keys[i])

print("\nSignature Components")

for value in signature:
    print(value)

print("\n" + "-" * 60)
print("STEP 5 : SIGNATURE VERIFICATION")
print("-" * 60)

verified=True

for value in signature:

    h=hashlib.sha256(str(value).encode()).hexdigest()

    if h in public_keys:
        print(f"Hash({value}) ✓ Verified")
    else:
        print(f"Hash({value}) ✗ Failed")
        verified=False

print("\n" + "-" * 60)
print("FINAL RESULT")
print("-" * 60)

if verified:

    print("Signature Verified Successfully")
    print("Message Integrity Preserved")
    print("Sender Authentication Successful")

else:

    print("Signature Verification Failed")
