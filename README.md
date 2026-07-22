# 🎓 5th Semester Lab Experiments (CIT)

Welcome to the central repository for my **5th Semester Lab Experiments** at **Chennai Institute of Technology (CIT)**. This repository contains the complete implementation and source code for various academic lab courses.

---

## 📚 Courses & Faculty Mentors

| Course Code / Abbreviation | Course Name | Faculty Mentor |
| :--- | :--- | :--- |
| **SPC** | Security & Privacy in Cloud | **Mr. V. Robin Britto** |
| **GenAI & LLM** | Generative AI & Large Language Models | **Ms. Vishali** |
| **NS** | Network Security | **Ms. P. Vidhya Lakshmi** |
| **MC** | Modern Cryptography | **Mr. M. Sithranjan** |

---

## 📁 Repository Structure

Here is a breakdown of the lab components included in this workspace:

### ☁️ [SPC](./SPC) — Security & Privacy in Cloud
*Guided by "Mr. V. Robin Britto"*
Focused on cloud security simulations, identity access management, policies, and forensic log auditing.
- Cloud Scheduling & Resource Management Simulations
- Log Forensics & Log Monitoring Systems
- Secure File Sharing Configurations
- Data Anonymization & Image Encryption/Obfuscation
- Role-Based Access Control (RBAC) & Attribute-Based Access Control (ABAC)

### 🤖 [GenAI & LLM](./GenAI%26LLM) — Generative AI & Large Language Models
*Guided by "Ms. Vishali"*
Explores the core fundamentals of building, training, and working with modern GenAI and transformer models.
- Tokenization & Token IDs exploration
- Dense Embedding representations
- Sequence Modelling and text generation scripts
- Interactive Jupyter Notebooks for model training/experimentation

### 🔒 [NS](./NS) — Network Security
*Guided by "Ms. P. Vidhya Lakshmi"*
Practical implementations of fundamental network defense mechanisms, attacks, and cryptographic protocols.
- MD5 Hash Collision attacks and binary collisions
- Cryptographic Hash-based Message Authentication Codes (HMAC)
- Buffer Overflow vulnerability demonstrations (memory manipulation)

### 🔑 [MC](./MC) — Modern Cryptography
*Guided by "Mr. M. Sithranjan"*
Implementations of cryptographic foundations, secure key distribution systems, and simulations of security architectures.
- Custom Scheduling & Resource Management Simulations
- Log Forensics & Secure File Sharing Simulations

---

## 🛠️ Getting Started

### Prerequisites
Make sure you have the following environments configured to run these experiments:
- **Python 3.x** (for GenAI, Cloud scripts, and Network Security scripts)
- **Java JDK 8+** (for CloudSim simulations in SPC and MC)
- **GCC / C Compiler** (for low-level buffer overflow demonstrations in NS)

### Running a Python script
```bash
python <path_to_script>.py
```

### Running C-based Security Demos
To compile and execute the buffer overflow experiment:
```bash
gcc -o overflow experiment_3_buffer_overflow.c -fno-stack-protector -z execstack
./overflow
```

---

## 🏛️ Chennai Institute of Technology
*Department of Computer Science and Engineering(CyberSecurity)*  
*Chennai*
