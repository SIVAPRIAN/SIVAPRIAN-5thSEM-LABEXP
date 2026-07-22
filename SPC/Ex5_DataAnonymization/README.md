# Implement Data Anonymization Techniques Over The Simple Dataset

## Aim
To implement data anonymization techniques (including data masking, attribute generalization, and $k$-anonymity enforcement) on a simple dataset using Python and Pandas.

## Theory
Data privacy regulations (like GDPR and HIPAA) require that personal data is protected to prevent the identification of individual subjects.
1. **Data Masking**: Replacing sensitive personal information with non-sensitive placeholders while preserving format and length (e.g. replacing letters in names/emails with asterisks).
2. **K-Anonymity**: A dataset satisfies $k$-anonymity if the information for each person contained in the release cannot be distinguished from at least $k-1$ other individuals whose information also appears in the release.
   - **Identifiers**: Explicitly identify a person (e.g., Name, Email). These are suppressed.
   - **Quasi-Identifiers**: Attributes that can be combined with external data to re-identify subjects (e.g., Age, Gender, Zip Code). These are generalized.
   - **Generalization**: Replacing specific values with ranges or broader categories (e.g. exact Age to Age brackets, specific Zip Code digits to wildcards).

## Algorithm
1. **Load/Create Dataset**: Construct a pandas DataFrame containing sensitive features (Name, Email) and quasi-identifiers (Zip Code, Age).
2. **Mask Direct Identifiers**:
   - Apply a name masking function that replaces characters after the first letter with asterisks.
   - Apply an email masking function that masks the username portion while preserving the domain.
3. **Generalize Quasi-Identifiers**:
   - Truncate the ZIP codes to remove the last two digits (e.g., "12345" -> "123XX").
   - Categorize exact Ages into brackets (e.g., "20-30", "30-40").
4. **Enforce K-Anonymity**: Group the generalized dataset to verify that the partition sizes satisfy the requirement (each combination of quasi-identifiers contains at least $k$ elements).
5. **Print Results**: Output original, masked, and $k$-anonymized dataframes.

## Requirements
- Python 3.x
- Pandas (`pip install pandas`)

## How to Run
1. Run the Python script:
   ```bash
   python data_anonymization.py
   ```

## Sample Output
```
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
0  Anonymous  suppressed@example.com    123XX  20-30
1  Anonymous  suppressed@example.com    123XX  20-30
2  Anonymous  suppressed@example.com    123XX  30-40

Group Sizes for Quasi-identifiers:
Zip Code  Age  
123XX     20-30    2
          30-40    1
dtype: int64
```

## Result
Data anonymization techniques were successfully implemented in Python. Direct identifiers were masked to protect privacy, and quasi-identifiers were generalized to demonstrate the mechanism of $k$-anonymity.
