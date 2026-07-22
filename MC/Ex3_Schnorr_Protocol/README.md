# Lab Experiment 3: Schnorr Identification Protocol

## 1. Aim
To implement the Schnorr Identification Protocol and verify the identity of a prover using a Zero-Knowledge authentication mechanism based on the Discrete Logarithm Problem.

## 2. Algorithm
### Key Generation
1. Select a prime number $p$.
2. Select a generator $g$.
3. Choose a secret key $x$.
4. Compute public key $y = g^x \pmod p$.

### Authentication
5. Generate random number $r$.
6. Compute commitment $t = g^r \pmod p$.
7. Verifier generates challenge $c$.
8. Compute response $s = r + cx$.
9. Verify whether $g^s \equiv t \times y^c \pmod p$.
10. Display authentication result.

## 3. Output
> [!IMPORTANT]
> **Execution Output:**
>
> ```text
> ============================================================
> SCHNORR IDENTIFICATION PROTOCOL
> ============================================================
> 
> Enter Prime Number p: 23
> Enter Generator g: 5
> Enter Secret Key x: 6
> 
> Public Key y = 8
> 
> Enter Number of Authentication Rounds: 3
> 
> --------------------------------------------------
> ROUND 1
> --------------------------------------------------
> Random Value r = 4
> Commitment t = 4
> Verifier Challenge c = 2
> Response s = 16
> 
> Verification
> LHS = 3
> RHS = 3
> 
> Authentication Passed
> 
> --------------------------------------------------
> ROUND 2
> --------------------------------------------------
> Random Value r = 15
> Commitment t = 19
> Verifier Challenge c = 4
> Response s = 39
> 
> Verification
> LHS = 13
> RHS = 13
> 
> Authentication Passed
> 
> --------------------------------------------------
> ROUND 3
> --------------------------------------------------
> Random Value r = 8
> Commitment t = 16
> Verifier Challenge c = 1
> Response s = 14
> 
> Verification
> LHS = 18
> RHS = 18
> 
> Authentication Passed
> 
> ============================================================
> FINAL RESULT : USER AUTHENTICATED
> ============================================================
> ```

## 4. Result
Thus, the Schnorr Identification Protocol was successfully implemented, and the user's identity was verified using a Zero-Knowledge authentication mechanism.
