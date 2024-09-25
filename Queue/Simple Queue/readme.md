# Working with Simple Queues

## Operations on Simple Queues
So, we've learned what a Queue is and the key terminologies related to it. We're now ready to roll up our sleeves and start working with Simple Queues. Remember our coffee shop line? Let's think of our Simple Queue in the same way.

The primary operations that we can perform on a Simple Queue are: Enqueue (add an element to the end of the Queue), and Dequeue (remove an element from the front). There's also Peek or Front (get the value of the front item without removing it), and IsEmpty (check if the Queue is empty).

### Enqueue Operation

The Enqueue operation is about adding an element at the rear of the Queue. The step is simple: we take the item we want to add, go to the end of the line (rear of the Queue), and place it there. But wait, how do we know if there's enough space in our Queue to add a new element? Good question! Before we add a new item, we must check if our Queue is already full. If it's full, we can't add a new item - we call this situation Queue Overflow.

### Dequeue Operation

The Dequeue operation is about removing an element from the front of the Queue. So, we go to the front of our Queue, serve the first customer (remove the first element), and adjust our front to point to the next customer. But here too, we need to be careful. Before we remove an item, we must check if there are any items to remove! If the Queue is empty, we can't remove anything - we call this situation Queue Underflow.

### Peek and IsEmpty Operations

Peek (or Front) and IsEmpty are straightforward operations. Peek lets us see the first element in the Queue (like calling the next customer without serving them), and IsEmpty lets us know if our Queue is empty (like checking if there are any customers left to serve).

![Time Complexity of Queue Operations](https://storage.googleapis.com/download/storage/v1/b/designgurus-prod.appspot.com/o/acdcc2d35f1896957760ef400?generation=1697410549023405&alt=media)

### Simple Queue in Action

In this section, we're going to look at some examples of the abovementioned operations and how they work in a program.

But before we jump into coding, let's consider how we're going to structure our Queue. A simple way is to implement a queue using a LinkedList. We can use a Node structure to represent each element of the Queue. Each Node will have a variable to store the data and a Node pointer which will be pointing to the next element of the queue. In the Queue class, we will have two pointers: one to the front Node of the Queue, and one to the rear Node. Here is the description of each element of the queue class:

1. Node Class: This is an inner class used to represent each element in the queue. Each node contains the data and a reference to the next node in the list.

2. Queue Class Attributes:

  - front: A reference to the first node in the queue.
  - rear: A reference to the last node in the queue.
  - size: An integer tracking the number of elements in the queue.

3. Constructor:

  - The constructor initializes an empty queue where both front and rear are set to null, and size is set to 0.

4. Enqueue Operation (enqueue method):

  - This method adds an element to the end of the queue.
  - A new node is created with the given data.
  - If the queue is empty (rear == null), both front and rear point to the new node.
  - If the queue is not empty, the new node is added after rear, and then rear is updated to point to this new node.
  - The size of the queue is incremented.

5. Dequeue Operation (dequeue method):

  - This method removes an element from the front of the queue.
  - If the queue is empty (front == null), the method returns null.
  - The data from the front node is saved.
  - front is updated to point to the next node in the queue.
  - If the queue becomes empty after this operation (front == null), rear is also set to null.
  - The size of the queue is decremented.
  - The method returns the saved data.

6. Peek Operation (peek method):

  - This method returns the data from the front node without removing it.
  - If the queue is empty (front == null), it returns null.
  - Otherwise, it returns the data of the front node.

7. Utility Methods:

  - isEmpty: Checks if the queue is empty (i.e., size == 0).
  - size: Returns the number of elements in the queue.

Here's a program to implement the queue. This implementation of a queue is a classic example of a FIFO (First-In-First-Out) data structure, where elements are added to the rear and removed from the front, ensuring that the order in which elements are added is the order in which they are removed.

Python3
```python
class Node:
    # Node class for storing data and the reference to the next node
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    # Queue class using linked list
    def __init__(self):
        self.front = self.rear = None
        self.size = 0

    def enqueue(self, data):
        # Add an element to the rear of the queue
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            self.size += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        # Remove an element from the front of the queue
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return temp.data

    def peek(self):
        # Get the front element of the queue
        if self.front is None:
            return None
        return self.front.data

    def is_empty(self):
        # Check if the queue is empty
        return self.size == 0

    def get_size(self):
        # Get the number of elements in the queue
        return self.size

# Example usage
if __name__ == "__main__":
    queue = Queue()

    # Enqueue elements
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Display front element
    print("Front element:", queue.peek())
    # Dequeue and display the dequeued element
    print("Dequeued:", queue.dequeue())
    # Display front element again
    print("Front element:", queue.peek())
    # Display the size of the queue
    print("Queue size:", queue.get_size())

```

Java:
```java
class Queue<T> {
    private Node<T> front, rear;
    private int size;

    // Node class for storing data and the reference to the next node
    private static class Node<T> {
        T data;
        Node<T> next;

        Node(T data) {
            this.data = data;
            this.next = null;
        }
    }

    public Queue() {
        front = rear = null;
        size = 0;
    }

    // Add an element to the queue
    public void enqueue(T data) {
        Node<T> newNode = new Node<>(data);
        if (rear == null) {
            front = rear = newNode;
        } else {
            rear.next = newNode;
            rear = newNode;
        }
        size++;
    }

    // Remove an element from the queue
    public T dequeue() {
        if (front == null) {
            return null;
        }
        T data = front.data;
        front = front.next;
        if (front == null) {
            rear = null;
        }
        size--;
        return data;
    }

    // Check the front element of the queue
    public T peek() {
        if (front == null) {
            return null;
        }
        return front.data;
    }

    // Check if the queue is empty
    public boolean isEmpty() {
        return size == 0;
    }

    // Get the size of the queue
    public int size() {
        return size;
    }
}

// Example usage
public class Solution {
    public static void main(String[] args) {
        Queue<Integer> queue = new Queue<>();

        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);

        System.out.println("Front element: " + queue.peek());
        System.out.println("Dequeued: " + queue.dequeue());
        System.out.println("Front element: " + queue.peek());
        System.out.println("Queue size: " + queue.size());
    }
}
```

Golang:
```golang
package main

import "fmt"

// Node struct for storing data and the reference to the next node
type Node struct {
    Data interface{}
    Next *Node
}

// Queue struct using linked list
type Queue struct {
    front *Node
    rear  *Node
    size  int
}

// NewQueue creates a new Queue instance
func NewQueue() *Queue {
    return &Queue{nil, nil, 0}
}

// Enqueue adds an element to the rear of the queue
func (q *Queue) Enqueue(data interface{}) {
    newNode := &Node{Data: data}
    if q.rear == nil {
        q.front = newNode
        q.rear = newNode
    } else {
        q.rear.Next = newNode
        q.rear = newNode
    }
    q.size++
}

// Dequeue removes an element from the front of the queue
func (q *Queue) Dequeue() interface{} {
    if q.front == nil {
        return nil
    }
    temp := q.front
    q.front = q.front.Next
    if q.front == nil {
        q.rear = nil
    }
    q.size--
    return temp.Data
}

// Peek gets the front element of the queue
func (q *Queue) Peek() interface{} {
    if q.front == nil {
        return nil
    }
    return q.front.Data
}

// IsEmpty checks if the queue is empty
func (q *Queue) IsEmpty() bool {
    return q.size == 0
}

// Size returns the number of elements in the queue
func (q *Queue) Size() int {
    return q.size
}

// Example usage
func main() {
    queue := NewQueue()

    // Enqueue elements
    queue.Enqueue(1)
    queue.Enqueue(2)
    queue.Enqueue(3)

    // Display front element
    fmt.Println("Front element:", queue.Peek())
    // Dequeue and display the dequeued element
    fmt.Println("Dequeued:", queue.Dequeue())
    // Display front element again
    fmt.Println("Front element:", queue.Peek())
    // Display the size of the queue
    fmt.Println("Queue size:", queue.Size())
}
```