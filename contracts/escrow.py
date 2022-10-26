import os
import base64

from algosdk.future import transaction
from algosdk import mnemonic
from algosdk.v2client import algod
from pyteal import *


first_account_mnemonic = os.getenv('ALGORAND_ACCOUNT_FIRST_MNEMONIC')
second_account_mnemonic = os.getenv('ALGORAND_ACCOUNT_SECOND_MNEMONIC')

if first_account_mnemonic == None\
    or first_account_mnemonic == ""\
    or second_account_mnemonic == None\
    or second_account_mnemonic == "":
    raise ValueError("Mnemonics cannot be empty.")

algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def compile_smart_signature(client: algod.AlgodClient, source_code: str):
    response = client.compile(source_code)
    return response['result'], response['hash']


def donation_escrow(benefactor_address: str):
    FEES = Int(1000)

    # Only the benefactor can withdraw from this contract account
    program = And(
        Txn.type_enum() == TxnType.Payment,
        Txn.fee() <= FEES,
        Txn.receiver() == Addr(benefactor_address),

        # Make sure transaction not submitted with other txs in group
        Global.group_size() == Int(1),

        # Make sure the contract is not rekeyed to other address
        Txn.rekey_to() == Global.zero_address()
    )

    return compileTeal(program, Mode.Signature, version=5)


def payment_transaction(sender_mnemonic: str, amount: int, receiver_address: str, client: algod.AlgodClient):
    params = client.suggested_params()
    sender_address = mnemonic.to_public_key(sender_mnemonic)
    sender_key = mnemonic.to_private_key(sender_mnemonic)

    unsigned_txn = transaction.PaymentTxn(sender_address, params, receiver_address, amount)
    signed_txn = unsigned_txn.sign(sender_key)
    txid = client.send_transaction(signed_txn)
    print("Transaction ID: ", txid)
    return transaction.wait_for_confirmation(client, txid, 5)


def lsig_payment_txn(escrow_program, escrow_address: str, amount: int, receiver_address: str, client: algod.AlgodClient):
    params = client.suggested_params()
    unsigned_txn = transaction.PaymentTxn(escrow_address, params, receiver_address, amount)
    encoded_program = escrow_program.encode()
    program = base64.decodebytes(encoded_program)
    lsig = transaction.LogicSig(program)
    signed_txn = transaction.LogicSigTransaction(unsigned_txn, lsig)
    txid = client.send_transaction(signed_txn)
    print("Transaction ID: ", txid)
    return transaction.wait_for_confirmation(client, txid, 10)


if __name__ == "__main__":
    algod_client = algod.AlgodClient(algod_token=algod_token, algod_address=algod_address)
    second_account_public_key = mnemonic.to_public_key(second_account_mnemonic)
    stateless_program_teal = donation_escrow(second_account_public_key)

    escrow_result, escrow_address = compile_smart_signature(algod_client, stateless_program_teal)

    print("Program: ", escrow_result)
    print("Address: ", escrow_address)

    # Send 4 Algos + 1000 microAlgos as fees
    deposit_amount = 4001000
    payment_transaction(first_account_mnemonic, deposit_amount, escrow_address, algod_client)

    # Withdraw 2 Algos from smart signature.
    withdrawal_amount = 2000000
    lsig_payment_txn(escrow_result, escrow_address, withdrawal_amount, second_account_public_key, algod_client)
