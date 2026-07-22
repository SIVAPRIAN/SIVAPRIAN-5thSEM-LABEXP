# Lab Experiment 6: Authentication Trees and One-Time Signatures

## 1. Aim
To implement Authentication Trees (Merkle Trees) with One-Time Signature Schemes for secure message authentication and verification using cryptographic hash functions.

## 2. Algorithm
### Phase 1 – Key Generation
1. Generate one-time public keys.
2. Compute SHA-256 hash of every public key.
3. Store hashes as leaf nodes.

### Phase 2 – Merkle Tree Construction
4. Pair two adjacent hashes.
5. Concatenate the hashes.
6. Compute SHA-256 of the concatenated value.
7. Continue until a single root hash is obtained.

### Phase 3 – Authentication
8. Select a leaf node.
9. Generate authentication path.
10. Recompute hashes toward the root.
11. Compare computed root with stored root.
12. If equal, authentication succeeds.

## 3. Output
> [!IMPORTANT]
> **Execution Output:**
>
> ```text
> ======================================================================
> AUTHENTICATION TREES AND ONE-TIME SIGNATURES
> ======================================================================
> 
> Enter Number of Leaf Nodes (Power of 2): 4
> 
> Enter Public Keys
> 
> Public Key 1: Alice
> Public Key 2: Bob
> Public Key 3: Charlie
> Public Key 4: David
> 
> ------------------------------------------------------------
> LEAF HASHES
> ------------------------------------------------------------
> Leaf 1 : 3bc51062973c458d...
> Leaf 2 : cd9fb1e148ccd844...
> Leaf 3 : 6e81b1255ad51bb2...
> Leaf 4 : a6b54c20a7b96eea...
> 
> ------------------------------------------------------------
> TREE LEVEL 1
> ------------------------------------------------------------
> Parent Hash : 0e7c8ef2c59b9f2c...
> Parent Hash : 97c5b73f8d7adbe1...
> 
> ------------------------------------------------------------
> TREE LEVEL 2
> ------------------------------------------------------------
> Parent Hash : 48a91c9d90f16d7b...
> 
> ------------------------------------------------------------
> MERKLE ROOT
> ------------------------------------------------------------
> 48a91c9d90f16d7b...
> 
> ------------------------------------------------------------
> AUTHENTICATION
> ------------------------------------------------------------
> Select Leaf Number to Verify : 3
> 
> Selected Leaf Hash
> 6e81b1255ad51bb2...
> 
> Computed Root
> 48a91c9d90f16d7b...
> 
> Verification Successful
> Leaf belongs to Authentication Tree
> Message Integrity Verified
> ```

## 4. Result
Thus, the Authentication Trees (Merkle Trees) with One-Time Signature Schemes was successfully implemented, and leaf key authentication was performed securely.
