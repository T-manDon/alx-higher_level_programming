#!/usr/bin/python3
"""Define singly-linked list."""

# Define the Node class
class Node:
    """Represent singly-linked list node."""

    # Constructor (initializer) for the Node class
    def __init__(self, data, next_node=None):
        """Init new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    # Getter method for the "data" property
    @property
    def data(self):
        """Get/set the data."""
        return self.__data

    # Setter method for the "data" property
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("must be an int")
        self.__data = value

    # Getter method for the "next_node" property
    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return self.__next_node

    # Setter method for the "next_node" property
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

# Define the SinglyLinkedList class
class SinglyLinkedList:
    """Represent a singly-linked list."""

    # Constructor (initializer) for the SinglyLinkedList class
    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    # Method to insert a new Node in a sorted manner
    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    # Method to provide a custom string representation
    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)
