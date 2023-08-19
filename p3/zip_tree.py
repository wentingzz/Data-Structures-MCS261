# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file.

from typing import TypeVar
import random 

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')
class Node:
    def __init__(self, k, v, r, left = None, right = None):
        self.key = k
        self.val = v
        self.rank = r
        self.left = left
        self.right = right
    def __repr__(self):
        return f"{self.key} {self.val} {self.rank}"
# from the MCS261-2023 lecture notes
def unzip(x,y):        #insert x to y (to be replaced)
    def unzip_lookup(k,node):
        if node is None: 
            return (None,None)
        if node.key < k:
            (P,Q) = unzip_lookup(k,node.right)
            node.right = P
            return(node, Q)
        else: # node.key > k
            (P,Q) = unzip_lookup(k,node.left)
            node.left = Q
            return(P, node)
    return unzip_lookup(x.key,y)
# from the MCS261-2023 lecture notes
def zip(x):
    def zipup(P,Q):
        if P is None: 
            return Q
        if Q is None: 
            return P
        if Q.rank > P.rank:
            Q.left = zipup(P,Q.left)
            return Q
        else:
            P.right = zipup(P.right,Q)
            return P
    return zipup(x.left,x.right)

class ZipTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def __repr__(self):
        def p(level, node):
            if not node:
                return ""
            res = "  " * level + f"{node}\n"
            res += p(level + 1, node.left)
            res += p(level + 1, node.right)
            return res
        return p(0, self.root)

    @staticmethod
    def get_random_rank() -> int:
        res = 0
        while random.uniform(0, 1) > 0.5:
            res += 1
        return res

    def insert(self, key: KeyType, val: ValType, rank: int = -1):
        self.size, rank = self.size + 1, self.get_random_rank() if rank == -1 else rank
        x, node, prev = Node(key, val, rank), self.root, None
        while node:
            if node.rank < x.rank or (node.rank == x.rank and node.key > x.key):
                break
            if node.key > x.key:
                node, prev = node.left, node
            else:
                node, prev = node.right, node
        x.left, x.right = unzip(x, node)
        if prev:
            if prev.key > x.key:
                prev.left = x
            else:
                prev.right = x
        else:
            self.root = x

    def remove(self, key: KeyType):
        self.size -= 1
        if self.root and self.root.key == key:
            self.root = zip(self.root)
        else:
            node, prev = self.root, None
            while node:
                if node.key == key:
                    tmp = zip(node)
                    if prev.key > key:
                        prev.left = tmp
                    else:
                        prev.right = tmp
                    return
                elif node.key > key:
                    node, prev = node.left, node
                else:
                    node, prev = node.right, node

    def find(self, key: KeyType) -> ValType:
        node = self.root
        while node:
            if node.key == key:
                return node.val
            elif node.key > key:
                node = node.left
            else:
                node = node.right
        return None

    def get_size(self) -> int:
        return self.size

    def get_height(self) -> int:
        def height(node):
            if node:
                return 1 + max(height(node.left), height(node.right))
            else:
                return 0
        return max(height(self.root) - 1, 0)

    def get_depth(self, key: KeyType):
        node, res = self.root, 0
        while node:
            if node.key == key:
                return res
            else:
                res += 1
                if node.key > key:
                    node = node.left
                else:
                    node = node.right
        return res