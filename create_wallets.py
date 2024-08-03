from eth_account import Account
import json
import os
import sys

# Function to create wallets
def create_wallets(num_wallets):
    # Create a directory to store the wallet information
    wallets_dir = 'wallets'
    os.makedirs(wallets_dir, exist_ok=True)

    # List to store wallet information
    wallet_list = []

    for i in range(num_wallets):
        # Create a new Ethereum account
        account = Account.create()

        # Get the private key and address
        private_key = account.key.hex()
        address = account.address

        # Store wallet information in a dictionary
        wallet_info = {
            'address': address,
            'private_key': private_key
        }

        # Save wallet information to a file
        with open(f'{wallets_dir}/wallet_{i}.json', 'w') as f:
            json.dump(wallet_info, f)

        # Append wallet information to the list
        wallet_list.append(wallet_info)

    print(f'Successfully created {num_wallets} MetaMask wallets.')

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python create_wallets.py <number_of_wallets>")
        sys.exit(1)

    try:
        num_wallets = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid number of wallets.")
        sys.exit(1)

    create_wallets(num_wallets)

if __name__ == '__main__':
    main()
