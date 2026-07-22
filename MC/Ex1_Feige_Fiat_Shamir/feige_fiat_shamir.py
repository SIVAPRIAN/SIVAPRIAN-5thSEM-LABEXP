import random
import math

print("=" * 60)
print("FEIGE-FIAT-SHAMIR IDENTIFICATION PROTOCOL")
print("=" * 60)

# Input primes
p = int(input("Enter Prime Number p: "))
q = int(input("Enter Prime Number q: "))

n = p * q

print("\nModulus n =", n)

# Input secret key
while True:
    s = int(input("Enter Secret Key s (coprime with n): "))

    if math.gcd(s, n) == 1:
        break

    print("s must be coprime with n. Try again.")

# Public key
v = pow(s, 2, n)

print("Public Key v =", v)

# Number of authentication rounds
rounds = int(input("\nEnter Number of Authentication Rounds: "))

success = True

for i in range(rounds):

    print("\n" + "-" * 50)
    print("ROUND", i + 1)
    print("-" * 50)

    # Prover chooses random r
    r = random.randint(2, n - 1)

    # Commitment
    x = pow(r, 2, n)

    print("Prover Random Value r =", r)
    print("Commitment x =", x)

    # Verifier generates challenge
    e = random.randint(0, 1)

    print("Verifier Challenge e =", e)

    # Response
    y = (r * pow(s, e, n)) % n

    print("Response y =", y)

    # Verification
    lhs = pow(y, 2, n)
    rhs = (x * pow(v, e, n)) % n

    print("\nVerification")
    print("LHS =", lhs)
    print("RHS =", rhs)

    if lhs == rhs:
        print("Authentication Passed")
    else:
        print("Authentication Failed")
        success = False

print("\n" + "=" * 60)

if success:
    print("FINAL RESULT : USER AUTHENTICATED")
else:
    print("FINAL RESULT : USER NOT AUTHENTICATED")

print("=" * 60)
