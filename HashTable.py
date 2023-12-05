# WGU #011047348
# Jeongwook Na
# C950 Task 2

# This code is from the course search => C950 - Webinar-1 - Let's Go Hashing -Complete Python Code
# W-1_ChainingHastTable_zyBooks_Key-Value.py

class HashTable:
    def __init__(self, initialcapacity=40):
        self.table = []
        for i in range(initialcapacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, key, item): # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print(key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes an item with matching key from the hash table
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if key in bucket_list:
            bucket_list.remove(key)
