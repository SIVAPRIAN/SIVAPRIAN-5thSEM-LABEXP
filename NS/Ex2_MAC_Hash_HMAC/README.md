# Lab Experiment 2: Computing MAC, Hash, and HMAC for Messages

## 1. Aim
To compute the Hash, MAC, and HMAC values for given messages and understand the role of these cryptographic functions in ensuring integrity and authenticity.

## 2. Algorithm
1. **Input Message**: Take a message from the user to be protected.
2. **Hashing**: Apply a secure hash algorithm (e.g., SHA-256) to the message to generate a fixed-length digest that ensures integrity.
3. **Secret Key Setup**: Define a secret key to be shared between sender and receiver for computing MAC/HMAC.
4. **MAC Computation**: Use a cryptographic library to generate a MAC using the secret key and the input message.
5. **HMAC Computation**: Apply the HMAC function (hash + secret key) to compute a stronger authentication code, and display results for comparison.

## 3. Output
> [!IMPORTANT]
> **Execution Output:**
> ```text
> === MAC, HASH and HMAC Computation ===
> 
> Enter the message: Hello World
> Enter the secret key: secret123
> 
> --- Hash Values ---
> SHA-256 Hash : a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
> MD5 Hash     : b10a8db164e0754105b7a99be72e3fe5
> 
> --- MAC Value ---
> MAC (SHA-256 with Key+Message): 5e5a10cce7c324f6b16224cf7791cc63d79e4690a3f5d6e14b7cd2731df512a2
> 
> --- HMAC Value ---
> HMAC (SHA-256): 4635c3bdb7d9e4d2472e251b0fa9cce1d3f5f430726f9a7769e2925ad918f1d4
> 
> ✅ Hash ensures integrity.
> ✅ MAC ensures authenticity using a secret key.
> ✅ HMAC provides stronger authentication with key + hash.
> ```

## 4. Result
The experiment successfully demonstrated the computation of Hash, MAC, and HMAC values for a given message, proving that while a hash ensures data integrity, the use of MAC and HMAC additionally provides authenticity and stronger protection against tampering.
