import json
import base64
import os
from algosdk.future import transaction
from algosdk import mnemonic
from algosdk.v2client import algod


algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_client = algod.AlgodClient(algod_token, algod_address)

my_address = os.getenv("ALGORAND_ACCOUNT_FIRST_ADDRESS")
my_mnemonic = os.getenv("ALGORAND_ACCOUNT_FIRST_MNEMONIC")

private_key = mnemonic.to_private_key(my_mnemonic)


def _transaction(private_key: str, sender_address: str):
    params = algod_client.suggested_params()

    receiver_address = os.getenv("ALGORAND_ACCOUNT_SECOND_ADDRESS")
    note = "Hello and you are welcome".encode()
    amount = 1000000
    unsigned_txn = transaction.PaymentTxn(sender_address, params, receiver_address, amount, None, note)
    signed_txn = unsigned_txn.sign(private_key)

    txid = algod_client.send_transaction(signed_txn)
    print(f"Successfully send ALGO with txID: {txid}")

    try:
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)
    except Exception as err:
        print(err)
        return

    account_info = algod_client.account_info(sender_address)
    print("Transaction information: {}".format(json.dumps(confirmed_txn, indent=4)))
    print("Decoded note: {}".format(base64.b64decode(confirmed_txn["txn"]["txn"]["note"]).decode()))
    print("Account information: {}".format(json.dumps(account_info, indent=4)))


_transaction(private_key, my_address)
