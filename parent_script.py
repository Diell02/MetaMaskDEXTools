import subprocess

# Total number of wallets
total_wallets = 500  # Adjust based on the number of wallets you have

# Path to the child script
child_script_path = './child_script.py'

# Iterate through wallets and run the child script
for wallet_index in range(total_wallets):
    print(f"Processing wallet {wallet_index}...")
    subprocess.run(['python', child_script_path, str(wallet_index)])
    print(f"Completed processing wallet {wallet_index}.")
