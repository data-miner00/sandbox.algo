- [Video](https://www.youtube.com/watch?v=gACVKaNqxPs)
- [Original blog](https://www.algorand.com/resources/blog/silvio-micali-lex-fridman-algorand-and-the-blockchain-trilemma)

---

- Blockchain Trilemma: Security, Scalability and decentralization
- Algorand allegedly solve the trilemma with Pure Proof of Stake (PPoS) consensus algorithm
- As long as the supermajority of the nodes in the network agrees on what should be added to the blockchain, Algorand is able to achieve the consensus in a fully decentralized network effeciently
- Algorand founded by [Silvio Micali](https://www.algorand.com/about/from-our-founder), a professor in MIT that has rich experience in cryptography and computer science

## The Importance of Scalability

- Bitcoin is not scalable. The finality for a transaction is too long. This way of making transactions is not tolerated by a fast moving society that we currently live in.
- Ethereum offers more scalability but compromises decentralization. Ethereum before the PoS upgrade favours centralization due to the mining process, which requires high-end machines to perform more verification.
- Micali: Scalability - high speed add new data, data sharing and verify validity.
- Micali: Estinate the world needs ledgers capable to process at least 1,000 tps
- Compare to credit cards (16,000 tps) on average and max can reach 40,000 tps
- Credit card is operated by centralized entities, the goal of blockchain is make sure tx is processed but also shared, visible and verifiable.
- Most scalable blockchain solution is **Delegated Proof of Stake (DPoS)**: A selected group of validators is handling the addition of new blocks. This is a more democratic approach, however
- > _One is centralized, 21 is also centralized_

## Algorand Employs Randomness to Solve Blockchain Trilemma

- Algorand achieve scalability while maintaining decentralization
- Algorand does this by selecting validators randomly from all token holders.
- The network relies on an algorithm that automatically picks the next group of nodes that become eligible to add blocks.
- This maintains decentralization since anyone can be selected by system.
- Nobody knows who is the next validators and this ensures security
- > Randomness is powerful to achieve decentralization and prevent 51% attack
- The only way to damage the Algorand network is to achieve a self-destructive majority of token holders, which is impossible in practice, as no one is interested in losing value.

## Who is Responsible With Random Picking Validators?

- Algorand do something **unorthodox**.
- The token holders choose themselves at random.
- Each token holders is executing his individual lottery to win the ticket next block in Algorand.
- Micali says that no matter how powerful the computing power that a party have, it doesn't increase the probability of winning the lottery.
- Every time, there are only 1,000 winners that able to validate the next blocks.
- It is scalable as the lottery happen in one microsecond.
