class HashTable:
    
    class _Node:

        def __init__(self, key, value, next_node=None):
            self.key = key
            self.value = value
            self.next = next_node

    def __init__(self, key):
        return hash(key) % self.capacity
    
    def insert(self, key, value):
        if self.size >= self.capacity * 0.7:
            self._resize()

        index = self._hash(key)
        node = self._table[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next
        
        raise KeyError(f"Key '{key}' not found.")
    
    def delete(self, key):

        index = self._hash(key)
        node = self._table[index]
        prev = None

        while node:
            if node.key == key:
                if prev is None:
                    self._table[index] = node.next
                else:
                    prev.next = node.next
                self.size -= 1
                return
            prev = node
            node = node.next

        raise KeyError(f"Key '{key}' not found.")
    
    def _resize(self):
        old_table = self._table
        self.capacity *= 2
        self.size = 0
        self._table = [None] * self.capacity

        print(f"\n--- Resizing table to {self.capacity} ---")

        for head_node in old_table:
            node = head_node
            while node:
                self.insert(node.key, node.value)
                node = node.next

    

            
