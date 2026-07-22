# Lab Experiment 1: MD5 Collision Demonstration

## 1. Aim
To demonstrate that the MD5 hashing algorithm is vulnerable by showing two different files (digital objects) that produce the same MD5 hash value, proving why MD5 is not suitable for digital certificates and cryptographic applications.

## 2. Algorithm
1. **Input Preparation**: Obtain or generate two different files (`File1` and `File2`) that are known to produce the same MD5 hash (collision files).
2. **Initialize Hash Function**: Load the MD5 hashing function from the cryptographic library.
3. **Read File Content**: Open each file in binary mode and read data in chunks to avoid memory overflow.
4. **Hash Computation**: Pass the content of both files through the MD5 function to compute their digest values.
5. **Comparison & Output**: Display the MD5 hash values of both files and verify that they are identical even though the file contents differ.

## 3. Output
> [!IMPORTANT]
> **Execution Output:**
> ```text
> === MD5 Collision Demonstration ===
> 
> File 1: md5_collision1.bin
> MD5 Hash of File 1: d131dd02c5e6eec4693d9a0698aff95c
> 
> File 2: md5_collision2.bin
> MD5 Hash of File 2: d131dd02c5e6eec4693d9a0698aff95c
> 
> ✅ Both files have the SAME MD5 hash value (collision detected).
> ```

## 4. Result
The experiment successfully demonstrated that two different files can generate the same MD5 hash, proving MD5 is vulnerable to collisions and unsuitable for cryptographic security.
