from django.http import HttpResponse
import requests

# TODO USE THIS package
# from algosdk.v2client import algod

# TODO Feel free to copy-paste the secrets.py file into this folder and import it here


def serve_image(request):
    # TODO modify this function to:
    # 1. Query the algorand blockchain for your NFT
    # 2. Recover the IPFS link from the NFT
    # 3. Query the image from IPFS
    # 4. Serve the image as an HTTP response

    image_bytes = open("./beautiful_temple.jpeg", "rb")
    return HttpResponse(image_bytes.read(), content_type="image/jpeg")

def home_page(request):
    return HttpResponse("<h1>Visit localhost:8000/nft to view your NFT!</h1>")