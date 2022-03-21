# Practical-HW3
Practical HW3 for CIS 233

This homework has 4 components: 
1. Choose your art piece and store it on IPFS.
2. Create an NFT Asset on the Algorand blockchain and link it to the art piece on IPFS
3. Create a local web server that queries the blockchain for your NFT and displays the image
4. Airdrop your NFT to our TA account (and then we’ll display it on a webpage to see all of your artistic glory)

Sidenote: We’ll have the students in the class vote on the 3 best NFTs. Tal will purchase the top 3 NFTs for 100, 60, and 40 Algos respectively. 


## Step 1: creating your NFT
In this step, you will find an art, upload it to IPFS, and create an NFT on Algorand linking to IPFS.

### What is IPFS?
From their documentation, IPFS defines itself as "a distributed system for storing and accessing files, websites, applications, and data".
In IPFS, files are found through a unique identifier, called CID, instead of *where* they are located. For example, in the conventional web, if we want to find a `.png` file, we would need to specify at which website it is, for example: `https://site.com/file.png`. In IPFS, if we want to file a `.png` file, we would specify its CID, for example: `ipfs://cid`.

In order to create the CID, IPFS splits the file into blocks and hashes each block. Then, it creates a Merkle Tree where the blocks are the leafs of the tree. The root of the Merkle Tree is the CID of the file.

To know more about IPFS, take a look at he following resources:
- [https://docs.ipfs.io/concepts/what-is-ipfs/](https://docs.ipfs.io/concepts/what-is-ipfs/)
- [https://proto.school/content-addressing](https://proto.school/content-addressing)
- [https://proto.school/anatomy-of-a-cid](https://proto.school/anatomy-of-a-cid)
- [https://proto.school/merkle-dags](https://proto.school/merkle-dags)


## TODO: talk about ARC3? https://developer.algorand.org/solutions/minting-nfts-on-algorand-using-ipfs/

### Step 1.1: creating an art
Create a `jpeg` or `png` file with any art :) put that file inside the `src/art/` folder. The file can have any name.

### Step 1.2: creating a Pinata account
In order to upload your art to IPFS, you will use [Pinata](https://www.pinata.cloud/). We are going to use it because, otherwise, you would need to run your own IPFS node and keep it running in order for other people to retrieve it. With Pinata, this is all handled for us and we onlyn need to call some functions.

To create your account, go to [https://www.pinata.cloud/](https://www.pinata.cloud/) and click on `Try for Free` at the top right corner.

After creating your account, you will be redirect to another page where you will be logged in. At the top right corder, there is a small dropdown button right next to the avatar image. Click on it, and then click on `API Keys` (or you can just access [https://app.pinata.cloud/keys](https://app.pinata.cloud/keys)). There, click on `+ New Key`. Active the slider right next to `Admin`, give your key any name you want, and click on `Create key`.

Right after that, a modal will show your API Key, and API secret. Save them at `src/secrets.py`.

### Step 1.3: Purestake API key
Put the Purestake API key you created for the previous assignments at `src/secrets.py`.

### Step 1.4: Algorand account
Create (or use a previously created) Algorand account. Put its mnemonic at `src/secrets.py`. If you created a new account, do not forget to fund it at [https://bank.testnet.algorand.network/](https://bank.testnet.algorand.network/).

### Step 1.5: install new packages
There are some new packages you need to add. In your terminal, run:
```
pip3 install requests
pip3 install base58
```

### Step 1.6: creating the NFT
In Practical HW 1, you created an asset using `AssetConfigTxn`. In this homework, you will do the same, but with some modifications.

- [ ] Fill out the `nft_info` function
- [ ] Fill out the `create_nft` function
- [ ] inside `main`, create an Algorand client like you did in the previous homeworks and call the `create_nft` function with the correct arguments.

If everything went right, a `NFT CID` will be printed on your screen. If you want to see your art, copy that CID and go to `https://gateway.pinata.cloud/ipfs/cid`, where `cid` should be the CID you just copied.

### Step 1.7: submit the generated `nft.json` file
After running the `nft.py` file, a `nft.json` file is created. Save this file because you will need to submit it on Gradescope :)
