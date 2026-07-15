import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Mock Incident Manager Database for local validation
incidents_db = []

class MockIncidentManagerClient:
    """Mock boto3 client for incident-manager to enable local execution."""
    def create_incident(self, title, description, impact, urgency, severity):
        incident_id = f"inc-{len(incidents_db) + 1:04d}"
        incident_record = {
            "incident_id": incident_id,
            "title": title,
            "description": description,
            "impact": impact,
            "urgency": urgency,
            "severity": severity,
            "status": "Open"
        }
        incidents_db.append(incident_record)
        print(f"[MockIncidentManager] Created Incident ticket: {incident_id}")
        return {"incidentArn": f"arn:aws:ssm-incidents::123456789012:incident/{incident_id}"}

def get_incident_manager_client():
    """
    Returns a real AWS Incident Manager client if AWS credentials are active,
    otherwise falls back to the Mock client.
    """
    try:
        # Check if AWS credentials exist
        session = boto3.Session()
        credentials = session.get_credentials()
        if credentials is not None:
            return boto3.client('incident-manager')
    except (NoCredentialsError, ClientError):
        pass
    return MockIncidentManagerClient()

def generate_incident(event, context=None):
    """
    Lambda Handler function triggered by CloudWatch Log Events.
    Parses details, evaluates threat level, and triggers Incident Manager.
    """
    try:
        # Extract metadata from CloudWatch Event Detail
        detail = event.get('detail', {})
        log_group = detail.get('logGroup', 'Unknown-LogGroup')
        log_stream = detail.get('logStream', 'Unknown-LogStream')
        log_message = detail.get('message', 'No message body provided')

        print(f"\n[Monitor] Received event from Log Stream: {log_stream}")
        
        # Analyze log message for severe events
        is_threat = False
        severity_level = 3 # Default info/low severity
        
        lower_msg = log_message.lower()
        if "unauthorized" in lower_msg or "denied" in lower_msg:
            is_threat = True
            severity_level = 1 # Critical
        elif "anomaly" in lower_msg or "exceeded" in lower_msg:
            is_threat = True
            severity_level = 2 # Major

        if is_threat:
            incident_title = f'Anomaly Detected in Log Stream: {log_stream}'
            incident_description = f'Anomaly detected in log group: {log_group}\nLog message: {log_message}'
            
            # Retrieve client (Real AWS or Mock Client)
            incident_service = get_incident_manager_client()
            
            # API parameters matching AWS Systems Manager Incident Manager specifications
            incident_service.create_incident(
                title=incident_title,
                description=incident_description,
                impact=severity_level,   # Define the impact level (1-5)
                urgency=severity_level,  # Define the urgency level
                severity=severity_level  # Define the severity level
            )
        else:
            print(f"[Monitor] Log entry classified as normal operational traffic. No incident created.")

    except Exception as e:
        print(f"[Error] Lambda execution failed: {e}")

def main():
    print("--- Simulating CloudWatch Log Stream & Incident Management ---")

    # Sample input event representing a security log alert
    event1 = {
        "detail": {
            "logGroup": "Production-Auth-Group",
            "logStream": "Auth-Stream-01",
            "message": "Unauthorized access attempt on database server from IP 192.168.1.100."
        }
    }

    # Sample input event representing a performance anomaly
    event2 = {
        "detail": {
            "logGroup": "Production-APIGateway",
            "logStream": "Gateway-Stream-05",
            "message": "Anomaly: CPU utilization exceeded safety threshold of 90%."
        }
    }

    # Sample input event representing normal traffic
    event3 = {
        "detail": {
            "logGroup": "Production-APIGateway",
            "logStream": "Gateway-Stream-05",
            "message": "API health check returned 200 OK."
        }
    }

    # Trigger Lambda functions
    generate_incident(event1)
    generate_incident(event2)
    generate_incident(event3)

    # Print created incidents
    print("\n--- Current Incident Dashboard ---")
    for inc in incidents_db:
        print(f"[{inc['incident_id']}] TITLE: {inc['title']}")
        print(f"       SEVERITY: Level {inc['severity']} | STATUS: {inc['status']}")
        print(f"       DESC: {inc['description'].replace('\n', ' | ')}")
        print("-" * 50)

if __name__ == '__main__':
    main()

# EXPECTED OUTPUT:
# [MockIncidentManager] Created Incident ticket: inc-0001
# [MockIncidentManager] Created Incident ticket: inc-0002
