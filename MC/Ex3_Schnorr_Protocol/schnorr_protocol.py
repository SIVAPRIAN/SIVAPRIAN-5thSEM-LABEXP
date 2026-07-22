import random

print("=" * 60)
print("SCHNORR IDENTIFICATION PROTOCOL")
print("=" * 60)

p = int(input("Enter Prime Number p: "))
g = int(input("Enter Generator g: "))

x = int(input("Enter Secret Key x: "))

y = pow(g, x, p)

print("\nPublic Key y =", y)

rounds = int(input("\nEnter Number of Authentication Rounds: "))

success = True

for i in range(rounds):

    print("\n" + "-" * 50)
    print("ROUND", i + 1)
    print("-" * 50)

    r = random.randint(1, p - 2)

    t = pow(g, r, p)

    print("Random Value r =", r)
    print("Commitment t =", t)

    c = random.randint(1, 5)

    print("Verifier Challenge c =", c)

    s = r + (c * x)

    print("Response s =", s)

    lhs = pow(g, s, p)

    rhs = (t * pow(y, c, p)) % p

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
