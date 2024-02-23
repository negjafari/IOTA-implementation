# IOTA Consensus Algorithm implementation

## Introduction
This implementation provides a simplified version of the algorithm, focusing on key steps involved in the consensus process. (based on IOTA paper implementation which is provided in this repository)

### Steps Implemented

1. **Calculating Hash:** 
   - Generates a new transaction with a unique ID, timestamp, and sender entity ID.
   - Calculates the hash of the transaction and prints the result.

2. **Selecting Two Transactions:**
   - Utilizes a transaction selection method to choose two transactions from the tipsList and unconfirmedList based on predefined criteria.
   - Prints the IDs of the selected transactions.

3. **Checking Transaction Conflict:**
   - Validates the selected transactions to ensure they are non-conflicting.

4. **Applying Required Changes:**
   - Updates the approved transactions for both the selected transactions and the newly created transaction.
   - Adds the hash of the new transaction to the selected transactions’ headers (previous_hashes list).
   - Adjusts the status of transactions in the tipsList and unconfirmedList.

5. **Updating Cumulative Weights and Confirmation:**
   - Adds the new transaction to the current node's transaction list.
   - Updates the tipsList and checks if any unconfirmed transactions have reached the cumulative weight threshold for confirmation.

### Implementation Details

For detailed implementation insights and code walkthrough, refer to the `IOTA Consensus Algorithm Implementation` document stored in this repository.
