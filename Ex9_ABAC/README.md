# Implement An Attribute-Based Access Control Mechanism Based On A Particular Scenario

## Aim
To implement an Attribute-Based Access Control (ABAC) authorization mechanism using Python, validating access decisions against user attributes, resource types, and contextual/environmental constraints (time-of-day).

## Theory
Attribute-Based Access Control (ABAC) is an authorization model that evaluates permissions by combining attributes together:
1. **Subject Attributes**: Characteristics of the user requesting access (e.g. Role, Department, Security Clearance).
2. **Resource Attributes**: Characteristics of the object being accessed (e.g. Resource Name, Owner, Sensitivity Level).
3. **Action Attributes**: The operation being attempted (e.g. Read, Write, Delete).
4. **Environment/Contextual Attributes**: Operational context metrics (e.g. Current Time, Location, Device Health).

- **PIP (Policy Information Point)**: The attribute authority that fetches metadata details.
- **PDP (Policy Decision Point)**: The logic engine that compares attributes against access rules.
- **PEP (Policy Enforcement Point)**: The gatekeeper that blocks or permits actions.

ABAC offers higher flexibility and granularity compared to RBAC by allowing fine-grained policies like: *"Only Sales Managers can read Sales Data during business hours (9 AM - 5 PM)."*

## Algorithm
1. **Define Attribute Authority (`AttributeAuthority`)**: Establish a mock user database holding roles, departments, locations, and security clearances.
2. **Implement PDP (`check_access`)**:
   - Receive the user ID, target resource, requested action, and current contextual time.
   - Fetch the subject's department and role from the `AttributeAuthority` (PIP).
   - Define access control rules as dictionaries containing matching fields.
   - Iterate through rules:
     - Check if resource and action match.
     - Validate if subject attributes (role, department) align.
     - Validate contextual attributes (check if current time falls within the allowed time window).
   - If all constraints are satisfied, permit transaction (`True`). Otherwise, block (`False`).
3. **Simulate Scenarios**: Run tests for different users, resources, and timestamps.
4. **Print Results**: Display access results.

## Requirements
- Python 3.x

## How to Run
1. Run the Python script:
   ```bash
   python abac_system.py
   ```

## Sample Output
```
--- Running ABAC Access Control Simulation ---

Evaluating: user1 requesting 'read' on 'sales_data' at 10:00
User can read: True

Evaluating: user1 requesting 'read' on 'sales_data' at 19:00 (After Hours)
User can read: False

Evaluating: user2 requesting 'read' on 'sales_data' at 10:00
User can read: False

Evaluating: user3 requesting 'write' on 'admin_panel'
User can write: True
```

## Result
An Attribute-Based Access Control (ABAC) policy evaluation engine was successfully implemented in Python. The engine validated permissions by correlating user identity attributes, resource attributes, and environmental variables (time-of-day).
