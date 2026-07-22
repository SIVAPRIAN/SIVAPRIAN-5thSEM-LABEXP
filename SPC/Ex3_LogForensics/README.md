# Simulate Log Forensics Using Cloud Sim

## Aim
To simulate a cloud monitoring environment and perform cloud log forensics using log analysis algorithms to detect suspicious activities and metric-based anomalies.

## Theory
Log forensics in cloud computing is the process of reconstructing events by analyzing logs from cloud infrastructures, virtual machines, applications, and network interfaces.
- **Suspicious Activities**: These are behavioral actions that represent potential security violations or policy breaches. Examples include unauthorized access attempts, mass outbound traffic to outside IPs (data exfiltration), and concurrent/multiple-IP login failures.
- **Anomalies**: These are deviations from the normal statistical operational baselines of virtual resources, such as CPU utilization spikes, RAM depletion, and unusually large file transfers.

This simulator captures logs generated inside a cloud datacenter and implements log parser and correlation rules to flag threats and alert the system administrators.

## Algorithm
1. **Define Log Attributes**: Establish a structured data format (`LogEntry`) containing:
   - Metadata: Timestamp, Source IP, Destination IP, Log Message.
   - Resource metrics: CPU Usage, RAM Usage, File Transfer Size.
2. **Collect/Generate Logs**: Simulate a dataset representing both standard operations and attack patterns (e.g. data exfiltration, unauthorized login, resource spikes).
3. **Analyze Suspicious Activities**:
   - Loop through the log list.
   - Match keywords using string patterns: "unauthorized", "high volume of outbound", "unusual login".
   - Flag matches as Suspicious.
4. **Analyze Anomalies**:
   - Set threshold constants: `CPU_THRESHOLD = 90%`, `MEMORY_THRESHOLD = 95%`, `SIZE_THRESHOLD = 10GB`.
   - Loop through the log list and identify logs where metric parameters cross these thresholds.
   - Flag matches as Anomalies.
5. **Print Audit Report**: Format and output the list of flagged events.

## Requirements
- Java Development Kit (JDK) 8 or later.

## How to Run
1. Compile the Java code:
   ```bash
   javac LogForensicsSimulation.java
   ```
2. Run the application:
   ```bash
   java LogForensicsSimulation
   ```

## Sample Output
```
Initializing Cloud Log Forensics Engine...

Detected Suspicious Activities:
1. Timestamp: 2023-06-01 10:23:45, Source IP: 192.168.1.100, Destination IP: 203.0.113.10, Log Message: Unauthorized access attempt.
2. Timestamp: 2023-06-02 14:55:12, Source IP: 192.168.1.150, Destination IP: 203.0.113.20, Log Message: High volume of outbound traffic to suspicious IP address.
3. Timestamp: 2023-06-03 09:10:27, Source IP: 192.168.1.200, Destination IP: 203.0.113.30, Log Message: Unusual login activity from multiple IP addresses.

Detected Anomalies:
1. Timestamp: 2023-06-01 12:05:30, Source IP: 192.168.1.75, Destination IP: 203.0.113.10, Log Message: Abnormal CPU utilization exceeding threshold.
2. Timestamp: 2023-06-02 16:30:15, Source IP: 192.168.1.110, Destination IP: 203.0.113.20, Log Message: Unusually large file transfer size.
3. Timestamp: 2023-06-03 11:40:21, Source IP: 192.168.1.180, Destination IP: 203.0.113.30, Log Message: Unusual memory consumption pattern.
```

## Result
A log forensics simulation system was successfully developed and executed in Java. The system parsed cloud log records and detected both rule-based suspicious security events and parameter-based operational anomalies.
