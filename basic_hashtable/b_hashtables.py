

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381

    for character in string:
        hash = (((hash << 5) + hash) + ord(character))

    return hash % max
# def hash(string):
# 	hash = 5381
#         for x in string:
#             hash = ((( hash << 5) + hash) + ord(x)) & 0xFFFFFFFF
#         return hash


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # get the hash version of key
    key_hash = hash(key, 5)
    # create a new pair using the key, value pair that was passed into function
    new_pair = Pair(key, value)
    # get the index by doing key_hash modulo hash_table.capacity
    index = key_hash % hash_table.capacity
    # if index has pair already, check if keys match
    if hash_table.storage[index] != None:
        # if keys don't match, pring warning but otherwise do nothing
        if key == hash_table.storage[index].key:
            print(f"Collision detected for {key} and {hash_table.storage[index].key}!")
        # if the keys do match, update the value
        else:
            hash_table.storage[index].value = value
    else:
        hash_table.storage[index] = new_pair

    # index = hash(key, hash_table.capacity)
    # pair = Pair(key, value)
    # if hash_table.storage[index] is not None:
    #     print("Warning: overwriting " + str(hash_table.storage[index].key) + "!")
    # hash_table.storage[index] = pair

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    # Get hash versin of key
    hash_key = hash(key, 5)
    # get index by mudolo the key by hash_table's capacity
    index = hash_key % hash_table.capacity
    # if there is a value other than None at index
    if hash_table.storage[index] != None:
        # set value to None
        hash_table.storage[index] = None
    #else print a warning:
    else:
        print(f"{key} not found in hash table and thus cannot be removed.")



# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    # Get hash versin of key
    hash_key = hash(key, 5)
    # get index by mudolo the key by hash_table's capacity
    index = hash_key % hash_table.capacity
    # if index is not equal to None
    if hash_table.storage[index] is not None:
        # if key is equal to key we are looking up
        if hash_table.storage[index].key == key:
            # return value
            return hash_table.storage[index].value
    # return None
    return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")
    print(ht.storage)

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
