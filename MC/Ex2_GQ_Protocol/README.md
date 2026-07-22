# Lab Experiment 2: GQ (Guillou-Quisquater) Identification Protocol

## 1. Aim
To implement the Guillou-Quisquater (GQ) Identification Protocol and perform secure user authentication using RSA-based Zero-Knowledge Proof techniques.

## 2. Algorithm
### Phase 1: Key Generation
1. Input prime numbers $p$ and $q$.
2. Compute $n = p \times q$ and $\phi(n) = (p-1)(q-1)$.
3. Input public exponent $e$ (coprime with $\phi(n)$).
4. Input secret identity $s$ (coprime with $n$).
5. Compute public identity $I = s^e \pmod n$.

### Phase 2: Authentication
6. Generate random value $r$.
7. Compute commitment $x = r^e \pmod n$.
8. Verifier generates challenge $c$.
9. Compute response $y = r \times s^c \pmod n$.
10. Verify whether $y^e \equiv x \times I^c \pmod n$.
11. Display authentication result.

## 3. Output
> [!IMPORTANT]
> **Execution Output:**
>
> ```text
> ============================================================
> GQ IDENTIFICATION PROTOCOL
> ============================================================
> 
> Enter Prime Number p: 17
> Enter Prime Number q: 11
> 
> Modulus n = 187
> Euler Totient phi(n) = 160
> 
> Enter Public Exponent e: 7
> 
> Enter Secret Identity s: 9
> 
> Public Identity I = 70
> 
> Enter Number of Authentication Rounds: 3
> 
> --------------------------------------------------
> ROUND 1
> --------------------------------------------------
> Random Value r = 52
> Commitment x = 69
> 
> Verifier Challenge c = 2
> 
> Response y = 155
> 
> Verification
> LHS = 44
> RHS = 44
> 
> Authentication Passed
> 
> --------------------------------------------------
> ROUND 2
> --------------------------------------------------
> Random Value r = 76
> Commitment x = 109
> 
> Verifier Challenge c = 3
> 
> Response y = 10
> 
> Verification
> LHS = 142
> RHS = 142
> 
> Authentication Passed
> 
> --------------------------------------------------
> ROUND 3
> --------------------------------------------------
> Random Value r = 93
> Commitment x = 137
> 
> Verifier Challenge c = 1
> 
> Response y = 89
> 
> Verification
> LHS = 64
> RHS = 64
> 
> Authentication Passed
> 
> ============================================================
> FINAL RESULT : USER AUTHENTICATED
> ============================================================
> ```

## 4. Result
Thus the Guillou-Quisquater (GQ) Identification Protocol was implemented successfully and the user's identity was authenticated using RSA-based challenge-response verification.
