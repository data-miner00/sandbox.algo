- [Original site](https://www.algorand.com/technology)

---

## Smart Contracts and AVM

**Algorand Virtual Machine (AVM)** supports smart contracts with Turing-complete languages, larger program sizes, more state, has many new additional opcodes, and offers developers the ability to use functions, loops, and recursion.

- **AVM** runs on every node and contains a _stack engine_ that executes smart contracts and smart signatures, enabling developers to easily take advantage by writing smart contracts in either Python or _Reach (JavaScript-like language)_.

- **Smart Contracts** contain logic that can be called remotely after being deployed. The contracts are called by issuing an _"application call"_ transaction. The AVM evaluates the contract as part of resolving this transaction.

- **Smart Signatures** contain logic that is used to sign transactions, primarily for _signature delegation_. The logic of smart signature is submitted with the transaction.

- **Scalable, fast and secure** execution that is currently impossible on legacy platforms. ASC1s operate at over 1,000 TPS and are final in under 5 seconds on a platform to blockchain.

- **Reduced risk** with instant settlement through _trustless execution_.

- **Low cost to execute** with transaction fees identical to any other transactions on the Algorand blockchain at 0.001 Algos

- **Increased speed to market with comprehensive development resources** and examples of different complex custom dApp for Smart Contracts - dApp to dApps (i.e. dApps for Voting, Stablecoins, Auctions, Crowdfunding)

- **Transaction Execution Approval Language (TEAL)** can be throught as syntatic sugar for AVM bytecode.

---

- Traditional transactions that involves paperworks is slow.

- First generation blockchain used to automate these process but is unscalable, costly and slow too.

- Algorand remove these impediments to offer mainstream adoption.

- Algorand's smart contract is proven to be faster, scalable, cost effective and functionally advanced for sophisticated applications.

- The smart contracts are trustless programs that execute on-chain, where users can be confident that the program was executed without error or tampered with.

- They integrated into Algorand's Layer-1, inheriting the same powerful speed, scale, finality and security.

- PyTeal is a Python language binding for TEAL.

---

- Today's economy rely on intermediaries to provide trust and execution that leads to unnecessary delays and costs to consumers.

- Examples:

  1. Bind issuance
  2. Escrow account creation
  3. Loan payments & fee executions
  4. Limit orders
  5. Subscriptions
  6. Collateralized obligations
  7. Disbursements
  8. Programmatic fees
  9. Delegated high-security account management
  10. Interface with off-chain data providers
  11. HELOC (Home Equity Line of Credit)
  12. DEX
  13. Crowdfunding
  14. Voting

- Contracts can call another one directly. [More details](https://medium.com/algorand/hello-contract-calling-abff8fc00939)

## Algorand Standard Assets

ASA provides a standardized Layer-1 mechanism to represent any type of asset on Algorand that includes fungible, non-fungible, restricted fungible and restricted non-fungible assets.

- Challenges to digitization of assets:
  1. Access to global, digital markets
  2. 24x7 transferability
  3. Instantaneous settlement
  4. Ease and enforceablity of asset controls
  5. Efficiency of administration, such as compliance and reporting

### ASA Features

- Role Based Asset Control (RBAC) - Optional and flexible asset controls for issuers and managers for business, compliance and regulatory requirements. This includes:

  1. Quarantine asset accounts for investigative purposes
  2. Force transfer an asset where legal or other regulations require it
  3. Whitelist model for privileged asset transacting, which allows only specific addresses that have been approved to transact within a specific asset (all other will be restricted)
  4. Flexible asset reserve models for custom business requirements
  5. Off chain asset documentation included in on chain asset definition

- User Protections - Asset spam protection that prevents unknown asset that may have tax, legal, or reputational risk from being sent to users without their explicit approval (users must opt-in to accept new assets).

### Unique Functionality

- ASAs are incredibly fast and secure, as they are built directly into Algorand's Layer-1
- ASAs are low cost to execute, due to Algorand's miniscule transaction fees
- Easy and simple asset issuance for developers and enterprises
- Universal interoperability of all assets issued on Algorand

### More Exciting Use Cases

- Asset tokenization
- 3rd party asset issuance on Algorand
- Democratize access to investments
- Disintermediate cross border transactions

### Example Asset Types

| Fungible Tokens                                                                                                              | Non-fungible Tokens                                                                                                                  | Restricted Fungible Tokens                                                    | Restricted Non-fungible Tokens                                                               |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| <ul><li>In Game Points</li><li>Stable Coins</li><li>Loyalty Points</li><li>System Credits</li><li>Cryptocurrencies</li></ul> | <ul><li>InGame Items</li><li>Supply Chain</li><li>Real Estate</li><li>Identity</li><li>Certifications</li><li>Collectables</li></ul> | <ul><li>Securities</li><li>Gov't Issued Fiat</li><li>Certifications</li></ul> | <ul><li>Real Estate</li><li>Ownership Registries</li><li>Regulatory Certifications</li></ul> |

## Atomic Transfers

- Traditional economy requires a trusted legal framework but _Atomic Transfers_ provide a trustless solution in Layer-1 blockchain.
- Atomic Transfers offer a secure way to simultaneously transfer a number of assets among a number of parties.
- Specifically, many transactions are grouped together and either all transactions are executed or none of them are executed.

### Unique Functionality

- Truly atomic, no need escrow or reliance on hash time-locked contracts. This is a new way of technical execution of complex transfers that is smooth and fast.
- With Algorand's miniscule transaction fees, Atomic Transfers are incredibly low cost to execute
- Supports all Algorand assets (Algos and any Algorand Standard Asset) and allows for multi-party transfers.

### Most Exciting Use Cases

- Simplififed and expedited debt statement
- Efficient matched funding
- Decentralized exchanges, when combined with Algorand Standard Assets (ASA) and Algorand Smart Contracts (ASC1)
- Instantaneous settlement of complex multi-party / multi-asset transactions
- Any instance of a multilateral trade

## Rekeying

- Public Address and Private Spending Key
- They always comes in distinct pairs
- Public-Private key is inefficient and not always secure
- A user that has a compsomised account needs to move his asset to a newly created account and this is operationally onerous
- Each time user change his account, they need to provide his new public key to others for authentication.
- Causes interruptions on automated recurring transactions with peers or institutions.
- Algorand Rekeying allows user to change their private key without changing their public address.
- Benefits: **Flexibility**, **Continuity**, **Operational Efficiency**

### Unique Functionality

- Rekeying in unprecedented in other blockchains
- A fast and seamless way to preserve public address permanence
- An innovative way to secure existing accounts with a new Private Spending Key with low operational cost
- Ability to change security posture of an account by introducing hardware wallet, multi-sig, or smart contract-based spending key to an address where they did not exist previously.
- Flexibility to maintain a single Public Address as desired and change the Private Spending Key at any time.
- Users to create (updateable) spending policies for their Public Address to enact automated, recurring transactions as a "set it and forget it" set-up
- Operational consistency and governance & control of an account by users and custody providers

### More Exciting Use Cases

- **Novation** with the ability to reassign ownership of a contract; this is often done in a _larger settlement context_. With blockchain, ammounts can now have ownership re-assigned in a trustless manner and in the context of atomic transfers/settlement.
- **Custody Providers** (Banks, Exchanges, Savings associations, Registered broker-dealers, and Futures commission merchants) can benefit from Rekeying by:
- Keeping their user's spending keys cold at all times while only needing to manage one Public Address key
- Eliminating the chain of old Public Address keys from having to move fun after using the spending keys. Eliminate complex off-chain solutions created to maintain a single Public Address key but give more control over the Private Spending Key.
- Enabling standardized key rotation schedules depending on security posture (i.e. a company can institute a monthly key rotation if desired)
- **Onboarding large user bases** for projects that are moving to Algorand from other blockchains or more traditional technology, it can be challenging to get users set up in the new blockchain ensuring as little friction as possible is passed to them during the transition. Rekeying allows organizations to create and set-up accounts for their users ahead of time and trustlessly reassign them when needed
- **Any high-security scenario** in which the spending key must be kept cold, but a transaction is needed from the account
