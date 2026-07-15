# Simulate A Secure File Sharing Using A Cloudsim

## Aim
To simulate a secure file sharing system in a cloud computing environment, incorporating authentication checks, Role-Based Access Control (RBAC), cryptographic encryption/decryption (AES-256), and security auditing.

## Theory
Secure storage and sharing are paramount in cloud services. Standard file sharing mechanisms are vulnerable to leaks if the hosting server is compromised. 
- **Encryption-at-Rest**: Files must be encrypted before writing to persistent cloud block storage. In this experiment, we utilize **AES-256** (Advanced Encryption Standard), a symmetric key cryptographic algorithm.
- **Access Control**: Users are mapped to roles (e.g. Admin, Developer, Client) which restrict capabilities:
  - `Admin`/`Developer` roles have write privileges (can upload files).
  - Only matching keyholders can retrieve/decrypt files.
- **Audit Logging**: Every access attempt (success or denial) is recorded for log analysis and forensic auditing.

## Algorithm
1. **Initialize Cloud Entities**: Configure user roles, names, and cryptographic keys.
2. **Generate File Sharing Requests**: Produce a workload queue of file requests with filenames and sizes.
3. **Execute Process Loop**: For each request:
   - Select a user.
   - Simulate an authentication check (incorporating a simulated 95% baseline success rate).
   - If authenticated, check write permissions for uploads or key matches for downloads.
   - For **Uploads**: Encrypt the payload using AES-256 and store the ciphertext in cloud storage.
   - For **Downloads**: Fetch the ciphertext and attempt decryption using the user's secret key.
   - Run verification (Integrity Check) by comparing decrypted contents with original data.
4. **Compile Metrics**: Calculate total uploads, total downloads, authentication success rate, average response time, and transaction throughput.
5. **Print Audit Logs & Performance Report**: Generate and output logs and security metrics.

## Requirements
- Java Development Kit (JDK) 8 or later.

## How to Run
1. Compile the Java code:
   ```bash
   javac SecureFileSharingSimulation.java
   ```
2. Run the application:
   ```bash
   java SecureFileSharingSimulation
   ```

## Sample Output
```
Starting Secure File Sharing Cloud Simulation...

--- Cloud Secure Audit Log Snippet ---
[AUDIT] Success: Encrypted upload of cloud_document_1.txt by user Alice
[AUDIT] Success: Decrypted download of cloud_document_1.txt by user Alice
[AUDIT] Integrity Check passed for: cloud_document_1.txt
[AUDIT] Success: Encrypted upload of cloud_document_2.txt by user Bob
[AUDIT] Success: Decrypted download of cloud_document_2.txt by user Bob
[AUDIT] Integrity Check passed for: cloud_document_2.txt
... [34 more logs recorded] ...

Simulation Results:
Total simulation time: 1000.0 seconds
Datacenter Information:
- Number of hosts: 5
- Number of virtual machines: 10
- Number of users: 1

File Sharing Activities:
- Total file uploads: 20
- Total file downloads: 20

Security Metrics:
- Authentication success rate: 95%
- Encryption level: AES-256

Performance Metrics:
- Average response time: 5.0 seconds
- Throughput: 0.04 files/second
```

## Result
A secure file sharing system was successfully simulated in Java. The system successfully executed role checks and AES-256 cryptographic routines, verifying file integrity and outputting the expected performance and security statistics.
