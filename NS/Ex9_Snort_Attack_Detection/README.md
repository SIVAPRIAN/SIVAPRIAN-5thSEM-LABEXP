# Lab Experiment 9: Generate a Network Attack and Detect It Using Snort

## 1. Aim
To simulate a network attack (such as ICMP Flood / Port Scan) and detect it using Snort IDS with custom detection rules.

## 2. Algorithm
1. **Setup Snort**: Install and configure Snort on a Linux machine, ensuring it is monitoring the correct interface.
2. **Write Attack Detection Rules**: Define Snort rules to detect specific network attack signatures (ICMP ping flood, Nmap port scan, SYN flood).
3. **Start Snort in IDS Mode**: Run Snort with `snort.conf` and `local.rules` enabled.
4. **Launch the Attack**: Use the attacker machine (or the same host with tools like `hping3`, `nmap`, or `ping -f`) to generate suspicious traffic.
5. **Observe Detection**: Check the Snort console/log files for alerts corresponding to the attack.

## 3. Implementation Steps
1. **Configure Custom Rules** in `/etc/snort/rules/local.rules`:
   - **(a) Detect ICMP Ping Flood**:
     ```text
     alert icmp any any -> any any (msg:"ICMP Flood Detected"; sid:3000001; rev:1;)
     ```
   - **(b) Detect Nmap Port Scan (TCP SYN)**:
     ```text
     alert tcp any any -> any any (flags:S; msg:"Nmap SYN Scan Detected"; sid:3000002; rev:1;)
     ```
   - **(c) Detect UDP Flood**:
     ```text
     alert udp any any -> any any (msg:"UDP Flood Detected"; sid:3000003; rev:1;)
     ```
2. **Run Snort in IDS Mode**:
   ```bash
   sudo snort -A console -q -c /etc/snort/snort.conf -i eth0
   ```
3. **Generate Attacks**:
   - **(a) ICMP Flood (Ping Flood)**:
     ```bash
     ping -f 192.168.1.10
     # Or using hping3:
     sudo hping3 -1 --flood -a 192.168.1.10 192.168.1.10
     ```
   - **(b) Port Scan using Nmap**:
     ```bash
     nmap -sS 192.168.1.10
     ```
   - **(c) UDP Flood using hping3**:
     ```bash
     sudo hping3 --udp -p 80 --flood 192.168.1.10
     ```

## 4. Output
> [!IMPORTANT]
> **Snort Console Alert Output:**
> ```text
> [**] [1:3000001:1] ICMP Flood Detected [**]
> [Priority: 0] {ICMP} 192.168.1.20 -> 192.168.1.10
> 
> [**] [1:3000002:1] Nmap SYN Scan Detected [**]
> [Priority: 0] {TCP} 192.168.1.20:50512 -> 192.168.1.10:22
> ```
> * Logs are also stored in: `/var/log/snort/alert`

## 5. Result
* Successfully generated ICMP Flood, SYN Scan, and UDP Flood attacks using `ping`, `nmap`, and `hping3`.
* Snort successfully detected these attacks, displaying alerts in the console and writing them to the log files.
