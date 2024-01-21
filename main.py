import hashlib
import random
import string
import time

tipsList = []  # Global FIFO list of tips

class Transaction:
    def __init__(self, timestamp, issuer, sender_entity):
        self.timestamp = timestamp
        self.issuer = issuer
        self.sender_entity = sender_entity
        self.weight = 1  # Initial weight, can be adjusted based on simulation requirements
        self.approving_transactions = []


class Entity:
    def __init__(self, id):
        self.id = id
        self.tangle = []    #The ones that confirm it
        self.peers = []     #The ones that the entity confirms
        self.entityTransactions = []
      

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
