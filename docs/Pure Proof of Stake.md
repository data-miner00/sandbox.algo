- [Link](https://www.algorand.com/technology/pure-proof-of-stake)

---

## Algorand's PPoS

- Algorand uses a PPoS protocol built on Byzantine consensus
- Users randomly and secretly selected to propose blocks and vote on block proposals
- All online users have the chance to be selected to propose and vote
- The likelihood that a user will be chosen and the weight of its proposals and votes are directly proportional to its stake

- PPoS approach ties **security** of the whole economy to **honesty** of majority of the economy rather than a small subset of the economy
- Assumption: It would be too foolish for the majority of the owners of the majority to misbehave as it will
  1. depreciate the currency
  2. devalue their own asset

## PPoS vs PoW

- PoW is an approach in which users race to solve very complex cryptographic puzzles (mining)
- The first one to solve the puzzle is entitled to append the next block to the chain and is rewarded.
- PPoS has numerous advantages over PoW

| PPoS                                                                                  | PoW                                                                                                             |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| No solving cryptographic puzzle                                                       | Wasteful and expensive                                                                                          |
| User that online and possesees stake is eligible to participate                       | Consumes enormous amount of electricity                                                                         |
| Participation cost (Computational and financial) is very low                          | Favors professional miners that have the capital expenditure to buy racks of hyper-specialized mining equipment |
|                                                                                       | Only one miner participate in block generation, others effort wasted                                            |
|                                                                                       | Concentration of power and de facto centralization as a result of miners pooling their resources                |
| Malicious users do not gain any advantage by splitting their stake into many accounts | These mining pools can erase blocks or change the order of blocks if they wish or if they’re bribed to do so    |
| Low computation and communication overhead, blocks propagated within seconds          | Slow as takes 10 minutes to propagate blocks to network, lack of scalability                                    |
| Never forks, adding block needs whole committee to vote on                            | Have small chance that 2 users solve simultaneously, blockchain forks into two                                  |

- Bitcoin currently controlled by 3 mining pool and Ethereum controlled by 2
- Blockchain that is centralized is dangerous and insecure

- Forks may persist for a while and elongated by addition of new blocks, but all smaller branch will eventually die and the transactions on the branches are invalidated.
- Forks are unwelcome souce of uncertainty and delay
- If a payment is made and appears in the latest block in chain, it still cannot guarantees the payment will lasts
- All txs are final in Algorand

## PPoS vs DPoS

- Delegated Proof of Stake is an approach in which a fixed number of elected entities (delegates) are selected to create blocks in a round-robin manner
- Delegates are voted into power by the users of the network, who each get a number of votes proportional to the number of tokens they own
- EOS: The number of delegates is 21
- Limited amount of block producers -> Able to produce higher throughput
- It offers scalability but sacrifices decentralization
- No guarantee all delegates remain honest and is easilly attacked (vulnerable to DoS attack)

- PPoS doesn't put a small set of users in charge of block generation
- There is no special group for attacker to attack

## PPoS vs BPoS

- Bonded Proof of Stake is an approach in which any number of users set aside part of their stake (bond) in order to influence block generation
- They lock up part of their stake for a certain amount of time (security deposit) and get chance proportional to that stake to select next block
- Once locked, it cannot withdraw within a threshold of time
- Users forfeit their stake along with priviledge of participating in the consensus process when they are found dishonest
- Drawback: User cannot spend their stake when participating in the consensus
- Algorand: No stake is ever held hostage
