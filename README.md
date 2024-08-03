# Ethereum Wallet and DEXTools Automation

These scripts are designed for creating Ethereum wallets, importing them into MetaMask, connecting to DEXTools, and automating voting processes.

## Scripts Overview

- **create_wallets.py**: This script creates Ethereum wallets.
- **child_script.py**: This script imports a wallet into MetaMask, redirects to DEXTools, connects the wallet, signs it, allows you to vote thumbs up on a token, disconnects from DEXTools, and repeats the process with the next wallet.
- **parent_script.py**: This script decides how many times the child_script should be executed and instructs the child_script to iterate to the next wallet.

## Disclaimer

This project is for educational purposes only. The voting part of the script is intentionally incomplete to prevent use for bot automation, which is against the guidelines of the websites.

## Technologies Used

- **Python**
- **Selenium**

## Browser Compatibility

This project is designed to work with **Mozilla Firefox**. Ensure that you have Firefox installed and properly configured, as the scripts use Firefox for interacting with MetaMask and DEXTools.

## Steps to Run the Scripts

1. **Create a Virtual Environment**:
    - Open a terminal and navigate to the directory where your project is located.
    - Create a virtual environment:
      ```sh
      python -m venv venv
      ```

2. **Activate the Virtual Environment**:
    - On Windows:
      ```sh
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```sh
      source venv/bin/activate
      ```

3. **Install the Required Packages**:
    - With the virtual environment activated, install the packages listed in `requirements.txt`:
      ```sh
      pip install -r requirements.txt
      ```

## Usage Instructions

- **create_wallets.py**: Run this script first to create the wallets.
- **parent_script.py**: Executes the child script. Specify the number of times you want to run the child script.
- **child_script.py**:
  - Replace the URL of the crypto you want to vote on in line 158.
  - Replace the profile path in line 18. You can find the `profile_path` by going to Firefox and typing `about:profiles` in the address bar. Copy the root directory of the `default-release` profile and set it as the `profile_path`, making sure to replace backslashes (`\`) with forward slashes (`/`).
  - Replace the MetaMask extension ID in line 68. You can find the MetaMask extension ID by unlocking your wallet, clicking the three dots in the top right, and expanding the view. The URL will contain the extension ID.

### MetaMask Setup

Before running the parent/child scripts, create an account in MetaMask. Do not leave it without an account. Set the password to `Test1234!`. If you want to use another password, go to `child_script.py` and replace it in line 182.
