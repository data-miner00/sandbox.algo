from algosdk import account, mnemonic


def generate_algorand_keypair():
    private_key, address = account.generate_account()

    print(f"Address     : {address}")
    print(f"Private key : {private_key}")
    print(f"Mnemonics   : {mnemonic.from_private_key(private_key)}")


generate_algorand_keypair()
