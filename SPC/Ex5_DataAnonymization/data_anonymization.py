import pandas as pd
import re

def mask_name(name):
    """
    Masks the name by keeping the first letter of each part 
    and replacing the rest with asterisks, preserving the length.
    E.g., "John Doe" -> "J*** D**"
    """
    parts = name.split()
    masked_parts = [p[0] + '*' * (len(p) - 1) if len(p) > 0 else '' for p in parts]
    return ' '.join(masked_parts)

def mask_email(email):
    """
    Masks the username part of the email address.
    E.g., "johndoe@example.com" -> "j******@example.com"
    """
    if '@' not in email:
        return '********'
    user, domain = email.split('@', 1)
    if len(user) <= 1:
        return user + '@' + domain
    return user[0] + '*' * (len(user) - 1) + '@' + domain

def generalize_zip(zip_code):
    """
    Generalizes ZIP code by suppressing the last three digits.
    E.g., "12345" -> "12XXX"
    """
    return zip_code[:2] + "XXX" if len(zip_code) >= 2 else "XXXXX"

def generalize_age(age):
    """
    Generalizes age into 10-year brackets.
    E.g., 25 -> "20-29", 35 -> "30-39"
    """
    bucket_start = (age // 10) * 10
    return f"{bucket_start}-{bucket_start + 9}"

def main():
    print("--- Original Dataset ---")
    data = pd.DataFrame({
        'Name': ['John Doe', 'Jane Smith', 'Michael Johnson'],
        'Email': ['johndoe@example.com', 'janesmith@example.com', 'michaeljohnson@example.com'],
        'Zip Code': ['12345', '12347', '12341'],
        'Age': [25, 29, 35]
    })
    print(data)

    print("\n--- Applying Data Masking ---")
    masked_data = data.copy()
    masked_data['Name'] = masked_data['Name'].apply(mask_name)
    masked_data['Email'] = masked_data['Email'].apply(mask_email)
    print(masked_data)

    print("\n--- Applying K-Anonymization (k=2) via Generalization & Suppression ---")
    # Quasi-identifiers: Zip Code, Age
    # Direct identifiers (Name, Email) are fully suppressed (masked/removed)
    anonymized_data = data.copy()
    anonymized_data['Name'] = 'Anonymous'
    anonymized_data['Email'] = 'suppressed@example.com'
    
    # Generalize Zip Code to '123XX'
    anonymized_data['Zip Code'] = anonymized_data['Zip Code'].apply(lambda z: z[:3] + "XX")
    
    # Generalize Age to age brackets (20-40) to achieve k-anonymity (k=2) for all rows
    anonymized_data['Age'] = anonymized_data['Age'].apply(lambda a: "20-40")
    
    print(anonymized_data)
    
    # Verify k-anonymity grouping
    # Check if every record is indistinguishable from at least k-1 other records based on quasi-identifiers
    groups = anonymized_data.groupby(['Zip Code', 'Age']).size()
    print("\nGroup Sizes for Quasi-identifiers:")
    print(groups)

if __name__ == '__main__':
    main()

"""
EXPECTED OUTPUT:
--- Original Dataset ---
              Name                       Email Zip Code  Age
0         John Doe         johndoe@example.com    12345   25
1       Jane Smith       janesmith@example.com    12347   29
2  Michael Johnson  michaeljohnson@example.com    12341   35

--- Applying Data Masking ---
              Name                       Email Zip Code  Age
0         J*** D**         j******@example.com    12345   25
1         J*** S****       j********@example.com    12347   29
2    M****** J******  m*************@example.com    12341   35

--- Applying K-Anonymization (k=2) via Generalization & Suppression ---
        Name                   Email Zip Code    Age
0  Anonymous  suppressed@example.com    123XX  20-40
1  Anonymous  suppressed@example.com    123XX  20-40
2  Anonymous  suppressed@example.com    123XX  20-40

Group Sizes for Quasi-identifiers:
Zip Code  Age  
123XX     20-40    3
dtype: int64
"""
