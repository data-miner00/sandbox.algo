- [Link](https://developer.algorand.org/docs/get-details/algorand_consensus/)

---

## Algorand consensus

- Algorand use a decentralized Byzantine Agreement protocol that leverages Pure Proof of Stake.
- This algorithm can tolerate malicious users while achieving consensus without a central authority as long as a supermajority of the stake is in non-malicious hands.
- The protocol is fast and require minimal computational power and able to finalize transactions efficiently.

## Verifiable Random Function

- VRF takes a secret and value and produce a **pseudorandom output**, with a proof that anyone can use to verify the result.
- The VRF output is used to sample from a binomial distribution to emulate a call for every algo in user's account.
- The more algo in an account, the greater chance the account of being selected.
- This ensures a user does not gain any advantage by creating multiple accounts.

## Participation Keys

- User must be online to participate
- (To reduce exposure) Online users does not use their _spending_ keys (the keys that use for signing tx) for consensus
- They will generate and register a participation key for a certain number of rounds
- It also generates a collection of _ephemeral keys_, one for each round, signs these keys with the participation key and finally revoke the participation key.
- Ephemeral key is used to sign messages for the corresponding round, and is deleted after the round is over.
- The rational of using a participation key is to ensure that the user's token are secure even if their participating node is compromised.
- Deleting participation and ephemeral keys after they are used ensures Algorand is forward-secure and cannot be compromised by attacks on old blocks using old keys.

## State Proof Keys

- `go-algorand 3.4.2` released March 2022, users also generate a state proof key along with associated ephemeral key and participation keys.
- State proof keys is used for generating Post-Quantum secure state proofs that attest to the state of the blockchain at different points in time.
- It is useful for apps that want a portable, lightweight way to cryptographically verify Algorand state without running a whole participation node.

## The Algorand Consensus Protocol

- Consensus requires 3 steps to propose, confirm and write the block: 1. Propose 2. Soft vote 3. Certify vote
  > Note: All messages are cryptographically signed with the user's participation key and committee membership is verified using the VRF

### Block Proposal

- Accounts are selected to propose new blocks to the network
- Starts with looping through each online account that has valid participation keys and running VRF to determine if the account is selected to propose the block
- VRF can be analogise as a weighted lottery that takes the amount of ALGO into consideration
- Once an account is selected, the node itself propagates the proposed block along with the VRF output that certify that the account is a valid proposer.

### Soft vote

- **Purpose**: narrow down the proposals to just a single one.
- This make sure only one block proposals get accepted as there are many proposals from other nodes
- Nodes verify the signature of the message and validate the selection using the VRF proof.
- The node compare the hash between the validated proposals and only will propagate the block proposals with the lowest VRF hash

- Each node then run VRF for every participating account it manages to see if they have been chosen to participate in the soft vote committee
- If any account is chosen it will have a weighted vote based on the number of ALGOs the account has and these votes will be propagated to the network
- These votes will be for the lowest VRF block proposals calculated at the timeout and will be sent out to the other nodes along with the VRF proof

- A new committee is selected for every step in the process and each step has a different committee size.
- The committee size is quantified in algos
- A quorum of votes is needed to move to next step and must be a certain percentage of the expected committee size.
- These votes will be received from other nodes on the network and each node will validate the committee membership VRF proof before adding to the vote tally.
- Once a quorum is reached for the soft vote the process moves to the certify vote step

### Certify vote

- A new committee checks the block proposal that was voted on in the soft vote stage for overspending, double-spending, or any other problems.
- If valid, the new committes votes again to certify the block.
- This is done similar to soft vote where each node iterates through its managed accounts to select a committee and to send votes
- The votes are collected and validated by each node until a quorum is reached, triggering an end to the round and prompting the node to create a certificate for the block and write it to the ledger
- At this point, a new round starts over
- If a quorum is not reached in a certifying committee vote by a certain timeout then the network will enter recovery mode
