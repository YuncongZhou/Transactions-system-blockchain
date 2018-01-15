import hashlib
import json

from time import time
from uuid import uuid4

class Blockchain(object):
    """
    It's a blockchain object implementation with all the POW features
    """


    def __init__(self):
        self.chain = []
        self.current_transactions = []

        #Create the genesis block with no predecessors
        self.new_block(previous_hash=1, proof = 100)

    def new_block(self):
        """
        creating a new block and append it to the blockchain
        :return: <Blockchain>
        """

        block ={
            'index': len(self.chain+1),
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        #reset transactions
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self):
        """
        add a new transaction in temp and add it to new block later on
        :return: <int>
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1


    @staticmethod
    def hash(block):
        """
        use this hash function to chain the blocks together
        :param block: <Blockchain>
        :return: <int>
        """

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        return the last block in the blockchain
        :return: <Blockchain>
        """
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        simple POF to find a hash result which has 4 leading zeros
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof


    @staticmethod
    def valid_proof(last_proof, proof):
        """
        chech if we got a valid proof which can produce 4 leading zeros
        :param last_proof: <int>
        :param proof: <int>
        :return: <bool>
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"






