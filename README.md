# Practical-HW3
Aight, let's make some NFTs

This homework has 4 components: 
1. Choose your art piece and store it on IPFS
2. Make your art piece an NFT Asset by putting in on the Algorand blockchain
3. Create a local web server that queries the blockchain for your NFT and displays the image
4. Airdrop your NFT to our TA account 

Sidenote: We’ll display all NFTs airdropped to the TA account on a webpage to see all of your glorious artistic inclinations. We’ll have the students in the class vote on the 3 best NFTs. Tal will purchase the top 3 NFTs for 100, 60, and 40 Algos respectively. 

## Step 1: Create your NFT
In this step, you will find an art, upload it to IPFS, and create an NFT on Algorand linking to IPFS.

### What is IPFS?
IPFS defines itself as "a distributed system for storing and accessing files, websites, applications, and data".
In IPFS, files are found through a unique identifier, called CID, instead of *where* they are located. For example, in Web2, if we want to find a `.png` file, we would need to specify at which website it is, for example: `https://site.com/file.png`. In IPFS, if we want to file a `.png` file, we would specify its CID, for example: `ipfs://cid`.

In order to create the CID, IPFS splits the file into blocks and hashes each block. Then, it creates a Merkle Tree where the blocks are the leafs of the tree. The root of the Merkle Tree is the CID of the file.

To know more about IPFS, take a look at the following resources:
- [https://docs.ipfs.io/concepts/what-is-ipfs/](https://docs.ipfs.io/concepts/what-is-ipfs/)
- [https://proto.school/content-addressing](https://proto.school/content-addressing)
- [https://proto.school/anatomy-of-a-cid](https://proto.school/anatomy-of-a-cid)
- [https://proto.school/merkle-dags](https://proto.school/merkle-dags)


### TODO: talk about ARC3? https://developer.algorand.org/solutions/minting-nfts-on-algorand-using-ipfs/

### Step 1.1: Create your Art Piece
Create a `jpeg` or `png` file with any art :) put that file inside the `src/art/` folder. The file can have any name.

### Step 1.2: Create a Pinata account
In order to upload your art to IPFS, you will use [Pinata](https://www.pinata.cloud/). 

Note: We are using Pinata because, otherwise, you would need to run your own IPFS node and keep it running in order for other people to retrieve it. With Pinata, this is all handled for us and we only need to call some functions.

To create your account, go to [https://www.pinata.cloud/](https://www.pinata.cloud/) and click on `Try for Free` at the top right corner.

After creating your account, you will be redirected to another page where you will be logged in. At the top right corner, there is a small dropdown button right next to the avatar image. Click on it, and then click on `API Keys` (or you can just access [https://app.pinata.cloud/keys](https://app.pinata.cloud/keys)). There, click on `+ New Key`. Active the slider right next to `Admin`, give your key any name you want, and click on `Create key`.

Right after that, a modal will show your API Key, and API secret. Save them at `src/secrets.py`.

### Step 1.3: Purestake API key
Put the Purestake API key you created for the previous assignments in `src/secrets.py`.

### Step 1.4: Algorand account
Create (or use a previously created) Algorand account. Put its mnemonic at `src/secrets.py`. If you created a new account, do not forget to fund it at [https://bank.testnet.algorand.network/](https://bank.testnet.algorand.network/).

### Step 1.5: install new packages
There are some new packages you need to add. In your terminal, run:
```
pip3 install requests
pip3 install base58
```

## Step 2: Linking your NFT to Algorand

Now that you've created your art piece and stored it on IPFS, let's get it onto the Algorand blockchain. Remember creating an Algorand Standard Asset (ASA) in HW1? Well, Algorand makes it super easy for you to create an NFT through that. On Algorand, you can think of NFTs as just another type of asset—the only clause being that there’s only 1 unit of this asset—where you link the metadata (so that the users can verify authenticity). 

### Step 2.1: Create NFT ASA
In Practical HW 1, you created an asset using `AssetConfigTxn`. In this homework, you will do the same, but with some modifications.

- [ ] Fill out the `nft_info` function
- [ ] Fill out the `create_nft` function
- [ ] inside `main`, create an Algorand client like you did in the previous homeworks and call the `create_nft` function with the correct arguments.

If everything went right, a `NFT CID` will be printed on your screen. Make sure to keep this CID as you will need it in the next step.

You might find the following resource useful for this step: (https://developer.algorand.org/docs/get-started/tokenization/nft/

### Step 2.2: Submit the generated `nft.json` file
After running the `nft.py` file, a `nft.json` file is created. Save this file because you will need to submit it on Gradescope :)


## Step 3 - Create local web server to view NFT

The next step is to learn how to query the NFT that you’ve minted to your own server for display.

We provide a basic web server to get you started, which can be found in the Step 3 folder. This folder provides the scaffolding of a Django server; Django is a web framework for python that lets you quickly spin up servers.

First, install django onto your system by running 
```
pip3 install django
```
Next, we will launch the server. Navigate to the Step 3 folder and run
```
python3 manage.py runserver
```
If you get an error message saying that you have missing packages, go ahead and pip install them as well.

Now, if you open your browser and go to `localhost:8000/nft`

You should see a picture of a gorgeous buddhist temple!
The handler associated with the path `localhost:8000/nft` can be found in the views.py folder. You can see that the function is currently returning a local image as an HttpResponse. Your job is the following. Modify the handler to:

1. Query the algorand blockchain for your NFT
2. Recover the IPFS link from the NFT
3. Query the image from IPFS
4. Serve the image as an HTTP response

You will need an algod client to query the blockchain for the NFT data. See the following docs: https://py-algorand-sdk.readthedocs.io/en/v1.2.1_a/algod.html

You will also need to use Pinata again, but this time to retrieve the image instead of uploading it. See the following link for retrieving content IPFS through Pinata: https://docs.pinata.cloud/retrieving-content

If you do everything correctly, the endpoint `localhost:8000/nft` should serve your NFT from IPFS!

Keep your views.py file for submission on gradescope.
