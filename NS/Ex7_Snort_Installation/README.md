# Lab Experiment 7: Explore and Install Snort Intrusion Detection Tool

## 1. Aim
To explore and install the Snort IDS tool, configure it to monitor network traffic, and test its functionality using sample attacks.

## 2. Algorithm
1. **Environment Setup**:
   - Install Snort on Linux (e.g., Ubuntu/Kali).
   - Update system packages.
2. **Snort Installation**:
   - Download and install Snort from repositories or source.
3. **Configuration**:
   - Locate the Snort configuration file (`/etc/snort/snort.conf`).
   - Define network variables (`HOME_NET`, `EXTERNAL_NET`).
   - Add custom rules to detect suspicious traffic.
4. **Running Snort**:
   - Run Snort in different modes: packet logger, sniffer, and IDS.
   - Use test packets to trigger alerts.
5. **Verification**:
   - Check log files and alert messages to verify Snort detection.

## 3. Installation & Run Instructions
1. **Update system and install Snort**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install snort -y
   ```
2. **Verify Installation**:
   ```bash
   snort -V
   ```
3. **Run Snort in Sniffer Mode**:
   ```bash
   sudo snort -i eth0 -v
   ```
4. **Run Snort in Packet Logger Mode**:
   ```bash
   sudo snort -i eth0 -dev -l /var/log/snort/
   ```
5. **Run Snort in IDS Mode with Rules**:
   ```bash
   sudo snort -A console -q -c /etc/snort/snort.conf -i eth0
   ```
6. **Testing with Custom Rule**:
   Add the following rule to `/etc/snort/rules/local.rules`:
   ```text
   alert icmp any any -> any any (msg:"ICMP Ping detected"; sid:1000001; rev:1;)
   ```

## 4. Output
> [!IMPORTANT]
> **Verification Outputs:**
>
> **Snort Version Check Output:**
> ```text
>    ,,_     -*> Snort! <*-
>   o"  )~   Version 2.9.20
>    ''''    By Martin Roesch & The Snort Team
> ```
>
> **IDS Alert Console Output (upon pinging):**
> ```text
> [**] [1:1000001:1] ICMP Ping detected [**]
> [Priority: 0]
> ```

## 5. Result
* Snort installed successfully.
* Able to run Snort in Sniffer, Logger, and IDS modes.
* Custom ICMP detection rule worked and generated alerts.
