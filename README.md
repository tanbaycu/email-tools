# Email Generator Tool

## Introduction

The Email Generator Tool is a utility designed to generate random email addresses and passwords. This tool allows you to:
- Create emails based on a template with random parts.
- Generate strong passwords with customizable length and character types.
- Save the list of emails and passwords in various file formats (txt, csv, json, md).

## Key Features

- **Generate Emails**: Create email addresses with customizable formats.
- **Generate Passwords**: Create strong passwords with customizable character options.
- **Save to File**: Save results in different file formats such as txt, csv, json, md.
- **User Interface**: Uses the `rich` library to provide an attractive and user-friendly interface.

## Installation

1. **Install Python**: Ensure you have Python 3.6 or higher installed.

2. **Install Required Libraries**:
    ```bash
    pip install rich
    ```

## Usage

1. **Run the Program**:
    ```bash
    python emailtool.py
    ```

2. **Input Information**:
    - Email Template: Enter the email template you want to create.
    - Domain: Enter the domain for the email.
    - Random Part Length: Enter the length of the random part in the email.
    - Random Character Type: Choose the type of characters for the random part.
    - Format: Choose the format for the email.
    - Number of Emails: Enter the number of emails to generate.
    - Exclude Characters: Enter any characters to exclude from passwords.
    - Password Length: Enter the length of the passwords.
    - Save Results: Confirm if you want to save the results to a file.
    - File Format: Choose the file format to save the results.
    - Filename: Enter the filename to save the results.

## Example

- Enter the email template (e.g., user1234@gmail.com): user{random}@example.com
- Enter the domain (e.g., @gmail.com, @yahoo.com) [default: @example.com]: @example.com
- Enter the length of the random part (e.g., 4 for 4 digits): 4
- Enter the type of random characters (digits, letters, alphanumeric) [default: alphanumeric]: alphanumeric
- Enter the format type (simple, custom) [default: simple]: custom
- Enter the number of emails to generate: 5
- Enter additional characters to exclude from passwords (leave empty for defaults): 
- Enter the length of the passwords: 12
- Do you want to save the emails and passwords to a file? (yes/no): yes
- Enter the file format (txt, csv, json, md) [default: txt]: txt
- Enter the filename (e.g., emails.txt): example.txt

## Contact

- **Author**: [T7C]
- **Email**: [tranminhtan4953@gmail.com]
- **Telegram**: [t.me/tanbaycu]

## Troubleshooting

If you encounter issues, please check the input parameters and ensure all required libraries are installed. For persistent problems, contact the author via email for support.

## Notes

This is a draft version and is currently under improvement.
