# Lab Experiment 8: Implement Firewall Rules using Snort

## 1. Aim
To implement firewall-like packet filtering rules using Snort IDS/IPS and demonstrate how Snort can block or allow specific traffic.

## 2. Algorithm
1. **Install and Configure Snort**: Ensure Snort is installed and configured on the machine (`/etc/snort/snort.conf`).
2. **Define Rule Base**: Write custom Snort rules inside `local.rules` to allow/deny specific traffic based on protocol, IP, and port.
3. **Enable IPS (Inline) Mode**: Run Snort in inline mode using `NFQUEUE` or `afpacket` to actively block traffic.
4. **Apply Firewall Rules**: Test rules like blocking ICMP ping, blocking HTTP port 80, or allowing only specific IP addresses.
5. **Verify Effectiveness**: Generate traffic (ping, curl, netcat) and observe whether Snort allows or blocks the packets.

## 3. Configuration & Running Rules
1. **Configure Firewall-like Rules** in `/etc/snort/rules/local.rules`:
   - **(a) Block all ICMP ping requests**:
     ```text
     drop icmp any any -> any any (msg:"Firewall Rule: ICMP Ping Blocked"; sid:2000001; rev:1;)
     ```
   - **(b) Block HTTP traffic on port 80**:
     ```text
     drop tcp any any -> any 80 (msg:"Firewall Rule: Blocked HTTP Traffic"; sid:2000002; rev:1;)
     ```
   - **(c) Allow only traffic from a specific trusted IP (192.168.1.100)**:
     ```text
     pass tcp 192.168.1.100 any -> any any (msg:"Firewall Rule: Allow Trusted Host"; sid:2000003; rev:1;)
     ```
2. **Running Snort in IPS (Inline) Mode**:
   ```bash
   sudo iptables -I INPUT -j NFQUEUE --queue-num 0
   sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0
   sudo snort -Q --daq nfq --daq-var queue=0 -c /etc/snort/snort.conf -i eth0
   ```

## 4. Output (Testing)
> [!IMPORTANT]
> **Verification Outputs:**
>
> **Case 1: ICMP Ping Blocked**
> * Command: `ping 8.8.8.8`
> * Snort Output:
>   ```text
>   [Drop] [**] Firewall Rule: ICMP Ping Blocked [**]
>   ```
> * Result: Ping fails &rarr; packets dropped.
>
> **Case 2: HTTP Traffic Blocked**
> * Command: `curl http://example.com`
> * Snort Output:
>   ```text
>   [Drop] [**] Firewall Rule: Blocked HTTP Traffic [**]
>   ```
> * Result: Connection blocked.
>
> **Case 3: Trusted IP Allowed**
> * Traffic from `192.168.1.100` passes, other IPs are blocked.

## 5. Result
The experiment successfully demonstrated the implementation of firewall-like packet filtering rules using Snort IDS/IPS, showing how specific traffic can be allowed or blocked, thereby proving Snort’s capability to function as a lightweight intrusion prevention and traffic control system.
