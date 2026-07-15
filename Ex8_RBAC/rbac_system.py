import sys
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import AzureError

# RBAC Configuration
roles = {
    'admin': ['read', 'write', 'delete'],
    'developer': ['read', 'write'],
    'end_user': ['read']
}

user_roles = {
    'user1@example.com': 'admin',
    'user2@example.com': 'developer',
    'user3@example.com': 'end_user'
}

# Simulated database/vault configuration
VAULT_URL = "https://mock-keyvault.vault.azure.net/"

class SimulatedSecretClient:
    """Mock Azure Secret Client for local offline verification."""
    def __init__(self, vault_url, credential):
        self.vault_url = vault_url
        print(f"[AzureMock] SecretClient initialized for Vault: {vault_url}")
        # Mock database storing role policies
        self.vault_secrets = {
            "admin-permissions": "read,write,delete",
            "developer-permissions": "read,write",
            "end-user-permissions": "read"
        }

    def get_secret(self, name):
        class MockSecret:
            def __init__(self, value):
                self.value = value
        
        if name in self.vault_secrets:
            return MockSecret(self.vault_secrets[name])
        raise AzureError("Secret not found")

def get_secret_client():
    """
    Attempts to connect to Azure KeyVault.
    Falls back to SimulatedSecretClient if offline or using placeholder URI.
    """
    if "mock-keyvault" in VAULT_URL or "<the_keyvault_url>" in VAULT_URL:
        return SimulatedSecretClient(VAULT_URL, None)
    
    try:
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=VAULT_URL, credential=credential)
        # Test connection
        client.get_secret("test-secret")
        return client
    except Exception as e:
        print(f"[AzureSDK] Warning: Real Azure KeyVault connection failed ({e}). Falling back to mock client.")
        return SimulatedSecretClient(VAULT_URL, None)

def check_access(user_email, permission, secret_client):
    """
    Checks if a user is authorized to perform a specific action (permission)
    by fetching role permissions from the KeyVault (or simulated vault).
    """
    if user_email not in user_roles:
        print(f"[AccessControl] User '{user_email}' not found in user database.")
        return False
        
    assigned_role = user_roles[user_email]
    secret_name = f"{assigned_role.replace('_', '-')}-permissions"
    
    try:
        # Retrieve permissions list from Azure KeyVault (or mock)
        secret = secret_client.get_secret(secret_name)
        allowed_permissions = secret.value.split(',')
        
        return permission in allowed_permissions
    except Exception as e:
        print(f"[AccessControl] Error retrieving permissions for role '{assigned_role}': {e}")
        # Fallback to local roles dictionary
        return permission in roles.get(assigned_role, [])

def main():
    # Initialize connection to Azure Key Vault client
    secret_client = get_secret_client()

    print("\n--- Simulating Access Control Checks ---")
    
    # 1. Test Admin Access (e.g. user1@example.com wants to write)
    user1 = 'user1@example.com'
    can_write = check_access(user1, 'write', secret_client)
    print(f"User '{user1}' role: {user_roles[user1]}")
    print(f"User can write: {can_write}")

    # 2. Test Developer Access (e.g. user2@example.com wants to delete)
    user2 = 'user2@example.com'
    can_delete = check_access(user2, 'delete', secret_client)
    print(f"\nUser '{user2}' role: {user_roles[user2]}")
    print(f"User can delete: {can_delete}")

    # 3. Test End User Access (e.g. user3@example.com wants to read)
    user3 = 'user3@example.com'
    can_read = check_access(user3, 'read', secret_client)
    print(f"\nUser '{user3}' role: {user_roles[user3]}")
    print(f"User can read: {can_read}")

if __name__ == '__main__':
    main()

# EXPECTED OUTPUT:
# User can write: True
