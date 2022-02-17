
class BlockChain:

    def __init__(self, content, pb=None, id=1):
        if pb is not None:
            self.pb_hash = f"Hashed::{pb.content}{pb.id}$$"
        else:
            self.pb_hash = pb

        self.nb = None
        self.id = id
        self.content = content
        self.hash = f"Hashed::{self.content}{self.id}$$"

    def create_block(self, content):
        """ Create new next block at the end of chain """

        if self.nb is None:
            self.nb = BlockChain(content, id=self.id+1, pb=self)
        else:
            self.nb.create_block(content)

    def get_all_blocks(self):
        """ Get detials of this block and previous block """

        print(f"""
            {self.id} This Block Detial:
                content: {self.content}
                id: {self.id}
                hased: Hashed::{self.content}{self.id}$$

            Previous Block Detail:
                hashed: {self.pb_hash}
        """)

        if self.nb is not None:
            self.nb.get_all_blocks()

    def verify_hash(self, hash):
        """ Checks if the block exists or not using its hash """

        if hash == self.hash:
            return True
        elif self.nb is not None:
            return self.nb.verify_hash(hash)
        else:
            return False

bc = BlockChain(content="Initial Block")

bc.create_block(content="block1")
bc.create_block(content="block2")
bc.create_block(content="block3")
bc.create_block(content="block4")
bc.create_block(content="block5")
bc.create_block(content="block6")

bc.get_all_blocks()
