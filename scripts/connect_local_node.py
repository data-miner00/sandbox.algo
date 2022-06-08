import os
from algosdk.v2client import algod


algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_client = algod.AlgodClient(algod_token, algod_address)

my_address = os.getenv("ALGORAND_WALLET_PUBLIC_ADDRESS")

account_info = algod_client.account_info(my_address)
print(account_info)
