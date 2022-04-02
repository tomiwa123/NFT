from algosdk import mnemonic

# TODO
PINATA_API_KEY = "da9967b697499189df23"
PINATA_API_SECRET = "e570fd7839f95dbe3de4b691e27f39ccc537408b38a9e39089044b9f78b37f67"

# TODO
PURESTAKE_API_KEY = "gZ1Hq4tmGS9QY8j5DOdhV4RfJQBkbaEc7yOkpC1N"

# TODO
account_mnemonic = "figure snack acoustic riot cart include crunch later pilot arena flame major satoshi solve close village spread volume position nose guide pumpkin ill ability kit"
account_private_key = mnemonic.to_private_key(account_mnemonic)
account_address = mnemonic.to_public_key(account_mnemonic)

ALGOD_ADDRESS = "https://testnet-algorand.api.purestake.io/ps2"
ALGOD_HEADERS = {"X-API-Key": PURESTAKE_API_KEY}
