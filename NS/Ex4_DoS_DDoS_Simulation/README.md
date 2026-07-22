# Lab Experiment 4: Denial of Service (DoS) and Distributed Denial of Service (DDoS) Demonstration

## 1. Aim
To implement and demonstrate the concept of Denial of Service (DoS) and Distributed Denial of Service (DDoS) attacks by simulating how multiple requests can overwhelm a server and cause unavailability of services.

## 2. Algorithm
1. **Setup Server**: Create a simple web server (victim) that listens for incoming requests.
2. **DoS Simulation**: Write a client program that sends a very large number of requests rapidly to the server from a single machine.
3. **DDoS Simulation**: Extend the client to mimic multiple “attackers” (threads/processes) sending requests simultaneously.
4. **Observe Effect**: Monitor server response time and check if it becomes slow or unresponsive.
5. **Conclusion**: Compare normal vs DoS vs DDoS load on the server and analyze why distributed attacks are more powerful.

## 3. Output
> [!IMPORTANT]
> **Execution Output:**
>
> **Case 1: Normal Server Access**
> ```text
> curl http://127.0.0.1:5000
> Output: "Hello from server!"
> ```
>
> **Case 2: DoS (Single Thread, Many Requests)**
> ```text
> [Thread-1] Request 1: 200
> [Thread-1] Request 2: 200
> ...
> Server becomes slow after many requests.
> ```
>
> **Case 3: DDoS (Multiple Threads, Many Requests)**
> ```text
> [Thread-1] Request 1: 200
> [Thread-2] Request 1: 200
> [Thread-3] Request 1: 200
> ...
> Some requests fail with "Connection error".
> Server becomes overloaded/unresponsive.
> ```

## 4. Result
The experiment successfully demonstrated how excessive or distributed traffic can overwhelm a server, making services unavailable to legitimate users, thereby proving the impact of DoS and DDoS attacks on network availability.
