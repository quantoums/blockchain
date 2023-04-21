import json
from datetime import datetime
from hashlib import sha256
import random



class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.previous_hash = None
        
        #create genesis block
        print(" \n---------------LIGHT ON !--------------------\n")

        self.proof_of_work()

    def get_chain(self):
          print(self.chain)

    def get_block(self,index):
          if(index < len(self.chain)):
            return self.chain[index]
          return 'This block does not exist !'

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
                # we get rid of pending transactions for the moment 

                block = {'index':len(self.chain),
                         'timestamp' : datetime.utcnow().isoformat(),
                         'transactions' : [],
                         'previous_hash' : self.previous_hash,
                         'nonce ' : format(random.getrandbits(8),"x")
                         }
                # hash the block
                hash = self.hasher(block)

                # add the  hash to the block
                block['hash'] = hash

                # return block

                return block

                
    # We stipulate that a block is valid if its hash begins with '0000'
    # the method is static, we can use it outside of the classes object to see if any subjected block is valid 
    @staticmethod
    def valid_block(block):
          return block['hash'].startswith('0000')
    
    # since in the block we have the field 'once" wich is a 64-bits hex number randomly generated
    # the work consists of finding a block with a hash starting with "0000"
    # if the block is not valid, we create a new one via the once randomly generated
    # 

    def proof_of_work(self):
            while True:
                  new_block = self.new_block()
                  if self.valid_block(new_block):
                        break
           # add the block to the chain
            self.chain.append(new_block)

            # update previous hash value
            self.previous_hash = new_block['hash']
            if(len(self.chain)==1):

                  print(f"\n Block {new_block['index']} : Genesis \n hash : {new_block['hash']} \n Ther are {len(self.chain)} blocks ! \n")
            
            else :
                  print(f"\n Block {new_block['index']}\n hash : {new_block['hash']} \n Ther are {len(self.chain)} blocks ! \n")
            
          
          
          
          





    
