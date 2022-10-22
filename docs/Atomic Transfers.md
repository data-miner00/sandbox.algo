- [Link](https://developer.algorand.org/docs/get-details/atomic_transfers/)

---

- Traditional finance: Trading assets need trusted intermediary to make sure both sides receive what they agreed to.
- Algorand: This is atomic transfer. It either all succeed or all fail. Allows strangers to trade assets without intermediary, all while guaranteeing what is agreed.
- Atomic transfer is implemented as irreducible batch operations, where group of transactions are submitted as a unit.
- This eliminates the need for complex solutions such as [hashed timelock contracts](https://en.bitcoinwiki.org/wiki/Hashed_Timelock_Contracts) on other blockchain.
- Atomic transfer finalized within 5 seconds.
- Transactions can contain Algos or ASA.

## Use cases

- **Circular trades** - Alice pays Bob if and only if Bob pays Claire if and only if Claire pays Alice.
- **Group payments** - Everyone pays or no on pays.
- **Decentralized exchanges** - Trade one asset for another without going through a centralized exchange.
- **Distributed payments** - Payments to multiple recipients.
- **Pooled transaction fees** - One transaction pays the fees of others.

## Process overview

- Generate all transactions that will be involved in the transfer and group them together
- Each transactions is assigned the same group ID
- Transactions split up and sent to their respective senders to be authorized.
- A single party collect all authorized transactions and submit to network together
