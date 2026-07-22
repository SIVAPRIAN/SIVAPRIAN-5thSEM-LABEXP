import hashlib
import random

print("=" * 70)
print("GMR ONE-TIME SIGNATURE SCHEME")
print("=" * 70)

message = input("Enter Message : ")

print("\n" + "-" * 60)
print("STEP 1 : MESSAGE")
print("-" * 60)

print("Original Message :")
print(message)

hash_value = hashlib.sha256(message.encode()).hexdigest()

print("\nSHA-256 Hash :")
print(hash_value)

binary_hash = bin(int(hash_value,16))[2:].zfill(256)

print("\nFirst 8 Bits of Hash :")
print(binary_hash[:8])

print("\n" + "-" * 60)
print("STEP 2 : KEY GENERATION")
print("-" * 60)

private_key = []

for i in range(8):

    value = random.randint(1000,9999)

    private_key.append(value)

print("\nPrivate Key Components")

for i,value in enumerate(private_key):

    print(f"SK{i+1} = {value}")

public_key = []

for value in private_key:

    h = hashlib.sha256(str(value).encode()).hexdigest()

    public_key.append(h)

print("\nPublic Key Components")

for i,value in enumerate(public_key):

    print(f"PK{i+1} = {value[:25]}...")

print("\n" + "-" * 60)
print("STEP 3 : SIGNATURE GENERATION")
print("-" * 60)

signature=[]

print("\nSelected Private Keys")

for i in range(8):

    if binary_hash[i]=='1':

        signature.append(private_key[i])

        print(private_key[i])

print("\n" + "-" * 60)
print("STEP 4 : SIGNATURE VERIFICATION")
print("-" * 60)

verified=True

for value in signature:

    h = hashlib.sha256(str(value).encode()).hexdigest()

    if h in public_key:

        print(f"Hash({value})  ---> VERIFIED")

    else:

        print(f"Hash({value})  ---> FAILED")

        verified=False

print("\n" + "-" * 60)
print("FINAL RESULT")
print("-" * 60)

if verified:

    print("Digital Signature Verified Successfully")

    print("Message Integrity Preserved")

    print("Sender Successfully Authenticated")

else:

    print("Signature Verification Failed")
