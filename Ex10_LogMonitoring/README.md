# Develop A Log Monitoring System With Incident Management In The Cloud

## Aim
To develop a cloud log monitoring and incident response system using Python, simulating an AWS Lambda function triggered by Amazon CloudWatch log events to automatically create incident tickets in AWS Systems Manager Incident Manager.

## Theory
Continuous log monitoring is essential to ensure operational integrity and security compliance in cloud environments.
- **Log Aggregator (Amazon CloudWatch)**: Centralizes system, network, and application log events.
- **Serverless Trigger (AWS Lambda)**: Parses the aggregated log stream in real time. It performs pattern matching and security rules to determine if a log entry represents a threat or anomaly.
- **Incident Response System (AWS Systems Manager Incident Manager)**: Automatically creates incident response tickets (escalating to on-call engineers via SMS/Pagers, launching runbooks, and compiling records) when a critical alert is triggered.

This pipeline reduces Mean Time to Resolution (MTTR) by replacing manual ticketing with serverless alert-to-incident automation.

## Algorithm
1. **Configure Log Ingestion**: Setup mock input event structures matching AWS CloudWatch log streams.
2. **Lambda Handler Function (`generate_incident`)**:
   - Receive the log event containing `logGroup`, `logStream`, and `message`.
   - Parse and extract the log parameters.
   - Run keyword pattern matching:
     - Flag statements containing "unauthorized" or "denied" as **Critical Threat** (Severity Level 1).
     - Flag statements containing "anomaly" or "exceeded" as **Major Anomaly** (Severity Level 2).
     - Treat normal API health check traffic as operational logs (Severity Level 3 - Low / Ignore).
   - If a threat/anomaly is detected:
     - Instantiate the SSM `incident-manager` client.
     - Call the `create_incident` API, passing the log stream name as the incident title, the log group and message as description details, and the evaluated impact, urgency, and severity levels.
3. **Execute Simulation**: Feed sample logs (unauthorized login, CPU threshold alert, normal operations) into the Lambda engine.
4. **Display Dashboard**: Print the open incident tickets.

## Requirements
- Python 3.x
- boto3 (`pip install boto3`)

## How to Run
1. Run the Python script:
   ```bash
   python log_monitoring.py
   ```

## Sample Output
```
--- Simulating CloudWatch Log Stream & Incident Management ---

[Monitor] Received event from Log Stream: Auth-Stream-01
[MockIncidentManager] Created Incident ticket: inc-0001

[Monitor] Received event from Log Stream: Gateway-Stream-05
[MockIncidentManager] Created Incident ticket: inc-0002

[Monitor] Received event from Log Stream: Gateway-Stream-05
[Monitor] Log entry classified as normal operational traffic. No incident created.

--- Current Incident Dashboard ---
[inc-0001] TITLE: Anomaly Detected in Log Stream: Auth-Stream-01
       SEVERITY: Level 1 | STATUS: Open
       DESC: Anomaly detected in log group: Production-Auth-Group | Log message: Unauthorized access attempt on database server from IP 192.168.1.100.
--------------------------------------------------
[inc-0002] TITLE: Anomaly Detected in Log Stream: Gateway-Stream-05
       SEVERITY: Level 2 | STATUS: Open
       DESC: Anomaly detected in log group: Production-APIGateway | Log message: Anomaly: CPU utilization exceeded safety threshold of 90%.
--------------------------------------------------
```

## Result
A serverless log monitoring and incident management pipeline was successfully simulated in Python. The script processed streams of CloudWatch logs, parsed security incidents, and automatically logged tickets in the Incident Manager dashboard.
