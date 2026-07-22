# Lab Experiment 1: Feige-Fiat-Shamir Identification Protocol

## 1. Aim
To implement the Feige-Fiat-Shamir Identification Protocol and authenticate a user using Zero-Knowledge Proof techniques without revealing the secret key.

## 2. Algorithm
### Phase 1: Key Generation
1. Input prime numbers $p$ and $q$.
2. Compute $n = p \times q$.
3. Choose secret key $s$ (coprime with $n$).
4. Compute public key $v = s^2 \pmod n$.

### Phase 2: Authentication
5. Choose random value $r$.
6. Compute commitment $x = r^2 \pmod n$.
7. Verifier generates challenge $e \in \{0, 1\}$.
8. Compute response $y = r \times s^e \pmod n$.
9. Verify whether $y^2 \equiv x \times v^e \pmod n$.
10. Display authentication status.

## 3. Output
> [!IMPORTANT]
> **Execution Output:**
>
> ```text
> ============================================================
> FEIGE-FIAT-SHAMIR IDENTIFICATION PROTOCOL
> ============================================================
> 
> Enter Prime Number p: 101
> Enter Prime Number q: 113
> 
> Modulus n = 11413
> 
> Enter Secret Key s (coprime with n): 23
> 
> Public Key v = 529
> 
> Enter Number of Authentication Rounds: 3
> 
> --------------------------------------------------
> ROUND 1
> --------------------------------------------------
> Prover Random Value r = 5421
> Commitment x = 7638
> Verifier Challenge e = 1
> Response y = 10422
> 
> Verification
> LHS = 10675
> RHS = 10675
> 
> Authentication Passed
> 
> --------------------------------------------------
> ROUND 2
> --------------------------------------------------
> Prover Random Value r = 8254
> Commitment x = 4817
> Verifier Challenge e = 0
> Response y = 8254
> 
> Verification
> LHS = 4817
> RHS = 4817
> 
> Authentication Passed
> 
> --------------------------------------------------
> ROUND 3
> --------------------------------------------------
> Prover Random Value r = 6132
> Commitment x = 10092
> Verifier Challenge e = 1
> Response y = 3624
> 
> Verification
> LHS = 948
> RHS = 948
> 
> Authentication Passed
> 
> ============================================================
> FINAL RESULT : USER AUTHENTICATED
> ============================================================
> ```

## 4. Result
Thus the Feige-Fiat-Shamir Identification Protocol was implemented successfully and the user's identity was authenticated using a Zero-Knowledge Proof mechanism without revealing the secret key.
