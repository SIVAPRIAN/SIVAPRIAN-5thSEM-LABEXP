# MD5 Collision Demonstration Program
# -----------------------------------
# This program demonstrates how two different files can have the exact same MD5 hash.
# It automatically generates two distinct 128-byte files that trigger an MD5 collision,
# and then computes and compares their MD5 hashes.

import hashlib
import binascii
import os

# Famous 128-byte MD5 collision blocks (Wang/Yu 2005)
COLLISION_HEX_1 = (
    "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f89"
    "55ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5b"
    "d8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0"
    "e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70"
)

COLLISION_HEX_2 = (
    "d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f89"
    "55ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5b"
    "d8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0"
    "e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70"
)

# Function to calculate MD5 hash of a given file
def calculate_md5(filename):
    md5 = hashlib.md5()
    with open(filename, "rb") as f:
        while True:
            data = f.read(4096)   # Read file in 4KB chunks
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()

# Setup function to generate the collision files if they don't exist
def setup_collision_files(file1, file2):
    print("[*] Generating collision binary files...")
    # Convert hex strings back to raw binary bytes
    bytes1 = binascii.unhexlify(COLLISION_HEX_1)
    bytes2 = binascii.unhexlify(COLLISION_HEX_2)
    
    with open(file1, "wb") as f1:
        f1.write(bytes1)
        
    with open(file2, "wb") as f2:
        f2.write(bytes2)
    print("[*] Created:", file1, f"({len(bytes1)} bytes)")
    print("[*] Created:", file2, f"({len(bytes2)} bytes)")

# Main program
def main():
    print("=== MD5 Collision Demonstration ===")

    # Two different files with the same MD5 (collision examples)
    file1 = "md5_collision1.bin"
    file2 = "md5_collision2.bin"

    # Auto-generate files if missing or of wrong size
    setup_collision_files(file1, file2)

    # Calculate MD5 hashes
    hash1 = calculate_md5(file1)
    hash2 = calculate_md5(file2)

    # Display results
    print("\nFile 1:", file1)
    print("MD5 Hash of File 1:", hash1)

    print("\nFile 2:", file2)
    print("MD5 Hash of File 2:", hash2)

    # Compare results
    if hash1 == hash2:
        print("\n[OK] Both files have the SAME MD5 hash value (collision detected).")
        # Compare file contents to prove they are indeed different
        with open(file1, "rb") as f1, open(file2, "rb") as f2:
            c1 = f1.read()
            c2 = f2.read()
            if c1 != c2:
                print("[OK] Verified: The file contents are DIFFERENT.")
            else:
                print("[ERROR] Error: The file contents are identical.")
    else:
        print("\n[ERROR] Files have different MD5 hashes (no collision).")

if __name__ == "__main__":
    main()
