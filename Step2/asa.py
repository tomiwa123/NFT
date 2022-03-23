from algosdk.v2client import algod
from algosdk.future import transaction
from algosdk.future.transaction import PaymentTxn, AssetConfigTxn, AssetTransferTxn, LogicSigTransaction
from algosdk import mnemonic, encoding
from utils import wait_for_confirmation, get_default_params

from ipfs_info import (
    ASSET_NAME,
    IPFS_METADATA_ADDRESS,
    IPFS_METADATA_HASH
)


def create_ASA(client, address, private_key):
    # TODO NFTs in Algorand can be represented on-chain as assets.
    # In HW1, you used AssetConfigTxn to create an asset. Here, you will use
    # the same class, but with different arguments. Refer to
    # https://developer.algorand.org/docs/get-started/tokenization/nft/
    # on how to create an NFT using AssetConfigTxn

    # You will need to pass strict_empty_address_check=False as an argument
    # to AssetConfigTxn

    # TODO sign and send transaction, and wait_for_confirmation like in the previous homeworks
    # Feel free to use functions from utils.py

    # TODO Assign to these variables to print out the Transaction ID and Asset ID
    print("Transaction ID: {}".format(tx_id))
    print("Asset ID: {}".format(asset_id))

def main():
    # TODO create an algod client
    # TODO call create_ASA with the correct arguments
    pass

if __name__ == '__main__':
    main()
