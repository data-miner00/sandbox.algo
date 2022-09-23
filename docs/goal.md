## What is GOAL

GOAL is the CLI tool provided by Algorand to interact with it's software instance.

GOAL comes together with every Algorand sandbox and node installation.

For more info, can check out [Algorand GOAL docs](https://developer.algorand.org/docs/clis/goal/goal/) or run `goal --help`. For goal commands within the Algorand sandbox, it is required to prefix each command with `./sandbox`, such that the help command will looks like `./sandbox goal --help`.

### Create a wallet in Algorand Sandbox

To create an NFT with goal CLI tool, it is required to create a new wallet in the Algorand Sandbox. The wallet is used to store Algorand accounts.

To check the existing wallets created within the Algorand sandbox,

```
./sandbox goal wallet list
```

There should be no preconfigured wallets when the command is first executed within the sandbox. As such, we will need to create the wallet with the following command,

```
./sandbox goal wallet new <your-wallet-name>
```

A password is required upon the creation of the wallet. Run the `wallet list` command again and a new wallet should appear in the result.
