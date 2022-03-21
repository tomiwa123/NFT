from algosdk.v2client import algod
from algosdk.future import transaction
from algosdk.future.transaction import AssetConfigTxn
from utils import wait_for_confirmation, get_default_params
from secrets import (
    ALGOD_ADDRESS,
    ALGOD_HEADERS,
    account_private_key,
    account_address,
)
from pinata import save_art_to_ipfs


def create_nft(client, address, private_key, nft_info):
    # TODO call save_art_to_ipfs, which is defined at `pinata.py`, with the
    # correct arguments
    ipfs_cid, ipfs_address, ipfs_metadata = save_art_to_ipfs('', '', '')
    print("NFT CID: {}".format(ipfs_cid))

    params = get_default_params(client)

    # TODO NFTs in Algorand can be represented on-chain as assets.
    # In HW1, you used AssetConfigTxn to create an asset. Here, you will use
    # the same class, but with different arguments. Refer to
    # https://developer.algorand.org/docs/get-started/tokenization/nft/
    # on how to create an NFT using AssetConfigTxn

    # TODO you will need to pass strict_empty_address_check=False as an argument
    # to AssetConfigTxn

    # TODO what should the values of `url` and `metadata_hash` be?
    # txn = AssetConfigTxn(strict_empty_address_check=False)

    # TODO sign and send transaction, and wait_for_confirmation


    print("Transaction ID: {}".format(tx_id))
    print("Asset ID: {}".format(asset_id))


def get_nft_info():
    # TODO: fill out the following values
    # - file-name should be the name of the file you created with its extension; for example: cis233.png
    # - unit-name is the Unit Name that will show up in Algorand; for example: PHIL-SUN
    # - asset-name the name of the asset/NFT that will show up in Algorand; for example: "Philadelphia's sunrise"
    # - asset-description any description you want to give to your NFT
    return {
        'file-name': "",
        'unit-name': "",
        'asset-name': "",
        'asset-description': "",
    }


def main():
    # TODO create an algod client
    # TODO call create_nft with the correct arguments
    pass


if __name__ == '__main__':
    main()
