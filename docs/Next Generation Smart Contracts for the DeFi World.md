- [original article](https://www.algorand.com/smart-contracts-defi)

---

- DeFi developers are facing challenges
  - **High execution costs**: The fee to interact and execute contracts on legacy networks are very high, often putting the economic viability into question, and creating a barrier to entry that undermines the security of the blockchain by incentivizing bad miners.
  - **Scalability and speed**: The first-gen block consensus times remain quite slow and suffer from regular forking that prohibits scaling as it cause congestions and lack in trust
  - **Security issues**: Legacy smart contracts have a number of bugs that can put assets in a smart contract at risk

## How Algorand's Smart Contracts Can Help in Key DeFi Transactions

### Escrow

Escrow is an account that the funds are locked up until some predetermined conditions have been fulfilled.

A scenario:

- Alice needs a loan
- Bob provides with condition that needs Alice to put another asset inside the escrow (collaterized loan)
- The funds can be released in either
  1. Alice does not pay back the loan after an expiration period -> Bob gets it
  2. Alice does pay back the loan before the expiration period -> Alice gets it

The event that unlocks the funds are usually governed by a centralized 3rd party entity, trusted intermediary such as banks in traditional finance. Requires high fees.

Algorand:

1. Conditions are encoded and secured.
2. Eliminating the need for a centralized authority
3. Take less then 5 seconds
4. Fees of less than a penny.

### Synthetics

- Synthetic cryptocurrency assets enable investors to use their cryptocurrency holdings to purchase stakes in various assets, such as fiat or commodities like gold without leaving the blockchain ecosystem.
- It provides a way for investors to mitigate the volatility of their crypto holdings while preserving the speed and security advantages of investing in a dex.
- Possible via smart contracts that peg stakes of a native token against the value of a synthetic asset and adjusts the stake by an eequivalent amount when the asset goes up or down in value.

### Stablecoins

- Objective: Minimize the risk of volatility levels of digital currencies that are taken on by the stakeholder.
- The volatility of crypto is one greatest impediments slowing down the widespread adoption of crypto.
- Stablecoins drastically reduce the risk taken by investors as the stablecoin is pegged to stable assets like USD or EURO using smart contracts.
- USDT and USDC have already been launched on Algorand, enabling organizations and financial institutions to build fast and scalable application with reduced counterparty risk

### Credit and Lending

- Opens up a new lending opportunities to indivuduals who lack access to traditional financing services.
- Lending in decentralized financial environment enables borrowers to circumnavigate the normal limitations of borrowing from a centralized firm (such as poor credit score)
- However, lender cannot trust borrowers without an intermediary of some sort.
- Traditionally, this would require a third-party, but smart contracts offer the value proposition of replacing that intermediary with self-executing lines of code that either accept or reject whether the conditions of the agreement were met.
- More people will have access to cheaper loans that are best suited for their needs.

### Exchanges and Liquidity

- The smart contract built into the exchanges automatically matches, verifies and finalizes these transactions without an intermediary.
- These exchanges offers increased levels of liquidity to investors, as the investors can swap digital assets in a matter of seconds.
- Algorand smart contract in layer-1 enables developers to build applications that keep track of buy and sell offers and matches them up so anyone across the network can trade with each other without the need of an dex.

### Margin Trading

- Powered by ASC1, margin trading with digital assets provides investors with the ability to use borrowed funds from a broker to trade a financial asset, which forms the collateral for the loan from thr broker
- ASC1 have the ability to automacally enforce custom rules and logic, making it possible to margin trade without working through traditional financial gatekeepers and thus cutting the cost for the trade and improving potential return.
- The end goal in margin trading digital currencies is to get a higher percentage return in the form of leveraged payouts.
- Increases both the return and risk associated with the trade.
- 2x leveraged means the potential value lost or gained is doubled.
- Allows traders to capitalize more heavily on the volatile nature of cryptocurrencies, hopefully timing their leveraged investment with a market upswing.
- Can also short for downswings.

### Alternative Savings

- Serves the same purpose as traditional saving account provided by bank.
- Funds placed are trasferred into currency pools to be lend out to willing borrowers.
- Alternative savings account are built using smart contracts.
- Rewards will be distributed to savings account holders based on the amount of interest accumulated from the loans.
- Typical traditional savings offer 1% APY but Alternative savings offer up to 5% APY.

### Payment Solutions

- Payment-based application are primarily used for transferring fund from one to another.
- Example: Algorand Mobile Wallet.
- Payment applications may be implemented with different currency or token such as stable coins.
- Atomic transfers is trustless and group transactions

### Prediction Markets

- Allow users to purchase and sell shares in the outcome of an event.
- Prediction markets now are centralized that controlled by one party thus open for fraudulent activity.
- Decentralized prediction markets allows thousands of users to report on the outcome of an event to ensure the result is accurate.
- This is referred as "Wisdom of the Crowd"
- No limitation on what topic to bet and no limit on tha amount fo bet.
- Usually centralized prediction market have limitations such as capped betting to mitigate the loss to the firm
- Smart contracts remove centralized intermediaries, resulting in lower transaction fees and more secure funds
- The smart contract will execute once the outcome of the event is reported and distribute the funds.

### Marketplaces

- Centralized: eBay, Amazon. Dictates terms of trade and take commission from transactions.
- Decentralized: Allow buyer and seller to trade without middleman, save fees.
- Dex also solves privacy: No pii data.

---

Glossary

- nascent
- much-tapped potential
- fringe
- tamper-proof (trustless)
