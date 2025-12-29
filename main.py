import hashlib as hasher
import datetime as date

# Block class
class Block:
  # initialize block
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
  # method to hash the block
  # "hashing the block" means converting the block's contents into a fixed-size string of characters,
  #  a sequence of numbers and letters.
  def hash_block(self):
    sha = hasher.sha256()
    sha.update((str(self.index) + 
               str(self.timestamp) + 
               str(self.data) + 
               str(self.previous_hash)).encode('utf-8'))
    return sha.hexdigest()

# Create the genesis block
# the genesis block is the first block in a blockchain.
def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  return Block(0, date.datetime.now(), "Genesis Block", "0")

# Create subsequent blocks
def next_block(last_block):
  index = last_block.index + 1
  timestamp = date.datetime.now()
  data = "Hey! I'm block {}".format(index)
  previous_hash = last_block.hash
  return Block(index, timestamp, data, previous_hash)

# Main program
if __name__ == '__main__':
  # Create the blockchain and add the genesis block
  blockchain = [create_genesis_block()]
  previous_block = blockchain[0]

  # How many blocks should we add to the chain
  # after the genesis block
  num_of_blocks_to_add = 20

  # Add blocks to the chain
  for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    # Tell everyone about it!
    print('Block #{} has been added to the blockchain!'.format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))