"""Contains functions to convert infix expressions
to postfix, then evaluating them.

Project 2: Evaluating Expressions using Stacks
Author:
    Richard Hua
Class: CPE202
"""

from linked_list import Node

class HashTableSepchain:
    """Hash table that holds key-value pairs with separate chaining
    collision handling.

    Table is a list of nodes that hold k-v pairs with links to next pair
    from chaining, otherwise None.

    Attributes:
        size (int) : size/capacity of the table
        num_items (int) : number of k-v pairs currently in table
        num_collisions (int) : number of collisions during insertions
        table (list) : a list of nodes holding k-v pairs
    """

    def __init__(self, table_size=11):
        self.table_size = table_size
        self.num_items = 0
        self.num_collisions = 0
        self.table = [None] * self.table_size

    def __eq__(self, other):
        return isinstance(other, HashTableSepchain)\
        and (self.table_size == other.table_size)\
        and (self.num_collisions == other.num_collisions)\
        and (self.num_items == other.num_items)\
        and (self.table == other.table)

    def __repr__(self):
        return 'HashTableSepchain\
        (size=%s, num_items=%s, num_collisions=%s, table=%s)'\
        % (self.table_size, self.num_items, self.num_collisions, self.table)

    def __getitem__(self, key):
        """implementing this method enables getting an item with [] notation
        This function calls your get method.

        Args:
            key (str) : a key which is compareable by <,>,==
        Returns:
            any : the value associated with the key
        Raises:
            KeyError : it raises KeyError because the get function in bst.py raises the error.
        """
        return self.get(key)

    def __setitem__(self, key, val):
        """implementing this method enables setting a key value pair with [] notation
        This function calls your put method.

        Args:
            key (any) : a key which is compareable by <,>,==
            val (any): the value associated with the key
        """
        self.put(key, val)

    def __contains__(self, key):
        """implementing this method enables checking if a key exists with in notaion

        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False
        """
        return self.contains(key)


    def put(self, key, data):
        """Takes a key and data, then stores the key-value pair into a hash
        table based on the hash value of the key.

        If k-v pair is duplicate, the old k-v pair will be replaced by new k-v pair.
        If load factor of hash table is greater than following values, hash table
        doubles its size and stores old data in new one.

        Load factors for:

        Separate Chaining: 1.5
        Linear Probing: 0.75
        Quadratic Probing: 0.75

        Note: Key and data are same string for this lab (i.e, stop words like "the")

        Args:
            key (str): string for key to hash and insert to hash table
            data (str): value of the k-v pair, same string as key in this case

        Returns:
            None
        """
        hkey = hash_string(key, self.table_size)
        if (self.num_items + 1) / self.table_size >= 1.5:
            self.table_size, self.table = enlarge(self.table, self.table_size)
        # Case 1 : Empty slot - insert item
        if self.table[hkey] is None:
            self.table[hkey] = Node(key, data)
        else: # collision
            self.num_collisions += 1
            if self.table[hkey].key == key:
                # self.table[hkey] = Node(key, data)
                self.table[hkey].key = key
                self.table[hkey].val = data
            else:
                temp = self.table[hkey]
                inserted = False
                while temp is not None:
                    if temp.key == key:
                        self.table[hkey].key = key
                        self.table[hkey].val = data
                        inserted = True
                    if temp.next is None:
                        break
                    else:
                        temp = temp.next
                if not inserted:
                    temp.next = Node(key, data)
            self.num_items += 1

    def get(self, key):
        """Returns the value (the item of a key-item pair) from the hash table
        associated with given key. Raises keyerror if not found.

        Args:
            key (str) : key to retrieve k-v pair from

        Returns:
            str : value from given key

        Raises:
            KeyError
        """
        hkey = hash_string(key, self.size)
        if self.table[hkey] is None:
            raise KeyError
        return self.table[hkey].val

    def contains(self, key):
        """Returns true if key is in table, otherwise false.

        Args:
            key (str) : key to check existence in table

        Returns:
            bool : True if key is in table. False if not.
        """
        hkey = hash_string(key, self.size)
        temp = self.table[hkey]
        if self.table[hkey] is None:
            return False
        while temp is not None:
            if temp.key == key:
                return True
            temp = temp.next
        return False

    def remove(self, key):
        """Removes the k-v pair from hash table and returns pair.
        Else raise KeyError if not found.

        Args:
            key (str) : key of k-v pair to be removed

        Returns:
            Node : the k-v pair removed at key's hash location on table

        Raises:
            KeyError: key-item pair not found
        """
        hkey = hash_string(key, self.size)
        temp = self.table[hkey]
        if self.table[hkey] is None:
            raise KeyError
        while temp is not None:
            if temp.key == key:
                return temp
            temp = temp.next
        raise KeyError

    def size(self):
        """Gets the number of key-value pairs in the hash table.

        Args:
            None

        Returns:
            int : the number of k-v pairs in hash table
        """
        return self.num_items

    def load_factor(self):
        """Returns the current load factor of the hash table.

        Args:
            None

        Returns:
            int : the current load factor
        """
        return self.num_items / self.size

    def collisions(self):
        """Returns number of collisions.
        A collision is defined as trying to insert an item into the table at
        a location with an already existing key-item pair. Collisions are not
        incremented when resizing, unless new item insertion is a collision.

        Args:
            None

        Returns:
            int : number of collisions that have occured during insertions
        """
        return self.num_collisions

class HashTableLinear:
    """Hash table that holds key-value pairs with linear probing collision
    handling.

    Attributes:
        size (int) : size/capacity of the table
        num_items (int) : number of k-v pairs currently in table
        num_collisions (int) : number of collisions during insertions
        table (list) : a list of of k-v pairs
    """

    def __init__(self, table_size=11):
        self.size = table_size
        self.num_items = 0
        self.num_collisions = 0
        self.table = [None] * self.size

    def __eq__(self, other):
        return isinstance(other, HashTableSepchain)\
        and (self.size == other.size)\
        and (self.num_collisions == other.num_collisions)\
        and (self.num_items == other.num_items)\
        and (self.table == other.table)

    def __repr__(self):
        return 'HashTableSepchain\
        (size=%s, num_items=%s, num_collisions=%s, table=%s)'\
        % (self.size, self.num_items, self.num_collisions, self.table)


    def put(self, key, data):
        """Takes a key and data, then stores the key-value pair into a hash
        table based on the hash value of the key.

        If k-v pair is duplicate, the old k-v pair will be replaced by new k-v pair.
        If load factor of hash table is greater than following values, hash table
        doubles its size and stores old data in new one.

        Load factors for:

        Separate Chaining: 1.5
        Linear Probing: 0.75
        Quadratic Probing: 0.75

        Note: Key and data are same string for this lab (i.e, stop words like "the")

        Args:
            key (str): string for key to hash and insert to hash table
            data (str): value of the k-v pair, same string as key in this case

        Returns:
            None
        """
        hkey = hash_string(key, self.size)
        # Case 1 : Empty slot - insert item
        if self.table[hkey] is not None:
            self.num_collisions += 1
        self.table[hkey] = Node(key, data)
        # Case 2 : Another item
        # else:
        self.num_items += 1
        if (self.num_items / self.size) >= 1.5:
            self.size, self.table = enlarge(self.table, self.size)

    def get(self, key):
        """Returns the value (the item of a key-item pair) from the hash table
        associated with given key. Raises keyerror if not found.

        Args:
            key (str) : key to retrieve k-v pair from

        Returns:
            str : value from given key

        Raises:
            KeyError
        """
        hkey = hash_string(key, self.size)
        if self.table[hkey].key is None:
            raise KeyError
        return self.table[hkey].val

    def contains(self, key):
        """Returns true if key is in table, otherwise false.

        Args:
            key (str) : key to check existence in table

        Returns:
            bool : True if key is in table. False if not.
        """
        hkey = hash_string(key, self.size)
        temp = self.table[hkey]
        if self.table[hkey] is None:
            return False
        while temp is not None:
            if temp.key == key:
                return True
            temp = temp.next
        return False

    def remove(self, key):
        """Removes the k-v pair from hash table and returns pair.
        Else raise KeyError if not found.

        Args:
            key (str) : key of k-v pair to be removed

        Returns:
            Node : the k-v pair removed at key's hash location on table

        Raises:
            KeyError: key-item pair not found
        """
        hkey = hash_string(key, self.size)
        temp = self.table[hkey]
        if self.table[hkey] is None:
            raise KeyError
        while temp is not None:
            if temp.key == key:
                return temp
            temp = temp.next
        raise KeyError

    def size(self):
        """Gets the number of key-value pairs
        currently stored in the hash table.

        Args:
            None

        Returns:
            int : the number of k-v pairs in hash table
        """
        return self.num_items

    def load_factor(self):
        """Returns the current load factor of the hash table.

        Args:
            None

        Returns:
            int : the current load factor
        """
        return self.num_items / self.size

    def collisions(self):
        """Returns number of collisions.
        A collision is defined as trying to insert an item into the table at
        a location with an already existing key-item pair. Collisions are not
        incremented when resizing, unless new item insertion is a collision.

        Args:
            None

        Returns:
            int : number of collisions that have occured during insertions
        """
        return self.num_collisions

class HashTableQuadratic:
    pass

def hash_string(string, size):
    hash = 0
    for c in string:
        hash = (hash*31 + ord(c)) % size
    return hash

def import_stopwords(filename, hashtable):
    """Imports a file of stop words and stores it into a hashtable object.
    Hashtable can be one of the different collision handling methods:
    separate chaining, linear probing, or quadratic probing

    Args:
        filename (file) : the file of stop words to be stored
        hashtable (HashTableXXX) : one of the different hash table classes

    Returns:
        hashtable : the hashtable with stop words inserted
    """
    with open(filename, newline=" ") as stopfile:
        for word in stopfile:
            hashtable.put(word, word)
            # hkey = hash_string(word, hashtable.size)
            # hashtable.table[hkey] = Node(word, word)
    return hashtable

def enlarge(table, capacity):
    new_cap = 2*capacity + 1
    new_table = [None] * new_cap
    for item in table:
        new_table[item] = table[item]
    return new_cap, new_table