# Implement A Role-Based Access Control Mechanism In A Specific Scenario

## Aim
To design and implement a Role-Based Access Control (RBAC) authorization system using Python, securing role-permission mappings through integration (and simulation) of Microsoft Azure KeyVault.

## Theory
Role-Based Access Control (RBAC) restricts system access to authorized users based on their assigned role within the organization.
- **Subject/User**: Entity requesting access (e.g. `user1@example.com`).
- **Role**: A job function that defines authority levels (e.g. `admin`, `developer`, `end_user`).
- **Permission**: An approval to perform a operation on a resource (e.g. `read`, `write`, `delete`).
- **Azure KeyVault**: A cloud-based secret management service. In a secure cloud-native architecture, permissions shouldn't be hardcoded; they should be loaded dynamically from a secured vault. This separates policy management from codebase logic.

## Algorithm
1. **Initialize Azure Credentials**: Set up `DefaultAzureCredential` to authenticate with Microsoft Azure.
2. **Instantiate SecretClient**: Configure the client with the vault URI (`https://<vault-name>.vault.azure.net`).
3. **Map Users to Roles**: Define a lookup mapping containing user email identifiers and their assigned roles.
4. **Access Verification Engine (`check_access`)**:
   - Receive the user ID (email) and the requested operation (permission).
   - Resolve the user's role.
   - Fetch the secret corresponding to the role's permission list (e.g., secret name `admin-permissions` value `read,write,delete`) from Azure KeyVault.
   - Parse the secret value string into an array of allowed permissions.
   - Verify if the requested permission exists within the allowed list. Return `True` or `False`.
5. **Print Outputs**: Demonstrate checks for various roles and log the outcomes.

## Requirements
- Python 3.x
- azure-identity (`pip install azure-identity`)
- azure-keyvault-secrets (`pip install azure-keyvault-secrets`)

## How to Run
1. Run the Python script:
   ```bash
   python rbac_system.py
   ```

## Sample Output
```
[AzureMock] SecretClient initialized for Vault: https://mock-keyvault.vault.azure.net/

--- Simulating Access Control Checks ---
User 'user1@example.com' role: admin
User can write: True

User 'user2@example.com' role: developer
User can delete: False

User 'user3@example.com' role: end_user
User can read: True
```

## Result
A Role-Based Access Control (RBAC) mechanism was successfully implemented in Python. By securely resolving role-permission strings via Azure KeyVault, the system authenticated access requests dynamically.
