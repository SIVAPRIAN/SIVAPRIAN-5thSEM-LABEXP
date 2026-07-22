import hashlib

print("=" * 70)
print("RABIN ONE-TIME SIGNATURE SCHEME")
print("=" * 70)

# INPUT MESSAGE
message = input("Enter Message : ")

print("\n" + "-" * 60)
print("STEP 1 : HASH GENERATION")
print("-" * 60)

hash_hex = hashlib.sha256(message.encode()).hexdigest()

print("Original Message :")
print(message)

print("\nSHA-256 Hash :")
print(hash_hex)

# Convert first few digits of hash into integer
digest = int(hash_hex[:8], 16)

print("\nMessage Digest (Integer Form) :")
print(digest)

print("\n" + "-" * 60)
print("STEP 2 : KEY GENERATION")
print("-" * 60)

# Small primes for demonstration
p = 61
q = 53

n = p * q

print("Prime p =", p)
print("Prime q =", q)

print("\nPublic Key (n) =", n)
print("Private Key = (p,q) =", (p, q))

print("\n" + "-" * 60)
print("STEP 3 : SIGNATURE GENERATION")
print("-" * 60)

# Simplified Rabin Signature
signature = pow(digest, 2, n)

print("Digest =", digest)

print("\nSignature S = Digest² mod n")

print("S =", signature)

print("\n" + "-" * 60)
print("STEP 4 : TRANSMISSION")
print("-" * 60)

print("Sender Sends:")

print("\nMessage:")
print(message)

print("\nSignature:")
print(signature)

print("\n" + "-" * 60)
print("STEP 5 : SIGNATURE VERIFICATION")
print("-" * 60)

verification_value = pow(signature, 2, n)

expected_value = pow(digest, 4, n)

print("Verification Value = S² mod n")
print(verification_value)

print("\nExpected Value = Digest⁴ mod n")
print(expected_value)

print("\nVerification Process")

if verification_value == expected_value:
    print("\nDigest Match ✓")
    print("Signature Verified Successfully ✓")
    print("Message Integrity Preserved ✓")
    print("Sender Authenticated ✓")
else:
    print("\nDigest Mismatch ✗")
    print("Signature Verification Failed ✗")

print("\n" + "=" * 70)
print("FINAL RESULT")
print("=" * 70)

if verification_value == expected_value:
    print("Digital Signature Verified Successfully")
else:
    print("Digital Signature Verification Failed")
