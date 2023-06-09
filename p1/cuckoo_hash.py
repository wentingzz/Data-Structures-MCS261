# explanations for member functions are provided in requirements.py
# each file that uses a cuckoo hash should import it from this file.
import random as rand
from typing import List

class CuckooHash:
    def __init__(self, init_size: int):
        self.__num_rehashes = 0
        self.CYCLE_THRESHOLD = 10
        
        self.table_size = init_size
        self.tables = [[None]*init_size for _ in range(2)]

    def hash_func(self, key: int, table_id: int) -> int:
        key = int(str(key) + str(self.__num_rehashes) + str(table_id))
        rand.seed(key)
        return rand.randint(0, self.table_size-1)

    def get_table_contents(self) -> List[List[int]]:
        return self.tables

	# you should *NOT* change any of the existing code above this line
	# you may however define additional instance variables inside the __init__ method.

    def insert(self, key: int) -> bool:
        tid, i = 0, 0
        while key != None and i <= self.CYCLE_THRESHOLD:
            pos = self.hash_func(key, tid)
            key, self.tables[tid][pos] = self.tables[tid][pos], key
            tid, i = 1 - tid, i + 1
        if key != None:
            return False
        return True
    
    def lookup(self, key: int) -> bool:
        return self.tables[0][self.hash_func(key, 0)] == key or self.tables[1][self.hash_func(key, 1)] == key
		

    def delete(self, key: int) -> None:
        if self.tables[0][self.hash_func(key, 0)] == key:
            self.tables[0][self.hash_func(key, 0)] = None
        if self.tables[1][self.hash_func(key, 1)] == key:
            self.tables[1][self.hash_func(key, 1)] = None

    def rehash(self, new_table_size: int) -> None:
        prevLen = self.table_size
        self.__num_rehashes += 1; self.table_size = new_table_size # do not modify this line
        toHash = [key for i in range(2) for key in self.tables[i] if key != None]
        self.tables = [[None] * self.table_size for _ in range(2)]
        for i in range(len(toHash)):
            self.insert(toHash[i])

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
