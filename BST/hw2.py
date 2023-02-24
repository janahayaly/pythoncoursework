"""
HW 2: BSTs

Name: Jana Hayaly

PennKey: jhayaly

Number of hours spent on homework: 4

Collaboration is NOT permitted.

In all functions below, the "NotImplementedError" exception is raised, for
you to fill in. The interpreter will not consider the empty code blocks
as syntax errors, but the "NotImplementedError" will be raised if you
call the function. You will replace these raised exceptions with your
code completing the function as described in the docstrings.
"""


class Node:
    def __init__(self, key):
        """
        Construct an instance of the Node class.

        Attributes:
            - self.key: the int representing the key for the node
            - self.left: the left child Node object (initialize to None)
            - self.right: the right child Node object (initialize to None)

        Args:
            key (int): the key for the node
        """
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        """
        Inserts the given key, and raises an Exception if the key already
        exists.

        Args:
            key (int): the key for the node

        Returns:
            None

        Raises:
            Exception: if the key already exists.
        """
        
        if self.key == key:
            raise Exception('key is already in node')
        if self.key > key:
            if self.left == None:
                self.left = Node(key)
            else:
                Node.insert(self.left, key)
        else:
            if self.right == None: 
                self.right = Node(key)
            else:
                Node.insert(self.right, key)
                


    def search(self, key):
        """
        Searches for the given key, and returns the Node the key
        is at, if it exists.

        Args:
            key (int): the key to be inserted

        Returns:
            Node: the node that contains the given key, or None if not found
        """
        
        if self.key == key:
            return self
        else:
            if self.key > key:
                if self.left == None:
                    return None
                else:
                    return Node.search(self.left, key)
            else:
                if self.right == None:
                    return None
                else:
                    return Node.search(self.right, key)


    def __str__(self):
        """
        Defines the string representation of a given Node instance.

        This function is optional and won't be graded, but you may find it
        useful to print Node attributes for debugging.

        Args:
            None

        Returns:
            str: a Node's string representation
        """
        if self == None:
            print("NONE")
        else:
            return str(self.key)


class BST:
    def __init__(self):
        """
        Construct an instance of the BST class. The BST should be initially
        empty.

        Attributes:
            - self.root: root Node of the BST (initialize to None)
            - self.length (initialize to 0)
        """
        self.root = None
        self.length = 0

    def insert(self, key):
        """
        Insert a node to the BST with a given key.

        Wraps the Node insert() function, but should catch the Exception
        raised by Node.insert() if a duplicate key is inserted.

        Remember to increment self.length when an insert is successful.

        Args:
            key (int): the key to insert in the BST

        Returns:
            bool: True if the key is successfully inserted, False if it is
            a duplicate.
        """
        try:
            if self.root == None:
                self.root = Node(key)
            else:
                Node.insert(self.root, key)
            self.length += 1
            return True
        except:
            return False

    def __len__(self):
        """
        The number of elements in the BST.

        Args:
            None

        Return:
            int: the number of elements in the BST
        """
        return self.length

    def search(self, key):
        """
        Searches for the given key, and returns the Node the key
        is at, if it exists.

        Wraps the Node search() function.

        Args:
            key (int): the key to search for in the BST

        Returns:
            Node: the node with the given key if present, None otherwise
        """
        if self.root == None:
            return None
        else:
            return Node.search(self.root, key)

    def __contains__(self, key):
        """
        Check whether the given key is in the BST.

        Hint: use your implemented search function.

        Args:
            key (int): the key to search for

        Returns:
            True if the key is in the BST, False otherwise
        """
        chosen_node = BST.search(self, key)
        if chosen_node == None:
            return False
        else:
            return key == chosen_node.key

    def __iter__(self):
        """
        A generator for iterating over the keys of the tree, in an in-order
        traversal.

        Hint: consider writing a recursive helper function, using yield and
        yield from.

        Args:
            None

        Yields:
            Keys of the BST in-order
        """
        
        gen = BST.__iter_helper__(self, self.root)
        
        yield from gen

    def __iter_helper__(self, curr):

        if curr.left != None:
            yield from BST.__iter_helper__(self, curr.left)

        yield curr.key

        if curr.right != None:
            yield from BST.__iter_helper__(self, curr.right)
        


if __name__ == '__main__':
    """
    Feel free to test your implementation here by running "python3 hw2.py" in
    your terminal.
    """
    
    my_bst = BST()

    print(BST.insert(my_bst, 1))
    print(BST.__len__(my_bst))
    print(BST.insert(my_bst, 3))
    print(BST.__len__(my_bst))
    print(BST.insert(my_bst, 4))
    print(BST.__len__(my_bst))
    print(BST.insert(my_bst, 5))
    print(BST.__len__(my_bst))

    """

    Node.__str__(BST.search(my_bst, 1))
    Node.__str__(BST.search(my_bst, 2))
    Node.__str__(BST.search(my_bst, 4))
    Node.__str__(BST.search(my_bst, 5))  

    print(BST.__contains__(my_bst, 1))
    print(BST.__contains__(my_bst, 2))
    print(BST.__contains__(my_bst, 3))
    print(BST.__contains__(my_bst, 4))
    print(BST.__contains__(my_bst, 5))  
    """

    # print("iter:")
    # print(BST.__iter__(my_bst))
    


    """my_node = Node(2)

    print(Node.insert(my_node, 1)) 
    
    Node.insert(my_node, 1)
    Node.insert(my_node, 5)
    Node.insert(my_node, 0)
    Node.insert(my_node, 3)

    print(Node.search(my_node, 1))"""
"""
    print("node 0: ")
    Node.__str__(Node.search(my_node, 0))
    print("node 1: ")
    Node.__str__(Node.search(my_node, 1))
    print("node 2:")
    Node.__str__(Node.search(my_node, 2))
    print("node 3:")
    Node.__str__(Node.search(my_node, 3))
"""

