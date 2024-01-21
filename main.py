import hashlib
import random
import string
import time

tipsList = []  # Global FIFO list of tips

class Transaction:
    def __init__(self, timestamp, issuer, sender_entity):
        self.data = self.get_random_string()
        self.timestamp = timestamp
        self.issuer = issuer
        self.sender_entity = sender_entity
        self.hash = self.calculate_hash()
        self.weight = 1  # Initial weight, can be adjusted based on simulation requirements
        self.cumulative_weight = self.calculate_cumulative_weight()
        self.approving_transactions = []

    def get_random_string(self):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))

    def calculate_hash(self):
        data = str(self.data) + str(self.timestamp) + str(self.issuer)
        return hashlib.sha256(data.encode()).hexdigest()

    def calculate_cumulative_weight(self):
        if not self.approving_transactions:
            self.cumulative_weight = self.weight
        else:
            self.cumulative_weight = self.weight + sum(
                [txn.calculate_cumulative_weight() for txn in self.approving_transactions]
            )
        return self.cumulative_weight

class Entity:
    def __init__(self, id):
        self.id = id
        self.tangle = []    #The ones that confirm it
        self.peers = []     #The ones that the entity confirms
        self.entityTransactions = []
      

    def send_transaction(self):
        timestamp = time.time()
        transaction = Transaction(timestamp, self.id, self)

        tipsList.append(transaction)     # Add the transaction to the global FIFO list

        peer = random.choice(self.peers)    # Simulate network propagation by randomly selecting a peer
        peer.receive_transaction(transaction)
        self.entityTransactions.append(transaction)  # Add the transaction to history
        print(f"Entity {self.id} sent a transaction: {transaction.data}")

        # Choose the first two transactions from the global FIFO list
        approving_transactions = tipsList[:2]
        for txn in approving_transactions:
            txn.approving_transactions.append(transaction)

            # Check if the transaction reached the limit of 2 confirmations(chon halet goft ta depth2 mitone entekhab kone)
            if len(txn.approving_transactions) >= 2:
                print(f"Transaction {txn.data} confirmed by two entities.")
                # Remove the confirmed transaction from the global FIFO list
                tipsList.remove(txn)

    def receive_transaction(self, transaction):
        # Simplified consensus algorithm (checking if the transaction is valid)
        if self.is_transaction_valid(transaction):
            self.tangle.append(transaction)
            transaction.approving_transactions = self.tangle  # Set approving transactions
            print(f"Entity {self.id} received a valid transaction: {transaction.data}")

    def is_transaction_valid(self, transaction):
        # Simulate transaction validation (check if the hash is correct)
        return transaction.hash.startswith("0000")  # Simplified validation condition

def simulate_network(entities, num_transactions):
    # Create a network by connecting each entity to two random peers
    for i in range(len(entities)):
        entity = entities[i]
        entity.peers = random.sample([n for n in entities if n != entity and not n.tangle], 2)

    # Generate and send transactions to the network
    for _ in range(num_transactions):
        random_entity = random.choice(entities)
        random_entity.send_transaction(f"Transaction {_}")

    # Print cumulative weights after transactions are sent
    for entity in entities:
        print(f"Entity {entity.entity_id} - Cumulative Weight: {entity.tangle[-1].calculate_cumulative_weight()}")

def main():
    num_entities = 5
    num_transactions = 10

    entities = [Entity(i) for i in range(num_entities)]       # Create entities

    simulate_network(entities, num_transactions)

if __name__ == "__main__":
    main()
