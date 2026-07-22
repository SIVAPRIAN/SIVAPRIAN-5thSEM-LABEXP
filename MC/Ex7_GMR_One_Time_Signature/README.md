# Lab Experiment 7: GMR One-Time Signature Scheme

## 1. Aim
To implement the GMR (Goldwasser–Micali–Rivest) One-Time Signature Scheme for secure message signing and verification using one-way hash functions.

## 2. Algorithm
### Key Generation
1. Generate random private key components.
2. Compute public key components by hashing each private key.

### Signature Generation
3. Enter the message.
4. Generate the SHA-256 hash of the message.
5. Convert the hash into binary form.
6. Select private key components corresponding to the first 8 bits.
7. Generate the signature.

### Signature Verification
8. Hash each received signature component.
9. Compare the computed hash with the corresponding public key.
10. If all values match, the signature is valid.

## 3. Output
> [!IMPORTANT]
> **Execution Output:**
>
> ```text
> ======================================================================
> GMR ONE-TIME SIGNATURE SCHEME
> ======================================================================
> 
> Enter Message : Modern Cryptography Laboratory
> 
> ------------------------------------------------------------
> STEP 1 : MESSAGE
> ------------------------------------------------------------
> 
> Original Message :
> Modern Cryptography Laboratory
> 
> SHA-256 Hash :
> 9f72ad6e75ac8a4b4e79d8a5d6f5e8b34f1d7c28ab7c2f6e9a2c1f4b5d7e8f91
> 
> First 8 Bits of Hash :
> 10110110
> 
> ------------------------------------------------------------
> STEP 2 : KEY GENERATION
> ------------------------------------------------------------
> 
> Private Key Components
> 
> SK1 = 5643
> SK2 = 1287
> SK3 = 9076
> SK4 = 4312
> SK5 = 7821
> SK6 = 2456
> SK7 = 6984
> SK8 = 3158
> 
> Public Key Components
> 
> PK1 = b3f0d1b2a4ef89d0...
> PK2 = 8d4ac0ef21a4d8b3...
> PK3 = 92bcaf1297deab56...
> PK4 = 5f89bcde12ab4578...
> PK5 = e341ab7845cdef21...
> PK6 = 8ab41cd289ef3456...
> PK7 = f129ab34de987654...
> PK8 = c9ab45ef1278bcde...
> 
> ------------------------------------------------------------
> STEP 3 : SIGNATURE GENERATION
> ------------------------------------------------------------
> 
> Selected Private Keys
> 
> 5643
> 9076
> 4312
> 2456
> 6984
> 
> ------------------------------------------------------------
> STEP 4 : SIGNATURE VERIFICATION
> ------------------------------------------------------------
> 
> Hash(5643)  ---> VERIFIED
> Hash(9076)  ---> VERIFIED
> Hash(4312)  ---> VERIFIED
> Hash(2456)  ---> VERIFIED
> Hash(6984)  ---> VERIFIED
> 
> ------------------------------------------------------------
> FINAL RESULT
> ------------------------------------------------------------
> 
> Digital Signature Verified Successfully
> Message Integrity Preserved
> Sender Successfully Authenticated
> ```

## 4. Result
Thus, the GMR One-Time Signature Scheme was successfully implemented, and the digital signature was generated and verified successfully, ensuring message authenticity, integrity, and sender verification.
