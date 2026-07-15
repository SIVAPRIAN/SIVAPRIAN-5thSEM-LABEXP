class AttributeAuthority:
    """
    Simulates a centralized Attribute Authority (PIP - Policy Information Point)
    that retrieves properties of users and resources from database sources.
    """
    def __init__(self):
        # Mock database of users and their attributes
        self.user_db = {
            'user1': {
                'role': 'Manager',
                'department': 'Sales',
                'location': 'US',
                'security_clearance': 3
            },
            'user2': {
                'role': 'Developer',
                'department': 'Engineering',
                'location': 'UK',
                'security_clearance': 2
            },
            'user3': {
                'role': 'Admin',
                'department': 'IT',
                'location': 'Global',
                'security_clearance': 5
            }
        }

    def get_attribute(self, user_id, attribute_name):
        """
        Query the user database to retrieve the requested attribute value.
        """
        user_info = self.user_db.get(user_id)
        if user_info and attribute_name in user_info:
            return user_info[attribute_name]
        return None

def check_access(user_id, resource_id, action, current_time=10):
    """
    Policy Decision Point (PDP) that evaluates attributes against policies.
    """
    attribute_authority = AttributeAuthority()

    # Define ABAC access control policies
    access_control_policies = [
        {
            'role': 'Manager',
            'department': 'Sales',
            'resource': 'sales_data',
            'action': 'read',
            'time_window': (9, 17) # Business hours check
        },
        {
            'role': 'Admin',
            'resource': 'admin_panel',
            'action': 'write',
            'time_window': (0, 24)
        }
    ]

    # Retrieve subject attributes from the Attribute Authority
    user_role = attribute_authority.get_attribute(user_id, 'role')
    user_department = attribute_authority.get_attribute(user_id, 'department')

    # Evaluate the requested action against policies
    for policy in access_control_policies:
        # Check if the policy targets the current resource and action
        if policy['resource'] == resource_id and policy['action'] == action:
            # Check subject attributes (role & department)
            role_match = policy.get('role') is None or policy['role'] == user_role
            dept_match = policy.get('department') is None or policy['department'] == user_department
            
            # Check contextual attribute (simulation of time-of-day attribute)
            start_time, end_time = policy.get('time_window', (0, 24))
            time_match = start_time <= current_time <= end_time

            if role_match and dept_match and time_match:
                return True

    return False

def main():
    print("--- Running ABAC Access Control Simulation ---")

    # Scenario 1: user1 (Manager in Sales) tries to read 'sales_data' during business hours (10:00)
    user1 = 'user1'
    resource1 = 'sales_data'
    action1 = 'read'
    time1 = 10 # 10 AM
    can_read_1 = check_access(user1, resource1, action1, time1)
    print(f"\nEvaluating: {user1} requesting '{action1}' on '{resource1}' at {time1}:00")
    print(f"User can read: {can_read_1}")

    # Scenario 2: user1 tries to read 'sales_data' after hours (19:00 / 7 PM)
    time2 = 19 # 7 PM
    can_read_2 = check_access(user1, resource1, action1, time2)
    print(f"\nEvaluating: {user1} requesting '{action1}' on '{resource1}' at {time2}:00 (After Hours)")
    print(f"User can read: {can_read_2}")

    # Scenario 3: user2 (Developer in Engineering) tries to read 'sales_data' at 10:00
    user2 = 'user2'
    can_read_3 = check_access(user2, resource1, action1, time1)
    print(f"\nEvaluating: {user2} requesting '{action1}' on '{resource1}' at {time1}:00")
    print(f"User can read: {can_read_3}")

    # Scenario 4: user3 (Admin in IT) tries to write to 'admin_panel'
    user3 = 'user3'
    resource2 = 'admin_panel'
    action2 = 'write'
    can_write_4 = check_access(user3, resource2, action2, time1)
    print(f"\nEvaluating: {user3} requesting '{action2}' on '{resource2}'")
    print(f"User can write: {can_write_4}")

if __name__ == '__main__':
    main()

# EXPECTED OUTPUT:
# User can read: True
