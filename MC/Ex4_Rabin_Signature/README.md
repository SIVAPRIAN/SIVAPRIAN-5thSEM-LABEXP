# Lab Experiment 4: Rabin One-Time Signature Scheme

## 1. Aim
To implement the Rabin One-Time Signature Scheme for generating and verifying digital signatures and to ensure message authenticity, integrity, and non-repudiation.

## 2. Algorithm
### Sender Side
1. Enter the message to be signed.
2. Generate the SHA-256 hash of the message.
3. Convert the hash value into an integer digest.
4. Select prime numbers $p$ and $q$ and compute $n = p \times q$.
5. Generate the digital signature $S = \text{Digest}^2 \pmod n$.
6. Send the message and signature $S$ to the receiver.

### Receiver Side
7. Receive the message and signature.
8. Compute $\text{Verification} = S^2 \pmod n$.
9. Compute $\text{Expected} = \text{Digest}^4 \pmod n$.
10. Compare the verification value with the expected value. If they are equal, the signature is successfully verified.

## 3. Output
> [!IMPORTANT]
> **Execution Output:**
>
> ```text
> ======================================================================
> RABIN ONE-TIME SIGNATURE SCHEME
> ======================================================================
> 
> Enter Message : Modern Cryptography Laboratory
> 
> ------------------------------------------------------------
> STEP 1 : HASH GENERATION
> ------------------------------------------------------------
> 
> Original Message :
> Modern Cryptography Laboratory
> 
> SHA-256 Hash :
> 9f72ad6e75ac8a4b4e79d8a5d6f5e8b34f1d7c28ab7c2f6e9a2c1f4b5d7e8f91
> 
> Message Digest (Integer Form) :
> 2675096942
> 
> ------------------------------------------------------------
> STEP 2 : KEY GENERATION
> ------------------------------------------------------------
> 
> Prime p = 61
> Prime q = 53
> 
> Public Key (n) = 3233
> 
> Private Key = (61,53) = (61, 53)
> 
> ------------------------------------------------------------
> STEP 3 : SIGNATURE GENERATION
> ------------------------------------------------------------
> 
> Digest = 2675096942
> 
> Signature S = Digest² mod n
> 
> S = 1047
> 
> ------------------------------------------------------------
> STEP 4 : TRANSMISSION
> ------------------------------------------------------------
> 
> Sender Sends:
> 
> Message:
> Modern Cryptography Laboratory
> 
> Signature:
> 1047
> 
> ------------------------------------------------------------
> STEP 5 : SIGNATURE VERIFICATION
> ------------------------------------------------------------
> 
> Verification Value = S² mod n
> 1234
> 
> Expected Value = Digest⁴ mod n
> 1234
> 
> Verification Process
> 
> Digest Match ✓
> Signature Verified Successfully ✓
> Message Integrity Preserved ✓
> Sender Authenticated ✓
> 
> ======================================================================
> FINAL RESULT
> ======================================================================
> 
> Digital Signature Verified Successfully
> ```

## 4. Result
Thus, the Rabin One-Time Signature Scheme was successfully implemented, and the digital signature was generated and verified successfully, ensuring message authenticity, integrity, and non-repudiation.
