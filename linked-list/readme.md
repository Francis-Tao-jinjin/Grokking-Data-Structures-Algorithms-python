# Introduction to LinkedList

Let's discuss one of the fundamental and most used data structures – the Linked List! This chapter aims to unravel the essence of linked lists, their variations, practical applications, and how to implement them across various programming languages.

## Section 1: What is a Linked List?

A linked list is a linear data structure where elements are stored in nodes, and each node points to the next one in the sequence, forming a chain-like structure.

### 1.1 Node Structure

- Value: The data element stored in the node.
- Next: A reference to the next node in the list.

### 1.2 Why Linked Lists?
- Dynamic Size: Easily grows and shrinks in size.
- Efficient Insertions/Deletions: Quick at the beginning and middle of the list.

## Section 2: Types of Linked Lists
In the realm of linked lists, there are several types, each serving a unique purpose.

### 2.1 Singly Linked List
- Definition: Each node points to the next node.
- Use Case: A music playlist where each song plays after the previous one.

### 2.2 Doubly Linked List
- Definition: Each node has pointers to both the next and the previous nodes.
- Use Case: A web browser's history, enabling forward and backward navigation.

### 2.3 Circular Linked List
- Definition: The last node in the list points back to the first node.
- Use Case: A multiplayer board game where play returns to the first player after the last.

## Section 3: Practical Implementations
### 3.1 Linked List in Java
Java offers a LinkedList class in its standard library.

```java
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<>();
        list.add("Node1");
        list.add("Node2");
        list.add("Node3");
        System.out.println(list);
    }
}
```

### 3.2 Linked List in Python3
Python provides a list data type which can be used as a linked list due to its dynamic nature.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

head = Node("Node1")
head.next = Node("Node2")
head.next.next = Node("Node3")

current = head
while current:
    print(current.data)
    current = current.next
```

### 3.3 Linked List in C++
In C++, linked lists can be manually created using structures and pointers.

```cpp
#include <iostream>

struct Node {
    std::string data;
    Node* next;
};

int main() {
    Node* head = new Node{"Node1"};
    head->next = new Node{"Node2"};
    head->next->next = new Node{"Node3"};

    Node* current = head;
    while (current) {
        std::cout << current->data << std::endl;
        current = current->next;
    }
}
```

### 3.4 Linked List in JavaScript
In JavaScript, we can create a linked list using objects and references.

```js
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

const head = new Node("Node1");
head.next = new Node("Node2");
head.next.next = new Node("Node3");

let current = head;
while (current) {
    console.log(current.data);
    current = current.next;
}
```

## Operations in Singly Linked List
In a singly linked list, each element (known as a node) contains a data value and a reference (or link) to the next node in the sequence. Given this basic structure, let's explore some common operations:

### 1. Insert
Insertion in a singly linked list can be of three types:

- At the Beginning - O(1): Add a new node before the current head of the list.
- At the End - O(n): Traverse the list to the last node and add the new node after it.
- After a Given Node - O(n): Traverse the list to the desired node and insert the new node after it.

### 2. Delete
To delete a node:

- From the Beginning - O(1): Set the second node as the new head.
- From the End - O(n): Traverse the list and remove the reference to the last node.
- A Given Node - O(n): Traverse to the node before the one to delete, then remove the reference to the node-to-delete.

### 3. Search - O(n)
Traverse the list from the head, comparing each node's data with the search value until a match is found or the end of the list is reached.

Now, let's write the code for these operations.

Python3:
```python
# Definition of a Node class
# class Node:
#     def __init__(self, val=None):
#         self.val = val  # Assign val to the node
#         self.next = None  # Initialize the next attribute to None

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
```

Java:
```java
// Class to represent a ListNode in the linked list
// class ListNode {
//     int val; // Data of the node
//     ListNode next; // Reference to the next node in the list
//     // Constructor to initialize the node with val and set the next reference to null
//     ListNode(int d) { val = d; next = null; }
// }

// Class to represent a Singly Linked List and perform various operations
class Solution {
    ListNode head; // head of the list, initially null

    // Inserts a new ListNode at the front of the list.
    void insert(int val) {
        ListNode newNode = new ListNode(val); // Create a new node with the given val
        newNode.next = head; // Set the next reference of the new node to the current head
        head = newNode; // Update the head of the list to the new node
    }

    // Inserts a new node after the given prev_node.
    void insertAfter(ListNode prev_node, int val) {
        // Check if the given prev_node is null
        if (prev_node == null) {
            System.out.println("The given previous node cannot be null");
            return;
        }
        ListNode newNode = new ListNode(val); // Create a new node with the given val
        newNode.next = prev_node.next; // Set the next reference of the new node to the next node of prev_node
        prev_node.next = newNode; // Update the next reference of prev_node to the new node
    }

    // Deletes the first occurrence of the specified key in the list
    void delete(int key) {
        ListNode temp = head, prev = null; // Initialize temp to head and prev to null
        // Check if head node itself holds the key to be deleted
        if (temp != null && temp.val == key) {
            head = temp.next; // Update the head to the next node
            return;
        }
        // Search for the key to be deleted
        while (temp != null && temp.val != key) {
            prev = temp; // Update prev to the current node
            temp = temp.next; // Move to the next node
        }
        // If key was not present in the list
        if (temp == null) return;
        // Unlink the node from the list
        prev.next = temp.next;
    }

    // Searches for the key in the linked list and returns true if found, otherwise false
    boolean search(int key) {
        ListNode current = head; // Initialize current to head
        while (current != null) {
            if (current.val == key) // If the key is found, return true
                return true;
            current = current.next; // Move to the next node
        }
        return false; // Key not found, return false
    }
    
    // Main method to test the linked list operations
    public static void main(String[] args) {
        Solution list = new Solution(); // Create an empty list

        // Insert nodes into the list
        list.insert(1);
        list.insert(2);
        list.insert(3);

        // Search for a key in the list
        System.out.println("Search 2: " + list.search(2)); // true

        // Delete a node from the list by key
        list.delete(2);

        // Check if the key is still present in the list
        System.out.println("Search 2: " + list.search(2)); // false
    }
}
```

Golang:
```golang
package main

import "fmt"

// ListNode struct to represent a ListNode in the linked list
// type ListNode struct {
// 	Val int   // Data of the node
// 	Next *ListNode // Reference to the Next node in the list
// }

// Solution struct to represent a Singly Linked List and perform various operations
type Solution struct {
	head *ListNode // head of the list, initially nil
}

// Inserts a new ListNode at the front of the list.
func (s *Solution) insert(Val int) {
	newNode := &ListNode{Val: Val} // Create a new node with the given Val
	newNode.Next = s.head       // Set the Next reference of the new node to the current head
	s.head = newNode            // Update the head of the list to the new node
}

// Inserts a new node after the given prevNode.
func (s *Solution) insertAfter(prevNode *ListNode, Val int) {
	// Check if the given prevNode is nil
	if prevNode == nil {
		fmt.Println("The given previous node cannot be nil")
		return
	}
	newNode := &ListNode{Val: Val} // Create a new node with the given Val
	newNode.Next = prevNode.Next // Set the Next reference of the new node to the Next node of prevNode
	prevNode.Next = newNode     // Update the Next reference of prevNode to the new node
}

// Deletes the first occurrence of the specified key in the list
func (s *Solution) delete(key int) {
	temp := s.head
	var prev *ListNode // Initialize temp to head and prev to nil

	// Check if head node itself holds the key to be deleted
	if temp != nil && temp.Val == key {
		s.head = temp.Next // Update the head to the Next node
		return
	}

	// Search for the key to be deleted
	for temp != nil && temp.Val != key {
		prev = temp     // Update prev to the current node
		temp = temp.Next // Move to the Next node
	}

	// If key was not present in the list
	if temp == nil {
		return
	}

	// Unlink the node from the list
	prev.Next = temp.Next
}

// Searches for the key in the linked list and returns true if found, otherwise false
func (s *Solution) search(key int) bool {
	current := s.head // Initialize current to head

	for current != nil {
		if current.Val == key { // If the key is found, return true
			return true
		}
		current = current.Next // Move to the Next node
	}

	// Key not found, return false
	return false
}

func main() {
	list := &Solution{} // Create an empty list

	// Insert nodes into the list
	list.insert(1)
	list.insert(2)
	list.insert(3)

	// Search for a key in the list
	fmt.Println("Search 2:", list.search(2)) // true

	// Delete a node from the list by key
	list.delete(2)

	// Check if the key is still present in the list
	fmt.Println("Search 2:", list.search(2)) // false
}
```

## [Dobuly Linked List](./doubly%20linklist/)