class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0
        self._collision_count = 0

    def reset(self):
        self.table = [None] * self.capacity
        self.size = 0

    def _hash_function(self, key):
        hash_val = 0
        for i, char in enumerate(key):
            hash_val += (i + 1) * ord(char)
        return hash_val % self.capacity

    def _probe(self, start, key):
        index = start
        while self.table[index] is not None:
            if self.table[index].key == key:
                return index
            index = (index + 1) % self.capacity
            if index == start:
                raise Exception("Hash table is full!")
        return index

    def insert(self, key, value):
        index = self._hash_function(key)
        start = index
        steps = 0

        while self.table[index] is not None:
            if self.table[index].key == key:
                self.table[index].value = value
                return
            index = (index + 1) % self.capacity
            steps += 1
            if index == start:
                raise Exception("Hash table is full")
        
        if steps > 0:
            self._collision_count += 1

        self.table[index] = Node(key, value)
        self.size += 1

    def find(self, key):
        index = self._hash_function(key)
        start = index
        while self.table[index] is not None:
            if self.table[index].key == key:
                return self.table[index].value
            index = (index + 1) % self.capacity
            if index == start:
                break
        return None

    def remove(self, key):
        index = self._hash_function(key)

        start = index
        while self.table[index] is not None:
            if self.table[index].key == key:
                self.table[index] = None
                self.size -= 1
                return True
            index = (index + 1) % self.capacity
            if index == start:
                break
        return False

    def display(self):
        print(f"Hash Table (capacity={self.capacity}, size={self.size}):")
        for i, node in enumerate(self.table):
            if node is None:
                print(f"Index {i}: Empty")
            else:
                print(f"Index {i}: (key={node.key}, value={node.value})")
        print()

    def collisions(self):
        return self._collision_count