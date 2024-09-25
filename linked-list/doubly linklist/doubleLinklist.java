class DLNode {
    int val;
    DLNode prev;
    DLNode next;

    // Constructor to initialize a DLNode with a given value.
    DLNode(int d) {
        val = d;
        prev = next = null;  // Initialize previous and next pointers to null.
    }
}

public class doubleLinklist {
  DLNode head;

    // Inserts a new DLNode at the front of the list.
    void insert(int val) {
        DLNode newNode = new DLNode(val);  // Create a new DLNode with the given value.
        newNode.next = head;
        if (head != null)
            head.prev = newNode;
        head = newNode;  // Update the head to the new DLNode.
    }

    // Inserts a new node after the given prev_node.
    void insertAfter(DLNode prev_node, int val) {
        if (prev_node == null) {
            System.out.println("The given previous node cannot be null");  // Check if the previous node is null.
            return;
        }
        DLNode newNode = new DLNode(val);  // Create a new DLNode with the given value.
        newNode.next = prev_node.next;
        prev_node.next = newNode;
        newNode.prev = prev_node;
        if (newNode.next != null)
            newNode.next.prev = newNode;
    }

    // Deletes the node with the given val.
    void delete(int key) {
        DLNode temp = head;
        while (temp != null) {
            if (temp.val == key) {
                if (temp.prev != null)
                    temp.prev.next = temp.next;  // Adjust pointers to remove the DLNode.
                else
                    head = temp.next;
                if (temp.next != null)
                    temp.next.prev = temp.prev;
                return;
            }
            temp = temp.next;
        }
    }

    // Searches for the node with the given val.
    boolean search(int key) {
        DLNode current = head;
        while (current != null) {
            if (current.val == key)
                return true;  // Return true if the key is found in the list.
            current = current.next;
        }
        return false;  // Return false if the key is not found in the list.
    }

    public static void main(String[] args) {
        doubleLinklist dll = new doubleLinklist();
        dll.insert(1);
        dll.insert(2);
        dll.insert(3);

        System.out.println("Search 2: " + dll.search(2));  // true
        dll.delete(2);
        System.out.println("Search 2: " + dll.search(2));  // false
    }
}
