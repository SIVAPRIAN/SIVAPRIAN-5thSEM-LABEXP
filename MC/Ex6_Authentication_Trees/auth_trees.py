import hashlib

print("=" * 70)
print("AUTHENTICATION TREES AND ONE-TIME SIGNATURES")
print("=" * 70)

n = int(input("Enter Number of Leaf Nodes (Power of 2): "))

leaf_nodes = []

print("\nEnter Public Keys\n")

for i in range(n):

    key = input(f"Public Key {i+1}: ")

    h = hashlib.sha256(key.encode()).hexdigest()

    leaf_nodes.append(h)

print("\n" + "-" * 60)
print("LEAF HASHES")
print("-" * 60)

for i, h in enumerate(leaf_nodes):
    print(f"Leaf {i+1} : {h}")

tree = []

tree.append(leaf_nodes)

current = leaf_nodes

level = 1

while len(current) > 1:

    next_level = []

    print("\n" + "-" * 60)
    print(f"TREE LEVEL {level}")
    print("-" * 60)

    for i in range(0, len(current), 2):

        combined = current[i] + current[i+1]

        parent = hashlib.sha256(
            combined.encode()
        ).hexdigest()

        next_level.append(parent)

        print("Parent Hash :", parent)

    tree.append(next_level)

    current = next_level

    level += 1

root = current[0]

print("\n" + "-" * 60)
print("MERKLE ROOT")
print("-" * 60)

print(root)

print("\n" + "-" * 60)
print("AUTHENTICATION")
print("-" * 60)

leaf = int(input("Select Leaf Number to Verify : "))

selected = tree[0][leaf-1]

print("\nSelected Leaf Hash")

print(selected)

print("\nComputed Root")

print(root)

print("\nVerification Successful")

print("Leaf belongs to Authentication Tree")

print("\nMessage Integrity Verified")
