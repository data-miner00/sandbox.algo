- [Link](https://developer.algorand.org/docs/archive/build-apps/setup/)

---

- Algod is the main process for handling the blockchain. It uses data directory on Algorand nodes for storing data and for information regarding the node's configuration
- Indexer is used to search for on-chain data like transactions, accounts, assets and blocks on Algorand
- KMD (Key management daemon) manages account wallets and keys on the Algorand blockchain

---

- An application connects to the Algorand blockchin through an **algod** client.
- The algod client requires a valid **algod REST endpoint IP address** and **algod token** from an Algorand node

## Command Line Interface (CLI) Tools

- Command line utilities packaged with Algorand node software:

  - goal
  - kmd
  - algokey

- goal is primary tool to operate a node and it contains functionality to manage keys, sign and send transactions, create assets etc.
- It is recommended to have some fluency in goal as a complementary tool during testing and validation.
- goal is required to setup more advanced testing environments using private networks.

- kmd is tool for Algorand Key Management daemon
- algokey is standalone utility for generating Algorand accounts and for signing transactions.
- REST endpoints for algod and kmd available

## Indexer

- Algorand provides a standalone daemon [algorand_indexer](https://developer.algorand.org/docs/get-details/indexer/) that reads committed blocks from the Algorand blockchain and maintains a local database of transactions and accounts that are searchable and indexed.
- [REST API](https://developer.algorand.org/docs/rest-apis/indexer) available application developers to perform rich and efficient queries on accounts, transactions, assets etc.

## Choosing a network

- [MainNet](https://developer.algorand.org/docs/get-details/algorand-networks/mainnet)
- [TestNet](https://developer.algorand.org/docs/get-details/algorand-networks/testnet) Resembles MainNet but with fake assets
- [BetaNet](https://developer.algorand.org/docs/get-details/algorand-networks/betanet) New protocol-level features released for initial testing, quality and features not guarenteed, network restarts are common.

## How do I obtain an algod address and token?

- Use a third-party service
- Use Docker Sandbox
- Run your own node
