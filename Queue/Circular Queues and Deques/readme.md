# Diving Deeper – Circular Queues and Deques

Now that we've got a solid understanding of Simple Queues, it's time to take the plunge and dive deeper into the world of Queues. In this module, we'll explore two other types of Queues – Circular Queues and Deques (Double Ended Queues).

## Understanding Circular Queues

### The Concept of a Circular Queue
In a Circular Queue, the last element points back to the first element making a circular link. We can visualize it as a circle where we remove elements from one end and add elements at the other end, and it goes on in a cycle.

### Operations on a Circular Queue
We will use an array to implement circular queue.

The operations on a Circular Queue are similar to those of a Simple Queue – Enqueue, Dequeue, Peek, and IsEmpty. But there's a twist in the way we handle these operations due to the circular nature of the Queue.

When we Enqueue (add an element), we add it at the rear and increment the rear pointer. But if we reach the end of our array while enqueueing, instead of declaring an Overflow, we wrap around and continue from the front of the array, as long as there is space.

Similarly, when we Dequeue (remove an element), we remove it from the front and increment the front pointer. But if we reach the end of the array while dequeuing, we wrap around and continue from the start of the array.

Python3:
```python
class CircularQueue:
    # Constructor to initialize the queue
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    # Function to insert an element in the queue
    def enqueue(self, element):
        if ((self.front == 0 and self.rear == self.size - 1) or
                (self.rear == (self.front - 1) % (self.size - 1))):
            print("Queue is Full")
        elif self.front == -1:  # Insert First Element
            self.front = self.rear = 0
            self.queue[self.rear] = element
        elif self.rear == self.size - 1 and self.front != 0:
            self.rear = 0
            self.queue[self.rear] = element
        else:
            self.rear = (self.rear + 1)
            self.queue[self.rear] = element

    # Function to delete an element from the queue
    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return None

        data = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1
        return data

    # Function to display the elements of the queue
    def displayQueue(self):
        if self.front == -1:
            print("Queue is Empty")
            return
        print("Elements in the Circular Queue are: ")
        if self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
        print()


# Main method to test the CircularQueue class
if __name__ == "__main__":
    q = CircularQueue(5)

    # Inserting elements in the queue
    q.enqueue(14)
    q.enqueue(22)
    q.enqueue(13)
    q.enqueue(-6)

    # Display elements present in the queue
    q.displayQueue()

    # Deleting elements from the queue
    print("Deleted value =", q.dequeue())
    print("Deleted value =", q.dequeue())

    q.displayQueue()

    q.enqueue(9)
    q.enqueue(20)
    q.enqueue(5)

    q.displayQueue()

    q.enqueue(20)
```

Java:
```java
class CircularQueue {
    private int[] queue;
    private int size;
    private int front;
    private int rear;

    // Constructor to initialize the queue
    public CircularQueue(int size) {
        this.size = size;
        queue = new int[this.size];
        front = -1;
        rear = -1;
    }

    // Function to insert an element in the queue
    public void enqueue(int element) {
        if ((front == 0 && rear == size - 1) || (rear == (front - 1) % (size - 1))) {
            System.out.println("Queue is Full");
        } else if (front == -1) { // Insert First Element
            front = 0;
            rear = 0;
            queue[rear] = element;
        } else if (rear == size - 1 && front != 0) {
            rear = 0;
            queue[rear] = element;
        } else {
            rear = (rear + 1);
            queue[rear] = element;
        }
    }

    // Function to delete an element from the queue
    public int dequeue() {
        if (front == -1) {
            System.out.println("Queue is Empty");
            return Integer.MIN_VALUE;
        }

        int data = queue[front];
        queue[front] = -1;
        if (front == rear) {
            front = -1;
            rear = -1;
        } else if (front == size - 1) {
            front = 0;
        } else {
            front++;
        }
        return data;
    }

    // Function to display the elements of the queue
    public void displayQueue() {
        if (front == -1) {
            System.out.println("Queue is Empty");
            return;
        }
        System.out.println("Elements in the Circular Queue are: ");
        if (rear >= front) {
            for (int i = front; i <= rear; i++) {
                System.out.print(queue[i] + " ");
            }
        } else {
            for (int i = front; i < size; i++) {
                System.out.print(queue[i] + " ");
            }
            for (int i = 0; i <= rear; i++) {
                System.out.print(queue[i] + " ");
            }
        }
        System.out.println();
    }
}

public class Solution {
    // Main method to test the CircularQueue class
    public static void main(String[] args) {
        CircularQueue q = new CircularQueue(5);

        // Inserting elements in the queue
        q.enqueue(14);
        q.enqueue(22);
        q.enqueue(13);
        q.enqueue(-6);

        // Display elements present in the queue
        q.displayQueue();

        // Deleting elements from the queue
        System.out.println("Deleted value = " + q.dequeue());
        System.out.println("Deleted value = " + q.dequeue());

        q.displayQueue();

        q.enqueue(9);
        q.enqueue(20);
        q.enqueue(5);

        q.displayQueue();

        q.enqueue(20);
    }
}
```

Golang:
```golang
package main

import (
	"fmt"
	"math"
)

type CircularQueue struct {
	queue       []int
	front, rear int
	size        int
}

// Constructor to initialize the queue
func NewCircularQueue(size int) *CircularQueue {
	return &CircularQueue{
		queue: make([]int, size),
		front: -1,
		rear:  -1,
		size:  size,
	}
}

// Function to insert an element in the queue
func (cq *CircularQueue) Enqueue(element int) {
	if (cq.front == 0 && cq.rear == cq.size-1) || (cq.rear == (cq.front-1)%(cq.size-1)) {
		fmt.Println("Queue is Full")
	} else if cq.front == -1 { // Insert First Element
		cq.front, cq.rear = 0, 0
		cq.queue[cq.rear] = element
	} else if cq.rear == cq.size-1 && cq.front != 0 {
		cq.rear = 0
		cq.queue[cq.rear] = element
	} else {
		cq.rear = (cq.rear + 1) % cq.size
		cq.queue[cq.rear] = element
	}
}

// Function to delete an element from the queue
func (cq *CircularQueue) Dequeue() int {
	if cq.front == -1 {
		fmt.Println("Queue is Empty")
		return math.MinInt64
	}

	data := cq.queue[cq.front]
	if cq.front == cq.rear {
		cq.front, cq.rear = -1, -1
	} else {
		cq.front = (cq.front + 1) % cq.size
	}
	return data
}

// Function to display the elements of the queue
func (cq *CircularQueue) DisplayQueue() {
	if cq.front == -1 {
		fmt.Println("Queue is Empty")
		return
	}
	fmt.Print("Elements in the Circular Queue are: ")
	if cq.rear >= cq.front {
		for i := cq.front; i <= cq.rear; i++ {
			fmt.Print(cq.queue[i], " ")
		}
	} else {
		for i := cq.front; i < cq.size; i++ {
			fmt.Print(cq.queue[i], " ")
		}
		for i := 0; i <= cq.rear; i++ {
			fmt.Print(cq.queue[i], " ")
		}
	}
	fmt.Println()
}

// Main method to test the CircularQueue class
func main() {
	q := NewCircularQueue(5)

	// Inserting elements in the queue
	q.Enqueue(14)
	q.Enqueue(22)
	q.Enqueue(13)
	q.Enqueue(-6)

	// Display elements present in the queue
	q.DisplayQueue()

	// Deleting elements from the queue
	fmt.Println("Deleted value =", q.Dequeue())
	fmt.Println("Deleted value =", q.Dequeue())

	q.DisplayQueue()

	q.Enqueue(9)
	q.Enqueue(20)
	q.Enqueue(5)

	q.DisplayQueue()

	q.Enqueue(20)
}
```

### Common Mistakes and How to Avoid Them
While working with Queues, it's easy to make a few common mistakes. The first mistake is forgetting to check for Queue Overflow and Underflow conditions. Always remember to check if the Queue is full before enqueueing and if it's empty before dequeuing. This will save you from unexpected errors.

Another common mistake is mixing up the front and rear pointers. Keep in mind that we always add items to the rear and remove them from the front.

## Introduction to Deques (Double-Ended Queues)

### The Flexibility of Deques

The name Deque is short for Double Ended Queue, and as the name suggests, it's a Queue where we can add or remove elements from both ends.

Think about a library line where you can borrow books from one end and return books at the other end. The Deque is flexible and allows us to work from both ends!

### Operations on Deques

The operations on Deques are a bit different from our regular Queues. We have four main operations in Deques:

- InsertFront: add an element at the front of the Deque.
- InsertRear: add an element at the rear of the Deque.
- DeleteFront: remove an element from the front of the Deque.
- DeleteRear: remove an element from the rear of the Deque.

This flexibility of Deques can be really useful in certain scenarios and can give you an extra edge when tackling complex problems.

