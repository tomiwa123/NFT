# Doc: https://docs.pinata.cloud/api-pinning/pin-file
import os
import requests
import json
import hashlib
import base64
import mimetypes
from ipfs2bytes32 import ipfscidv0_to_byte32

from secrets import (
    PINATA_API_KEY, 
    PINATA_API_SECRET
)
from art.art_info import (
    FILE_NAME,
    ASSET_NAME,
    ASSET_DESCRIPTION
)


PINATA_IMAGE_URL = "https://api.pinata.cloud/pinning/pinFileToIPFS"
PINATA_JSON_URL = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
PINATA_HEADERS = {
    "pinata_api_key": PINATA_API_KEY,
    "pinata_secret_api_key": PINATA_API_SECRET,
}

def pin_image_to_ipfs(file_path):
    # TODO read the file in binary format
    f = open(file_path, 'rb')

    # TODO replace None with file data
    files = {
        'file': f.read(),
    }

    # TODO make POST request to the correct URL, with files=files, and using the PINATA_HEADERS
    response = requests.post(url=PINATA_IMAGE_URL, headers=PINATA_HEADERS, files=files)

    data = response.json()
    # TODO examine response extract out the IpfsHash (this is the CID). Return it
    # print(r.content)
    return json.loads(response.content.decode("utf-8")).get("IpfsHash")


def pin_metadata_to_ipfs(metadata):
    # TODO make POST request to the correct URL, with json=metadata, and using the PINATA_HEADERS
    response = requests.post(url=PINATA_JSON_URL, headers=PINATA_HEADERS, data=metadata)
    # TODO examine response extract out the IpfsHash (this is the CID). Return it
    return json.loads(response.content.decode("utf-8")).get("IpfsHash")
    pass


def compute_integrity(ipfs_image_cid):
    integrity = ipfscidv0_to_byte32(ipfs_image_cid)
    integrity = base64.b64encode(bytes.fromhex(integrity))
    integrity = "sha256-{}".format(integrity.decode('utf-8'))
    return integrity


def compute_metadata_hash(metadata):
    metadata_json_string = json.dumps(metadata)

    hash = hashlib.sha256()
    hash.update(metadata_json_string.encode("utf-8"))
    ipfs_metadata_hash = hash.digest()
    return ipfs_metadata_hash


def main():
    # TODO compute absolute path to FILE_NAME and use it to pin image to IPFS
    file_path = os.path.abspath(FILE_NAME)
    ipfs_cid = pin_image_to_ipfs(file_path)
    # TODO convert the IPFS CID it returns to an IPFS address
    ipfs_address = "ipfs://" + ipfs_cid
    # TODO compute the integrity
    integrity = compute_integrity(ipfs_cid)
    # TODO compute the mimetype
    mime_type = mimetypes.guess_type(file_path)


    metadata = {
        'name': ASSET_NAME,
        'description': ASSET_DESCRIPTION,
        'image': ipfs_address,
        'image_integrity': integrity,
        'image_mimetype': mime_type,
    }

    # TODO pin metadata to IPFS
    ipfs_metadata_cid = pin_metadata_to_ipfs(metadata)

    # TODO convert the IPFS CID it returns to an IPFS address
    ipfs_metadata_address = "ipfs://" + ipfs_metadata_cid

    # TODO compute metadata hash
    response = requests.get(url="https://gateway.pinata.cloud/ipfs/" + ipfs_metadata_cid, headers=PINATA_HEADERS)
    # ipfs_metadata_hash = json.loads(response.content.decode("utf-8"))
    ipfs_metadata_hash = compute_metadata_hash(json.loads(response.content.decode("utf-8")))

    # TODO assign to these variables to print them out
    print("IPFS metadata CID: {}".format(ipfs_metadata_cid))
    print("IPFS metadata address: {}".format(ipfs_metadata_address))
    print("IPFS metadata hash: {}".format(ipfs_metadata_hash))

if __name__ == '__main__':
    main()
