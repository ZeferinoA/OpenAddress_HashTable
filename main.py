from hash_table import HashTable

def main():
    print("Creating a new hash table with capacity 10...\n")
    ht = HashTable(capacity=10)

    # insert some key-value pairs
    print("Inserting key-value pairs:")
    ht.insert("apple", 100)
    ht.insert("banana", 200)
    ht.insert("grape", 300)
    ht.insert("cherry", 400)
    ht.insert("apricot", 500)  # likely to collide with "apple"

    ht.display()

    # find values
    print("finding some values:")
    print("apple:", ht.find("apple"))
    print("banana:", ht.find("banana"))
    print("grape:", ht.find("grape"))

    # Remove a key
    print("\nRemoving 'banana' from the table...")
    ht.remove("banana")
    ht.display()

    # Try findting a removed key
    print("banana:", ht.find("banana"))

    # Reset the table
    print("\nResetting the table...")
    ht.reset()
    ht.display()

    # Re-insert
    print("Re-inserting after reset:")
    ht.insert("kiwi", 999)
    ht.display()

    # Show collision count
    print("\nCollision count:")
    print(ht.collisions())

if __name__ == "__main__":
    main()