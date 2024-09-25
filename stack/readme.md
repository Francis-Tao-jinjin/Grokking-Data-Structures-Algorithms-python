# Introduction to Stack

Stack is a linear data structure that operates on the principle of Last-In, First-Out (LIFO), meaning the most recently added element is the first one to be removed.

Imagine you have a pile of books that you plan to read. You keep adding books to the top of the pile. When you're ready to start reading, you take a book from the top of the pile. The last book you added to the pile is the first one you read. That's LIFO - the principle that stack data structures operate on.

What makes stacks so unique is their simplicity and elegance. Despite being straightforward, they can be incredibly powerful when used in the right way.

## The LIFO Principle

As mentioned earlier, stacks in data structures operate on the Last-In, First-Out (LIFO) principle. This means that the last item added to the stack is the first one that gets taken out.

The LIFO principle is the heart of stack data structures. It governs how we add and remove elements, making stack operations predictable and consistent. With that, let's explore the primary operations that you can perform on a stack.

There are four key operations that you can perform on a stack:

1. Push: This is how we add an element to the stack. The element is always added to the top.

2. Pop: This is the removal of an element from the stack. The element removed is always from the top.

3. Peek (or Top): This operation allows us to see the element on the top of the stack without removing it.

4. IsEmpty: This operation checks if the stack is empty.

## Use Cases of Stacks

Before diving into technicalities, let's familiarize ourselves with stacks in our daily lives. Stacks are everywhere around us, even if we might not notice them. Here are some examples to help you relate:

1. Web Browser History: Every time you visit a new webpage, it's added to the top of your history stack. When you hit the back button, you're "popping" pages off the top of the stack.

2. Undo Function in Software Applications: The undo function in software applications uses a stack to remember actions. The most recent action is on top and will be the first one undone.

3. Expression Evaluation: Stacks are used to evaluate expressions (e.g., converting infix to postfix notation).

4. Function Call Management: Most programming languages use a call stack to manage function calls and returns.

Looking at these examples, it's clear that stacks are not just a theoretical concept, but a practical one that we use unconsciously in our day-to-day life. With this understanding, let's dive deeper into the operations that define stacks in data structures.

Let's see the stack in action in the next section.


# Operations on Stack
This chapter aims to demystify the main operations involved in manipulating a stack: push, pop, peek, and isEmpty. We will examine these operations closely, detailing their functionality, providing coding examples, and highlighting their importance in problem-solving.

## Push Operation

Let's start with the push operation. As we've previously learned, push adds a new element to the top of the stack. Think of it like placing a new dish on top of a pile in your sink - the new dish (our data) is added to the top of the pile (our stack).

In programming, the push operation usually involves a few steps. First, we check if there's room to add a new element (we'll discuss this in more detail when we talk about stack overflow). If there's room, we add the new element to the top of the stack.

## Pop Operation

Next, we have the pop operation, which removes the topmost element of the stack. It's like removing the top dish from our pile in the sink.

In code, popping an element from a stack is usually done in two parts. First, we check if there are any elements to remove (we'll look at this more when we discuss stack underflow). If there are elements, we remove the top one.

![Stack operations and their time complexities](https://storage.googleapis.com/download/storage/v1/b/designgurus-prod.appspot.com/o/d13936bcef323d4cc44c2ff00?generation=1697346165687514&alt=media)

## Peek or Top Operation
The peek or top operation is slightly different. Instead of adding or removing an element, this operation allows us to look at the top element of the stack without removing it. It's like looking at the top dish in our sink pile without touching it.

This operation can be handy when you need to know what's on top of your stack, but you don't want to change anything. It's a read-only operation.

## IsEmpty Operation
Finally, the isEmpty operation checks if the stack is empty. This operation is essential for preventing errors when popping an element from an empty stack (known as stack underflow).

An empty stack will return true when the isEmpty operation is performed, while a stack with one or more elements will return false.

## Putting it All Together
Knowing how each of these operations works is crucial. But, what's more important is knowing how to use them together to solve problems. Here's a brief coding example to show how these operations can be used together.

Python3:
```Python
class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack.
        self.stack = []

    def isEmpty(self):
        # Check if the stack is empty by comparing it to an empty list.
        return self.stack == []

    def push(self, data):
        # Add the given data to the top of the stack (end of the list).
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            # If the stack is empty, return a message indicating so.
            return 'Stack is empty'
        # Remove and return the top element from the stack (last item in the list).
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            # If the stack is empty, return a message indicating so.
            return 'Stack is empty'
        # Return the top element from the stack without removing it.
        return self.stack[-1]
```

Java:
```java
import java.util.Stack;
import java.util.EmptyStackException;

// Class MyStack, a generic class to implement a stack data structure.
public class MyStack<T> {
    // A Stack object to store the elements.
    private Stack<T> stack = new Stack<>();

    // Method to check if the stack is empty.
    public boolean isEmpty() {
        return stack.empty(); // Returns true if the stack is empty, false otherwise.
    }

    // Method to add an element to the top of the stack.
    public void push(T data) {
        stack.push(data); // Adds 'data' to the top of the stack.
    }

    // Method to remove and return the top element of the stack.
    public T pop() {
        if (isEmpty()) {
            throw new EmptyStackException(); // Throws an exception if the stack is empty.
        }
        return stack.pop(); // Returns and removes the top element of the stack.
    }

    // Method to return the top element of the stack without removing it.
    public T peek() {
        if (isEmpty()) {
            throw new EmptyStackException(); // Throws an exception if the stack is empty.
        }
        return stack.peek(); // Returns the top element of the stack without removing it.
    }
}
```

Golang:
```go
package main

import (
    "container/list" // Import the container/list package for using the doubly-linked list.
    "fmt"
)

// MyStack is a generic stack data structure.
type MyStack[T any] struct {
    stack list.List // Create a list (doubly-linked list) to store stack elements.
}

// IsEmpty checks if the stack is empty.
func (s *MyStack[T]) IsEmpty() bool {
    return s.stack.Len() == 0 // Check if the length of the list is 0 to determine if the stack is empty.
}

// Push adds an element to the top of the stack.
func (s *MyStack[T]) Push(data T) {
    s.stack.PushBack(data) // Add the element to the back of the list, representing the top of the stack.
}

// Pop removes and returns the top element from the stack.
func (s *MyStack[T]) Pop() (T, error) {
    if s.IsEmpty() {
        return nil, fmt.Errorf("EmptyStackException") // Return an error if the stack is empty.
    }
    back := s.stack.Back() // Get a reference to the back (top) element of the list.
    s.stack.Remove(back)  // Remove the top element from the list.
    return back.Value.(T), nil // Return the value of the top element as type T.
}

// Peek returns the top element of the stack without removing it.
func (s *MyStack[T]) Peek() (T, error) {
    if s.IsEmpty() {
        return nil, fmt.Errorf("EmptyStackException") // Return an error if the stack is empty.
    }
    back := s.stack.Back() // Get a reference to the back (top) element of the list.
    return back.Value.(T), nil // Return the value of the top element as type T without removing it.
}
```

## Dealing with Stack Overflow and Underflow
As we discussed earlier, stack overflow and underflow are two situations you might encounter when working with stacks. Stack overflow occurs when you try to push an element onto a stack that's already full, while stack underflow occurs when you try to pop an element from an empty stack.

Handling these situations properly is crucial to preventing runtime errors and ensuring that your code runs smoothly. Depending on the programming language and the specific implementation of the stack, you might have different ways of handling these situations. It's always a good idea to check for stack overflow and underflow before performing push and pop operations.

## Stack Implementation Using Linked List

An alternative way of implementing a stack is by using a linked list. This method can overcome the size limitation issue present in the array implementation. The code will look something like this:

Python3
```Python
class Stack:
    class Node:
        def __init__(self, data):
            self.data = data  # Store the data in this node
            self.next = None  # Initialize the next node as None

    def __init__(self):
        self.top = None  # Initialize the top of the stack as None

    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")  # Raise exception if the stack is empty
        item = self.top.data  # Store the top item's data
        self.top = self.top.next  # Update the top to be the next node
        return item  # Return the popped item

    def push(self, item):
        t = self.Node(item)  # Create a new node with the provided data
        t.next = self.top  # Set the next of this new node to be the current top
        self.top = t  # Update the top to be the new node

    def peek(self):
        if self.top is None:
            raise IndexError("peek from empty stack")  # Raise exception if the stack is empty
        return self.top.data  # Return the top item's data

    def is_empty(self):
        return self.top is None  # Return True if the stack is empty, False otherwise
```

Java:
```java
import java.util.EmptyStackException;

public class Stack<T> {
    // Private inner class representing a Node in the stack
    private static class Node<T> {
        private T data;         // Data stored in the node
        private Node<T> next;   // Reference to the next node in the stack

        // Constructor to create a new node with the given data
        private Node(T data) {
            this.data = data;
        }
    }

    private Node<T> top;  // Reference to the top node of the stack

    // Pop operation: Removes and returns the top element of the stack
    public T pop() {
        // Check if the stack is empty
        if (top == null) {
            throw new EmptyStackException(); // Throw an exception if it's empty
        }
        T item = top.data;  // Get the data from the top node
        top = top.next;     // Move the top reference to the next node
        return item;        // Return the removed item
    }

    // Push operation: Pushes a new item onto the top of the stack
    public void push(T item) {
        Node<T> t = new Node<T>(item);  // Create a new node with the given data
        t.next = top;                   // Set the new node's next reference to the current top
        top = t;                        // Update the top reference to the new node
    }

    // Peek operation: Returns the top element of the stack without removing it
    public T peek() {
        // Check if the stack is empty
        if (top == null) {
            throw new EmptyStackException(); // Throw an exception if it's empty
        }
        return top.data;  // Return the data of the top node
    }

    // Check if the stack is empty
    public boolean isEmpty() {
        return top == null;
    }
}
```

Golang
```Golang
import (
    "errors"
)

// Solution represents a stack data structure.
type Solution struct {
    top *Node // Pointer to the top node of the stack
}

// Node represents an element in the stack.
type Node struct {
    data interface{} // Data stored in the node
    next *Node      // Pointer to the next node in the stack
}

// Pop removes and returns the top element from the stack.
// It raises an error if the stack is empty.
func (s *Solution) Pop() interface{} {
    if s.top == nil {
        panic(errors.New("EmptyStackException")) // Raise an error if the stack is empty
    }
    item := s.top.data // Get the data of the top node
    s.top = s.top.next // Move the top pointer to the next node
    return item
}

// Push adds a new element to the top of the stack.
func (s *Solution) Push(item interface{}) {
    t := &Node{data: item} // Create a new node with the given data
    t.next = s.top        // Set the next pointer of the new node to the current top node
    s.top = t             // Update the top pointer to the new node
}

// Peek returns the data of the top element without removing it.
// It raises an error if the stack is empty.
func (s *Solution) Peek() interface{} {
    if s.top == nil {
        panic(errors.New("EmptyStackException")) // Raise an error if the stack is empty
    }
    return s.top.data // Return the data of the top node
}

// IsEmpty checks if the stack is empty.
func (s *Solution) IsEmpty() bool {
    return s.top == nil // The stack is empty if the top pointer is nil
}
```