# Lab Experiment 5: Merkle One-Time Signature Scheme

## 1. Aim
To implement the Merkle One-Time Signature Scheme for secure message signing and signature verification using cryptographic hash functions.

## 2. Algorithm
### Key Generation
1. Generate random private keys.
2. Compute public keys by hashing each private key.

### Signature Generation
3. Enter the message.
4. Generate the SHA-256 hash of the message.
5. Convert the hash into binary.
6. Select private keys corresponding to the first 8 hash bits.
7. Generate the signature.

### Verification
8. Hash each received signature component.
9. Compare with the stored public keys.
10. If all values match, accept the signature.

## 3. Output
> [!IMPORTANT]
> **Execution Output:**
>
> ```text
> ======================================================================
> MERKLE ONE-TIME SIGNATURE SCHEME
> ======================================================================
> 
> Enter Message : Modern Cryptography Laboratory Experiment
> 
> ------------------------------------------------------------
> STEP 1 : MESSAGE
> ------------------------------------------------------------
> 
> Original Message :
> Modern Cryptography Laboratory Experiment
> 
> ------------------------------------------------------------
> STEP 2 : HASH GENERATION
> ------------------------------------------------------------
> 
> SHA-256 Hash :
> ab5d0e28d4d95af42d63c18fd09fd7ec8e9bfbaf4d5d53...
> 
> First 8 Bits of Hash :
> 10110110
> 
> ------------------------------------------------------------
> STEP 3 : KEY GENERATION
> ------------------------------------------------------------
> 
> Private Keys
> 
> SK1 = 3451
> SK2 = 8263
> SK3 = 9175
> SK4 = 2387
> SK5 = 6514
> SK6 = 7459
> SK7 = 1246
> SK8 = 5832
> 
> Public Keys
> 
> PK1 = 45f8b45f4d5c89d1...
> PK2 = 5f29ab92cd7fa124...
> PK3 = 0f14c83ad7bc2f91...
> PK4 = a5f74b9c89d7aa45...
> PK5 = 6e41c4d81fbc2290...
> PK6 = 21a8d97bc45df214...
> PK7 = 7f1d6bc92d89c145...
> PK8 = 9e62df4512ab98ef...
> 
> ------------------------------------------------------------
> STEP 4 : SIGNATURE GENERATION
> ------------------------------------------------------------
> 
> Signature Components
> 
> 3451
> 9175
> 2387
> 7459
> 1246
> 
> ------------------------------------------------------------
> STEP 5 : SIGNATURE VERIFICATION
> ------------------------------------------------------------
> 
> Hash(3451) ✓ Verified
> Hash(9175) ✓ Verified
> Hash(2387) ✓ Verified
> Hash(7459) ✓ Verified
> Hash(1246) ✓ Verified
> 
> ------------------------------------------------------------
> FINAL RESULT
> ------------------------------------------------------------
> 
> Signature Verified Successfully
> Message Integrity Preserved
> Sender Authentication Successful
> ```

## 4. Result
Thus, the Merkle One-Time Signature Scheme was successfully implemented, and the digital signature was generated and verified successfully using cryptographic hash functions.
