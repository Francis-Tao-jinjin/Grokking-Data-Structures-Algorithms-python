package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

type Solution struct{}

// Function to merge two sorted linked lists
func (s *Solution) mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	// Initialize a dummy node and a current pointer
	dummy := &ListNode{Val: -1}
	current := dummy

	// Traverse through both lists until one is exhausted
	for l1 != nil && l2 != nil {
		// Compare nodes and append the smaller one to current
		if l1.Val < l2.Val {
			current.Next = l1
			l1 = l1.Next
		} else {
			current.Next = l2
			l2 = l2.Next
		}
		current = current.Next
	}

	// Append the remaining nodes from the non-empty list
	if l1 != nil {
		current.Next = l1
	} else {
		current.Next = l2
	}

	// Return the merged sorted list
	return dummy.Next
}

func main() {
	solution := &Solution{}

	// Create the first example ListNode instances
	node1 := &ListNode{Val: 1}
	node2 := &ListNode{Val: 2}
	node3 := &ListNode{Val: 3}

	node1.Next = node2
	node2.Next = node3
	node3.Next = nil

	list1 := &ListNode{Val: 1}
	list2 := &ListNode{Val: 4}

	list1.Next = list2
	list2.Next = nil

	// Call mergeTwoLists method and print the result
	result := solution.mergeTwoLists(node1, list1)
	for result != nil {
		fmt.Print(result.Val, " ")
		result = result.Next
	}
}
