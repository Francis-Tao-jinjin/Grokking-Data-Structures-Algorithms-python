# Definition of a Node class
class Node:
    def __init__(self, val=None):
        self.val = val  # Assign val to the node
        self.next = None  # Initialize the next attribute to None

# Definition of the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    # Function to insert a new node at the beginning of the list
    def insert(self, val):
        new_node = Node(val)  # Create a new node
        new_node.next = self.head  # Set the next attribute of the new node to the current head
        self.head = new_node  # Update the head of the list to the new node

    # Function to insert a new node after a given node
    def insert_after(self, prev_node, val):
        # Check if the given prev_node is None
        if prev_node is None:
            print("The given previous node must be in LinkedList.")
            return
        new_node = Node(val)  # Create a new node
        new_node.next = prev_node.next  # Update the next attribute of the new node to the next node of prev_node
        prev_node.next = new_node  # Set the next attribute of prev_node to the new node

    # Function to delete the first occurrence of a key in the list
    def delete(self, key):
        temp = self.head  # Store head node
        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.val == key:
                self.head = temp.next  # Change head
                temp = None  # Free old head
                return
        # Search for the key to be deleted
        while temp is not None:
            if temp.val == key:
                break
            prev = temp  # Save the previous node
            temp = temp.next  # Move to the next node
        # If key was not present in the list
        if temp == None:
            return
        # Unlink the node from the list
        prev.next = temp.next
        temp = None  # Free the memory

    # Function to search for a key in the list. Returns True if found, otherwise False
    def search(self, key):
        current = self.head  # Initialize current
        while current != None:
            if current.val == key:  # If the key is found, return True
                return True
            current = current.next  # Move to the next node
        return False  # Key not found, return False


# Driver function
if __name__=="__main__":
    llist = LinkedList()  # Create an empty list

    # Insert nodes into the list
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)

    # Search for a key in the list
    print("Search 2:", llist.search(2))  # True

    # Delete a node from the list by key
    llist.delete(2)

    # Check if the key is still present in the list
    print("Search 2:", llist.search(2))  # False
