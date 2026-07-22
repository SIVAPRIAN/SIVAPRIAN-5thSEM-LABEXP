# Security and Privacy in Cloud Laboratory

This repository contains complete, executable, and optimized source code implementations for the **Security and Privacy in Cloud (SPC)** Laboratory experiments.

All syntax and logical errors present in the original lab manual have been corrected. Python scripts and Java programs include standalone verification modules and mock fallbacks (for AWS and Azure SDK integrations) to allow out-of-the-box local execution.

## Repository Structure

Each experiment is housed in its own dedicated directory containing a single complete source code file and a detailed guide:

1. **[Ex1_CloudScheduling](file:///c:/Users/Sivap/Documents/lab/SPC/Ex1_CloudScheduling)**: Simulate a Cloud Scenario Using CloudSim and Run a Custom Round-Robin Scheduling Algorithm.
   - Source Code: [CustomSchedulingSimulation.java](file:///c:/Users/Sivap/Documents/lab/SPC/Ex1_CloudScheduling/CustomSchedulingSimulation.java)
2. **[Ex2_ResourceManagement](file:///c:/Users/Sivap/Documents/lab/SPC/Ex2_ResourceManagement)**: Simulate resource allocation, CPU/RAM/bandwidth utilization, and energy consumption in CloudSim.
   - Source Code: [ResourceManagementSimulation.java](file:///c:/Users/Sivap/Documents/lab/SPC/Ex2_ResourceManagement/ResourceManagementSimulation.java)
3. **[Ex3_LogForensics](file:///c:/Users/Sivap/Documents/lab/SPC/Ex3_LogForensics)**: Parse and analyze log entries to detect unauthorized accesses, data exfiltration, and resource spikes.
   - Source Code: [LogForensicsSimulation.java](file:///c:/Users/Sivap/Documents/lab/SPC/Ex3_LogForensics/LogForensicsSimulation.java)
4. **[Ex4_SecureFileSharing](file:///c:/Users/Sivap/Documents/lab/SPC/Ex4_SecureFileSharing)**: Simulate secure cloud file sharing with role check restrictions, AES-256 encryption, and integrity verification.
   - Source Code: [SecureFileSharingSimulation.java](file:///c:/Users/Sivap/Documents/lab/SPC/Ex4_SecureFileSharing/SecureFileSharingSimulation.java)
5. **[Ex5_DataAnonymization](file:///c:/Users/Sivap/Documents/lab/SPC/Ex5_DataAnonymization)**: Anonymize datasets by implementing character-level data masking and structural $k$-anonymity.
   - Source Code: [data_anonymization.py](file:///c:/Users/Sivap/Documents/lab/SPC/Ex5_DataAnonymization/data_anonymization.py)
6. **[Ex6_ImageEncryption](file:///c:/Users/Sivap/Documents/lab/SPC/Ex6_ImageEncryption)**: Encrypt local images using AES-256 CBC and upload/download payload and IV objects to AWS S3.
   - Source Code: [image_encryption.py](file:///c:/Users/Sivap/Documents/lab/SPC/Ex6_ImageEncryption/image_encryption.py)
7. **[Ex7_ImageObfuscation](file:///c:/Users/Sivap/Documents/lab/SPC/Ex7_ImageObfuscation)**: Local image obfuscation applying Gaussian blurring filters and selective pixelation of regions.
   - Source Code: [image_obfuscation.py](file:///c:/Users/Sivap/Documents/lab/SPC/Ex7_ImageObfuscation/image_obfuscation.py)
8. **[Ex8_RBAC](file:///c:/Users/Sivap/Documents/lab/SPC/Ex8_RBAC)**: Manage and enforce Role-Based Access Control policies loaded from Microsoft Azure KeyVault.
   - Source Code: [rbac_system.py](file:///c:/Users/Sivap/Documents/lab/SPC/Ex8_RBAC/rbac_system.py)
9. **[Ex9_ABAC](file:///c:/Users/Sivap/Documents/lab/SPC/Ex9_ABAC)**: Enforce Attribute-Based Access Control policies validating subject role, department, and contextual time-of-day.
   - Source Code: [abac_system.py](file:///c:/Users/Sivap/Documents/lab/SPC/Ex9_ABAC/abac_system.py)
10. **[Ex10_LogMonitoring](file:///c:/Users/Sivap/Documents/lab/SPC/Ex10_LogMonitoring)**: CloudWatch log event handler triggered via serverless AWS Lambda to automatically report incidents to AWS Incident Manager.
    - Source Code: [log_monitoring.py](file:///c:/Users/Sivap/Documents/lab/SPC/Ex10_LogMonitoring/log_monitoring.py)

---

## Prerequisites and How to Run

Please refer to the `README.md` inside each experiment directory for custom execution steps, dependency listings, and sample terminal logs.

### Requirements Summary:
- Java JDK 8 or later.
- Python 3.x.
- Python Libraries: `pandas`, `boto3`, `pycryptodome`, `Pillow`, `azure-identity`, `azure-keyvault-secrets`.
- CloudSim 3.0.3 JAR + dependencies (only required for Ex 1 & Ex 2 simulation execution).
