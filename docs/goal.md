## What is GOAL

- GOAL is the CLI tool provided by Algorand to interact with it's software instance.
- GOAL comes together with every Algorand sandbox and node installation.
- For more info, can check out [Algorand GOAL docs](https://developer.algorand.org/docs/clis/goal/goal/) or run `goal --help`.
- For goal commands within the Algorand sandbox, it is required to prefix each command with `./sandbox`, such that the help command will looks like `./sandbox goal --help`.

### Create a wallet in Algorand Sandbox

To create an NFT with goal CLI tool, it is required to create a new wallet in the Algorand Sandbox. The wallet is used to store Algorand accounts. To check the existing wallets created within the Algorand sandbox,

```
./sandbox goal wallet list
```

There should be no preconfigured wallets when the command is first executed within the sandbox.

```
No wallets found. You can create a wallet with `goal wallet new`
```

As such, we will need to create the wallet with the following command,

```
./sandbox goal wallet new <your-wallet-name>
```

A password is required upon the creation of the wallet. Run the `wallet list` command again and a new wallet should appear in the result.

### Troubleshooting

If the following error is observed while creating a wallet,

```
Please choose a password for wallet 'shaun-wallet': Couldn't read password: inappropriate ioctl for device
```

Use

```
./sandbox enter algod
```

Then there must be an observable change towards the prompt of the terminal as such.

```
Entering /bin/bash session in the algod container...
root@27103d2b89ab:~/testnetwork/Node#
```

The wallet may now be created with the same command, but without the `./sandbox` prefix.

```
goal wallet new <your-wallet-name>
```

The wallet now should be created with the following output.

```
Please choose a password for wallet 'shaun-wallet':
Please confirm the password:
Creating wallet...
Created wallet 'shaun-wallet'
Your new wallet has a backup phrase that can be used for recovery.
Keeping this backup phrase safe is extremely important.
Would you like to see it now? (Y/n):  y
Your backup phrase is printed below.
Keep this information safe -- never share it with anyone!

<your> <25> <word> <phrase> ... <here>
```

Note down the mnemonic phrases in somewhere safe.

### Creating a new account

To create a new account, run

```
./sandbox goal account new
```

To export the the account credentials,

```
./sandbox goal account export -a <your-address>
```
