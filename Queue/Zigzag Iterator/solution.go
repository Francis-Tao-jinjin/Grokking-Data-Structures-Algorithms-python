package main

import (
	"fmt"
)

// Define a Solution struct that uses the Queue data structure.
type Solution struct {
	queue Queue // the Queue struct in the "Simple Queue"
}

// Constructor initializes the Solution struct with values from two integer slices.
func Constructor(v1 []int, v2 []int) Solution {
	// Create a new Queue.
	queue := NewQueue()

	// If v1 is not empty, push it to the Queue.
	if len(v1) > 0 {
		queue.Push(v1)
	}

	// If v2 is not empty, push it to the Queue.
	if len(v2) > 0 {
		queue.Push(v2)
	}

	return Solution{queue}
}

// Next returns the next integer in the queue.
func (s *Solution) Next() int {
	// Get the front element from the queue along with any potential error.
	front, err := s.queue.Front()
	if err != nil {
		// Handle the error appropriately; here, it returns -1 as a placeholder.
		return -1 // Replace with your error handling logic
	}
	iter := front.([]int)

	// Get the first integer from the list.
	value := iter[0]

	// Remove the first integer from the list.
	iter = iter[1:]

	if len(iter) > 0 {
		// If there are more elements in the list, update the queue.
		s.queue.Pop()
		s.queue.Push(iter)
	} else {
		// If the list is empty, remove it from the queue.
		s.queue.Pop()
	}

	return value
}

// HasNext checks if there are more integers in the queue.
func (s *Solution) HasNext() bool {
	return !s.queue.Empty()
}

func main() {
	// Create an instance of Solution and initialize it with integer slices.
	i := Constructor([]int{1, 2}, []int{3, 4, 5, 6})

	// Print the results of calling Next and HasNext methods.
	fmt.Println(i.Next())    // returns 1
	fmt.Println(i.Next())    // returns 3
	fmt.Println(i.Next())    // returns 2
	fmt.Println(i.Next())    // returns 4
	fmt.Println(i.Next())    // returns 5
	fmt.Println(i.Next())    // returns 6
	fmt.Println(i.HasNext()) // returns false
}
