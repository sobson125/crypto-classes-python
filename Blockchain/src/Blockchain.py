import hashlib
import json
from time import time


# Dodaj API do wykonywania "transakcji", pobierania stanu portfela, stanu sieci, liczby bloków w łańcuchu, itp.


class Blockchain(object):
    def __init__(self) -> None:
        super().__init__()
        self.chain = []
        # self.wallet = 0
        self.pending_transactions = []
        self.new_block(previous_hash="carry on my wayward son", proof=420)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

    @property
    def last_block(self):
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash
