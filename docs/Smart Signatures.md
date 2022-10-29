- [Link](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/smartsigs/modes/)

---

## Modes of use

- Two basic usage
  - contract account
  - delegated signature
- Used to approve transactions in different way.
- Both modes use Logic Signatures.

### Logic signatures

- Referenced as LogicSig, are structures that contains 4 parts

  - Logic: Raw Program Bytes (required)
  - Sig: Signature of Program Bytes (optional)
  - Msig: Multi-Signature of Program Bytes (optional)
  - Args: Array of Bytes Strings Passed to the Program (optional)

- LogicSig must be valid before it can use in transaction.
- It is valid if
  - Sig contains a valid signature of the program from the account that is sending the transaction
  - Msig contains a valid multi-signature of the program from the Multi-Signature account sending the transaction
  - The has of the program is equal to the sender's address
- The first two cases are examples of delegation.
- An account owner can grant permission to the signed logic to authorize transaction on their behalf.
- Third case is an acount wholly governed by the program. The program cannot be changed and once Algos or assets have been sent to the account, they can only leave when there is a transactions that approves it.
- This is considered a **contract account**

### Contract account

- For each unique compiled smart signature program they will have a unique Algorand address that can be outputed by `goal clerk compile`.
- Send Algos to a TEAL program and turn it into contract account.
- Outwardly, the account looks no different from the account that we users use.
- It differs that the assets in the contract account is governed by the TEAL program.
- There must be a code that evaluates some condition to be truthy and henceforth executes the sending transaction.

### Delegated approval

- Can be used to delegate signature authority.
- Means that private key signs a TEAL program, the output used to sign transactions on behalf of the account associated.
- The owner can now share the logic signature to allow anyone to spend funds from his/her account in accordance to the logic in the TEAL program.
- Scenario: Alice setup recurring payment to utility company for 200 Algos every 50000 rounds, she creates a TEAL contracts with the logic and signs with private key.
- The logic signature is given to utility company
- Utility company use logic signature in the transaction they submit every 50000 rounds to collect payment from Alice.
- Logic Sig can be produced by single/multisig account.
