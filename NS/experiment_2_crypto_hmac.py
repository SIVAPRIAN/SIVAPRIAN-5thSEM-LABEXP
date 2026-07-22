# Program: Computing Hash, MAC, and HMAC for messages
# ----------------------------------------------------
# This program demonstrates the computation of Hash values (integrity),
# a simple Message Authentication Code (MAC) via key prefixing,
# and an HMAC (Hash-based Message Authentication Code) for message integrity and authenticity.

import hashlib
import hmac

# Function to compute hash of a message
def compute_hash(message):
    sha256_hash = hashlib.sha256(message.encode('utf-8')).hexdigest()
    md5_hash = hashlib.md5(message.encode('utf-8')).hexdigest()
    return sha256_hash, md5_hash

# Function to compute simple MAC (by hashing key + message)
def compute_mac(message, key):
    # This is a naive MAC construction (key concatenation)
    data = key + message
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Function to compute HMAC
def compute_hmac(message, key):
    # Standard HMAC implementation using hmac library and SHA-256
    return hmac.new(key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()

# Main Program
def main():
    print("=== MAC, HASH and HMAC Computation ===\n")
    
    # Step 1: Input message
    message = input("Enter the message: ")
    secret_key = input("Enter the secret key: ")

    # Step 2: Compute Hashes
    sha256_hash, md5_hash = compute_hash(message)
    print("\n--- Hash Values ---")
    print("SHA-256 Hash :", sha256_hash)
    print("MD5 Hash     :", md5_hash)

    # Step 3: Compute MAC
    mac_value = compute_mac(message, secret_key)
    print("\n--- MAC Value ---")
    print("MAC (SHA-256 with Key+Message):", mac_value)

    # Step 4: Compute HMAC
    hmac_value = compute_hmac(message, secret_key)
    print("\n--- HMAC Value ---")
    print("HMAC (SHA-256):", hmac_value)

    print("\n[OK] Hash ensures integrity.")
    print("[OK] MAC ensures authenticity using a secret key.")
    print("[OK] HMAC provides stronger authentication with key + hash.")

if __name__ == "__main__":
    main()
