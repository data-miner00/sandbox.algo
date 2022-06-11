import os
from algosdk.v2client import algod

algod_address = 'https://testnet-algorand.api.purestake.io/idx2'
algod_token = os.getenv('PURESTAKE_API_KEY')
headers = {
   "X-API-Key": algod_token,
}
algod_client = algod.AlgodClient(algod_token, algod_address, headers)

my_address = os.getenv("ALGORAND_ACCOUNT_FIRST_ADDRESS")

account_info = algod_client.account_info(my_address)
print(account_info)
