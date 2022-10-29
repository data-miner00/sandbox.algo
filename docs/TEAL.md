- [link](https://www.youtube.com/watch?v=OWFRP9McBmk)

---

- Transaction Execution Approval Language
- Stack language
- Can analyze and approve (reject) transaction but cannot change or create transaction
- Transaction is approved by TEAL is as good as cryptographically signed by an account key in one of two conditions:
  - The TEAL code is signed by an account key
  - The TEAL code hashes to the account address (creates a contract account)

### Teal cannot do

- create or change a transaction, only approve or reject
- lookup balances of Algos or other assets
- access information in previous blocks or transactions
- know exactly what round the current transaction will commit in
- know exactly what time its transaction is committed
- loop.bnz "branch if not zero" can only branch forward so as to skip some code
- recurse

### Teal can do

- cross chain swaps via hashed-time-locked-contract
- automatic payment splitting
- recurring payments
- limit order trades
