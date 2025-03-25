# OTP Generator and Validator

## Description
This project is a console-based OTP (One-Time Password) generator and validator written in Python. It sends a randomly generated OTP via email and verifies it through user input.

## Features
- Generates a secure 4-digit OTP.
- Sends OTP to multiple email addresses.
- Validates the OTP entered by the user.

## Prerequisites
Before running this script, ensure you have:
- Python installed.
- The required libraries installed using:
  ```sh
  pip install smtplib email
  ```
- Enabled **Less Secure Apps** in your Gmail settings.

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/otp-generator.git
   ```
2. Navigate to the project directory:
   ```sh
   cd otp-generator
   ```
3. Run the script:
   ```sh
   python otp_generator.py
   ```

## Usage
- Enter the number of email recipients.
- Provide email addresses to receive OTPs.
- The script generates and sends an OTP.
- Enter the received OTP for validation.

## Security Considerations
- **Do not hardcode email credentials** in the script. Use environment variables instead.
- SMTP authentication is not recommended for production; use OAuth 2.0 for enhanced security.

## License
This project is licensed under the MIT License.

