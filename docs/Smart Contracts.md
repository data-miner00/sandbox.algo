- [Documentation link](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/)

---

- Algorand Smart Contracts (ASC1) are small programs that serve various functions on the blockchain and operate on layer-1.
- It is seperated into two categories - _Smart Contracts_ and _Smart Signature_.
- They also referred to _stateful_ and _stateless_ contracts respectively.
- The type of contract written will affect how the logic of the program is evaluated.
- Both are written in [TEAL](https://developer.algorand.org/docs/get-details/dapps/avm/teal/).
- Interpreted by [AVM](https://developer.algorand.org/docs/get-details/dapps/avm).
- TEAL can be written directly or transpile from Python via PyTEAL compiler.

## Smart contracts

- Once deployed, referred to as an Application and assigned an Application Id.
- Application can **modify global state** or local state as per application + account basis.
- Able to **access on-chain values** - account balances, asset configuration parameters or the latest block time.
- Can **execute transactions** as part of execution of the logic.
- An application can call another application.
- Application have an **associated application account** that can hold Algos and ASA
- To provide a standard method for exposing an API and encoding/decoding data types from application call transactions, the [ABI](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/ABI/) should be used.

## Smart signatures

- Contains logic that used to sign transactions, primarily for signature delegation.
- The logic of smart signature is submitted with a transaction.
- While the logic in smart signature is stored on the chain as part of resolving the transaction, it is not remotely callable.
- New transaction that relies on the same smart signature would resubmit the logic.
- It will fail or success when the logic is submitted to a node that AVM evaluates.
- Smart signature's logic failure will abort the transaction.

- Can be used in two different modes

  - [contract account](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/smartsigs/modes/#contract-account)
  - [delegated signature](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/smartsigs/modes/#delegated-approval)

- The submitted transaction that is signed with smart signature only have access to a few global variables, some temporary space and properties of the transaction they submitted with.

## More details

- [Smart contract documentation](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/apps/)
- [PyTeal overview](https://developer.algorand.org/docs/get-details/dapps/pyteal/)
- [Interacting with smart contracts](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/frontend/smartsigs/)
- [Debugging](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/debugging/)
