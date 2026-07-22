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
*Guided by Mr. V. Robin Britto*
1. Experiment 1 - Cloud Scheduling Simulation
2. Experiment 2 - Resource Management Simulation
3. Experiment 3 - Log Forensics Simulation
4. Experiment 4 - Secure File Sharing Simulation
5. Experiment 5 - Data Anonymization Techniques
6. Experiment 6 - Image Encryption
7. Experiment 7 - Image Obfuscation
8. Experiment 8 - Role-Based Access Control
9. Experiment 9 - Attribute-Based Access Control
10. Experiment 10 - Log Monitoring and Incident Management

### 🤖 [GenAI & LLM](./GenAI%26LLM) — Generative AI & Large Language Models
*Guided by Ms. Vishali*
1. Experiment 1 - Basic Text Generation and Model Setup
2. Experiment 2 - Interactive Training & Notebook Verification
3. Experiment 3 (Program 1) - Tokenization Exploration
4. Experiment 3 (Program 2) - Token IDs Conversion
5. Experiment 3 (Program 3) - Dense Embeddings Generation
6. Experiment 3 (Program 4) - Sequence Modelling

### 🔒 [NS](./NS) — Network Security
*Guided by Ms. P. Vidhya Lakshmi*
1. Experiment 1 - MD5 Collision Attacks and Binary Demonstration
2. Experiment 2 - Cryptographic Hash-based Message Authentication Codes (HMAC)
3. Experiment 3 - Buffer Overflow Vulnerability and Memory Manipulation

### 🔑 [MC](./MC) — Modern Cryptography
*Guided by Mr. M. Sithranjan*
1. Experiment 1 - Custom Scheduling Simulation
2. Experiment 2 - Resource Management Simulation
3. Experiment 3 - Log Forensics Simulation
4. Experiment 4 - Secure File Sharing Simulation

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

### Running Java/CloudSim Simulations
To compile and run the Java experiments (e.g., in SPC or MC) which require dependency `.jar` libraries:

**On Windows (PowerShell/CMD):**
```powershell
# Navigate to the experiment directory (e.g., SPC/Ex1_CloudScheduling)
cd SPC/Ex1_CloudScheduling

# Compile the Java file with classpaths
javac -cp ".;cloudsim-3.0.3.jar;commons-math3-3.6.1.jar" CustomSchedulingSimulation.java

# Run the simulation
java -cp ".;cloudsim-3.0.3.jar;commons-math3-3.6.1.jar" CustomSchedulingSimulation
```

**On Linux / macOS:**
```bash
# Navigate to the experiment directory (e.g., SPC/Ex1_CloudScheduling)
cd SPC/Ex1_CloudScheduling

# Compile the Java file with classpaths
javac -cp ".:cloudsim-3.0.3.jar:commons-math3-3.6.1.jar" CustomSchedulingSimulation.java

# Run the simulation
java -cp ".:cloudsim-3.0.3.jar:commons-math3-3.6.1.jar" CustomSchedulingSimulation
```

---

## 🏛️ Chennai Institute of Technology
*Department of Computer Science and Engineering / Information Technology*  
*Affiliated to Anna University, Chennai.*
