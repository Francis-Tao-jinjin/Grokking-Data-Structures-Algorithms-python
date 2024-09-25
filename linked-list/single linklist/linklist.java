// Class to represent a ListNode in the linked list
class ListNode {
    int val; // Data of the node
    ListNode next; // Reference to the next node in the list
    // Constructor to initialize the node with val and set the next reference to null
    ListNode(int d) { val = d; next = null; }
}

// Class to represent a Singly Linked List and perform various operations
class Linklist {
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
      Linklist list = new Linklist(); // Create an empty list

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
