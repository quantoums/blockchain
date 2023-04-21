import json
from datetime import datetime
from hashlib import sha256



class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.previous_hash = None
        
        #create genesis block
        print(" \n---------------LIGHT ON !--------------------\n")

        self.new_block()

    def get_chain(self):
          print(self.chain)

    def last_block(self):

        # returns the last block of the chain
        return self.chain[-1]
    

    @staticmethod # can be called from any object even if its not from the class
    def hasher(block):
          
          #transform the block to string to not have any problems of hashing
          block_string = json.dumps(block,sort_keys=True)
          encoded_block_string = block_string.encode()
          hash = sha256(encoded_block_string).hexdigest()
          return hash
    
    def new_transaction(self,receiver,sender,amount):
          #add new transaction inside the list of pending transactions 

          transaction = {'receiver' : receiver,  
                         'sender' : sender,
                         'amount' : amount}
          self.pending_transactions.append(transaction)

    def new_block(self):

                # create new block as dictionary, each block contains index, time, the previous_hash
                # the transactions to validate are in the pending_transactions list
                # each block has to validate those transactions 

                block = {'index':len(self.chain),
                         'timestamp' : datetime.utcnow().isoformat(),
                         'transactions' : self.pending_transactions,
                         'previous_hash' : self.previous_hash
                         }
                # hash the block
                hash = self.hasher(block)
                # add the  hash to the block
                block['hash'] = hash

                # add the block to the chain
                self.chain.append(block)

                # update previous hash value
                self.previous_hash = hash

                # empty pending_transactions since they've been hashed and put to the block
                self.pending_transactions = []
                # return the block
                return block




    
