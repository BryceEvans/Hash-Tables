

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity, count):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.count = 0


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381

    for character in string:
        hash = ((hash << 5) + hash) + ord(character)

    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    # Generate index for key using hash function.
    index = hash(key, hash_table.capacity)
    print(f"Insert Print Statment {key} {index}")

    # Lets retrieve the current pair at the specified index.
    current_pair = hash_table.storage[index]

    # Loop if the current pair already is a LL.
    # If the key already exists in the LL we just change the value for that key.
    while current_pair is not None and current_pair.key != key:
        # Assign current pair to the next pair.
        current_pair = current_pair.next

    # if current pair is None then the key does not exist in our hash table because it is new.
    if current_pair is None:
        # Create a new pair for our new key and value.
        new_pair = LinkedPair(key, value)
        # Grab old head.
        old_head = hash_table.storage[index]
        # Assign the LL head to the new pair.
        hash_table.storage[index] = new_pair
        new_pair.next = old_head

        if new_pair.next is None: # [LL(2 Pairs), LL(1 Pair), None]
            hash_table.count += 1
    
    
    
    
    
    # # pair = Pair(key, value)

    # current_pair = hash_table.storage[index]

    # last_pair = None
    # while current_pair is not None and current_pair.key != key:
    #     # last_pair = current_pair
    #     current_pair = current_pair.next

    # if current_pair is None:
    #     new_pair = Pair(key, value)
    #     new_pair.next = hash_table.storage[index]
    #     hash_table.storage[index] = new_pair
    # else:
    #     current_pair.value = value

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    pass


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    # Generate index for key using hash function.
    index = hash(key, hash_table.capacity)
    # check_hash_table(new_hash_table))
    # Lets get current pair at the specified index.
    current_pair = hash_table.storage[index]

    if current_pair is not None:
        # Loop if the current pair already is a LL.
        # We also need to check if the key exists in the LL.
        while current_pair is not None and current_pair.key != key:
            # Assign the current pair to the previous pair.
            # Assign the current pair to the next pair.
            prev_pair =  current_pair
            current_pair = current_pair.next
        

        # If the previous pair is none and the current pair key equals key.
        # Then, remove the only pair that existed at the current index position in the hash table.
        if prev_pair is None and current_pair.key == key:
            hash_table.storage[index] = None
            hash_table.count -= 1
        # If current pair is None the key does not exist in our hash table.
        elif current_pair is None:
            print(f"Error 1: {key} not found.")
        else:
            # We found the key!! We change the next pointer of previous pair to None.
            prev_pair.next = None
    else:
        print(f"Error 2: {key} not found.")

# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    # Create a new hash table and give it a new capacity (e.g Double the old capacity).
    new_hash_table = HashTable(hash_table.capacity * 2)

    for x in range(hash_table.count):
        current_pair = hash_table.storage[x]

        while current_pair is not None:
            hash_table_insert(new_hash_table, current_pair.key, current_pair.value)
            current_pair = current_pair.next

    # Use the function below to check your new hash table!
    # check_hash_table(new_hash_table)

    return new_hash_table

def check_hash_table(hash_table):
    arr = []

    for x in range(hash_table.count):
        arr.append([])
        current_pair = hash_table.storage[x]

        while current_pair is not None:
            if current_pair.next is None:
                arr[x].append((current_pair.key, current_pair.value, None))
            else:
                arr[x].append((current_pair.key, current_pair.value, current_pair.next.key))
            current_pair = current_pair.next

        print('New hash table: ', arr)


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity) + " to " + str(new_capacity) + ".")


Testing()
