from algosdk import mnemonic

# TODO
PINATA_API_KEY = "your-key-here"
PINATA_API_SECRET = "your-secret-here"

# TODO
PURESTAKE_API_KEY = "your-purestake-key-here"

account_mnemonic = "mnemonic here" # TODO
account_private_key = mnemonic.to_private_key(account_mnemonic)
account_address = mnemonic.to_public_key(account_mnemonic)

ALGOD_ADDRESS = "https://testnet-algorand.api.purestake.io/ps2"
ALGOD_HEADERS = {"X-API-Key": PURESTAKE_API_KEY}
