import random
import math

print("=" * 60)
print("GQ IDENTIFICATION PROTOCOL")
print("=" * 60)

p = int(input("Enter Prime Number p: "))
q = int(input("Enter Prime Number q: "))

n = p * q
phi = (p - 1) * (q - 1)

print("\nModulus n =", n)
print("Euler Totient phi(n) =", phi)

while True:

    e = int(input("\nEnter Public Exponent e: "))

    if math.gcd(e, phi) == 1:
        break

    print("e must be coprime with phi(n).")

while True:

    s = int(input("Enter Secret Identity s: "))

    if math.gcd(s, n) == 1:
        break

    print("s must be coprime with n.")

I = pow(s, e, n)

print("\nPublic Identity I =", I)

rounds = int(input("\nEnter Number of Authentication Rounds: "))

success = True

for i in range(rounds):

    print("\n" + "-" * 50)
    print("ROUND", i + 1)
    print("-" * 50)

    r = random.randint(2, n - 1)

    x = pow(r, e, n)

    print("Random Value r =", r)
    print("Commitment x =", x)

    c = random.randint(1, 5)

    print("Verifier Challenge c =", c)

    y = (r * pow(s, c, n)) % n

    print("Response y =", y)

    lhs = pow(y, e, n)

    rhs = (x * pow(I, c, n)) % n

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
