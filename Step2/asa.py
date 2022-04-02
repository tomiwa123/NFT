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

from secrets import (
    ALGOD_ADDRESS,
    ALGOD_HEADERS
)


def create_ASA(client, address, private_key):
    # TODO NFTs in Algorand can be represented on-chain as assets.
    # In HW1, you used AssetConfigTxn to create an asset. Here, you will use
    # the same class, but with different arguments. Refer to
    # https://developer.algorand.org/docs/get-started/tokenization/nft/
    # on how to create an NFT using AssetConfigTxn

    # You will need to pass strict_empty_address_check=False as an argument
    # to AssetConfigTxn

    txn = AssetConfigTxn(
        sender=address,
        sp=get_default_params(client),
        total=1,
        default_frozen=False,
        unit_name="myNFT",
        asset_name=ASSET_NAME + "#arc3",
        manager="",
        reserve="",
        freeze="",
        clawback="",
        url=IPFS_METADATA_ADDRESS,
        metadata_hash=IPFS_METADATA_HASH,
        decimals=0,
        strict_empty_address_check=False
    )

    # TODO sign and send transaction, and wait_for_confirmation like in the previous homeworks
    # Feel free to use functions from utils.py
    stxn = txn.sign(private_key)
    tx_id = client.send_transaction(stxn)

    wait_for_confirmation(client, tx_id, 10)

    ptx = client.pending_transaction_info(tx_id)
    asset_id = ptx["asset-index"]

    # TODO Assign to these variables to print out the Transaction ID and Asset ID
    print("Transaction ID: {}".format(tx_id))
    print("Asset ID: {}".format(asset_id))

def main():
    # TODO create an algod client
    address_A = "D4HO6L3EQZAYBW45MTEAYDC6Y7IC3SFRP77GRNFGL2KKF5J7EMIHMIF36A"
    private_key_A = mnemonic.to_private_key(
        "figure snack acoustic riot cart include crunch later pilot arena flame major satoshi solve close village spread volume position nose guide pumpkin ill ability kit"
    )
    algod_client = algod.AlgodClient(
        algod_token="",
        algod_address=ALGOD_ADDRESS,
        headers=ALGOD_HEADERS
    )
    # TODO call create_ASA with the correct arguments
    create_ASA(algod_client, address_A, private_key_A)
    pass

if __name__ == '__main__':
    main()
