# Binary Search Tree (BST)

## Introduction to Binary Search Tree (BST)
A Binary Search Tree (BST) is a fundamental data structure that organizes elements in a hierarchical manner, allowing for efficient searching, insertion, deletion, and traversal operations. In this section, we will explore the characteristics of a BST, its benefits, applications, ADT operations, time and space complexity, as well as potential issues and solutions.

### Definition and Characteristics of BST
A Binary Search Tree is a binary tree in which each node has at most two children, referred to as the left child and the right child. The BST follows a specific property: for any given node, all nodes in its left subtree have values less than or equal to the node's value, and all nodes in its right subtree have values greater than the node's value.

#### Example:
Consider the following BST:
![Binary Search Tree](https://www.designgurus.io/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fdownload%2Fstorage%2Fv1%2Fb%2Fdesigngurus-prod.appspot.com%2Fo%2F377a282cee94ba3ae92f46900%3Fgeneration%3D1693327695857313%26alt%3Dmedia&w=1920&q=75)

In this example, the tree satisfies the BST property since, for each node, all nodes in its left subtree have values less than the node's value, and all nodes in its right subtree have values greater than the node's value.

### Benefits and Applications of BST
BSTs provide efficient searching operations due to their hierarchical structure and the BST property. The search can be performed in O(log n) time in a balanced BST.

1. Efficient Searching: BSTs provide fast searching capabilities with an average time complexity of O(log n) for balanced trees. This makes them suitable for applications that require quick data retrieval based on a key, such as database indexing and dictionary implementations.
2. Ordered Data Storage: The inherent order of BSTs makes them suitable for scenarios where data needs to be stored in a sorted manner. For example, BSTs can maintain sorted lists or retrieve elements in a particular order.
3. Binary Search Tree in Databases: BSTs are used in databases to create indexes that allow for faster data retrieval based on specific fields. Using BSTs for indexing, databases can efficiently handle large datasets and complex queries.
4. Binary Search Tree in File Systems: File systems often use BSTs to organize and manage directory structures. The hierarchical nature of BSTs aligns well with the hierarchical structure of directories, enabling efficient file retrieval.

### BST Abstract Data Type (ADT)

The BST ADT covers various operations to manipulate and manage the tree efficiently. The basic operations typically supported by a BST ADT include the following:

1.Insertion
2.Update
3.Deletion
4.Search
5.In-order Traversal
6.Pre-order Traversal
7.Post-order Traversal

Let's start by discussing our data model. We will use a Node class to store a single node of BST. Here is what our Node class looks like:

Python3:
```python
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
```

Java:
```java
class Node<T> {
    public T data;
    public Node<T> left;
    public Node<T> right;

    public Node(T value) {
        data = value;
        left = null;
        right = null;
    }
}
```

C++
```cpp
template<class T>
class Node
{
public:
    T data;
    Node<T>* left;
    Node<T>* right;
    Node(T value) : data(value), left(nullptr), right(nullptr) {}
};
```

Golang:
```golang
type Node[T any] struct {
  Data T
  Left *Node[T]
  Right *Node[T]
}
```

The above class represents a single node of a binary tree. It has the following members:

- data: A template member that stores the value of the node.
- left: A pointer to the left child node.
- right: A pointer to the right child node.

The class has two constructors:

- Node(): Default constructor that initializes left and right pointers to null (0).
- Node(int v): Constructor that takes a value v and initializes info with it. It also sets left and right pointers to null.

### ADT Class

Now, let's look at the BST ADT class definition.

```python
class BST:
    def __init__(self):
        self.root = None

    def inOrderHelper(self, p):
        pass

    def preOrderHelper(self, p):
        pass

    def postOrderHelper(self, p):
        pass

    def findMin(self, node):
        pass

    def deleteNode(self, root, node):
        pass

    def insert(self, node):
        pass

    def deleteMethod(self, node):
        pass

    def search(self, node):
        pass

    def inOrder(self):
        pass

    def preOrder(self):
        pass

    def postOrder(self):
        pass
```

Java:
```java
public class BST<T extends Comparable<T>> {
    private Node<T> root;
    
    private void inOrderHelper(Node<T> p);
    private void preOrderHelper(Node<T> p);
    private void postOrderHelper(Node<T> p);
    private Node<T> findMin(Node<T> node);
    private Node<T> deleteNode(Node<T> root, T node);
    
    public BST();
    public void insert(T node);
    public void deleteMethod(T node);
    public boolean search(T node);
    public void inOrder();
    public void preOrder();
    public void postOrder();
}
```

The above code defines a binary search tree class. It uses templates to support different data types for the elements stored in the tree.

The class contains private helper functions for in-order, pre-order, and post-order traversals, as well as for finding the minimum node in a subtree, deleting a node, and updating a node's value.

The public interface provides functions to insert, delete, search, and update nodes in the BST. Additionally, it offers functions to perform in-order, pre-order, and post-order traversals of the tree. The code is designed to facilitate managing and manipulating binary search trees with various data types.

Let's discuss each ADT operation of BST:

### Insertion:

The insertion operation adds a new element to the BST while maintaining the BST property. The BST property ensures that the left subtree contains nodes with values less than or equal to the current node's value, and the right subtree contains nodes with values greater than the current node's value.

Here is the implementation of the insert method:

Python3:
```python
 def insert(self, value):
    new_node = Node(value)
    
    if self.root is None:
        self.root = new_node
    else:
        current = self.root
        parent = None
        
        while current is not None:
            parent = current
            if value < current.data:
                current = current.left
            else:
                current = current.right
        
        if value < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
```

The given code is a template function to insert a new node with a value node into a binary search tree (BST) while maintaining the BST property. If the tree is empty, the new node becomes the root. Otherwise, the function traverses the tree to find the appropriate position for insertion.

It compares the value of the node with each node along the path and goes left if the value is less and right if the value is greater. Based on the comparison, when the correct position is found, the new node becomes the left or right child of the parent node. The function efficiently inserts the node into the BST while keeping the tree ordered.

#### Example:

Consider an empty BST. We insert the values 5, 3, 7, 2, 4, 6, and 8 in the following order:

![Insertion demo](https://www.designgurus.io/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fdownload%2Fstorage%2Fv1%2Fb%2Fdesigngurus-prod.appspot.com%2Fo%2F81a5e864e783846bdcb88c000%3Fgeneration%3D1693423065008568%26alt%3Dmedia&w=2048&q=75)

### Deletion:
The deletion operation removes a node from the BST while maintaining the BST property. Deletion can be more complex as it involves handling different cases based on the node to be deleted.

The delete method uses the findMin and deleteNode methods. The code below implements the findMin, deleteNode, and deleteMethod methods.

Python3:
```python
def find_min(self, node):
    if node.left is None:
        return node
    return self.find_min(node.left)

def delete_node(self, root, value):
    if root is None:
        return root
    
    if value < root.data:
        root.left = self.delete_node(root.left, value)
    elif value > root.data:
        root.right = self.delete_node(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        temp = self.find_min(root.right)
        root.data = temp.data
        root.right = self.delete_node(root.right, temp.data)
    
    return root

def delete_method(self, value):
    self.root = self.delete_node(self.root, value)
```

Java:
```java
private Node<T> findMin(Node<T> node) {
    if (node.left == null) {
        return node;
    }
    return findMin(node.left);
}

private Node<T> deleteNode(Node<T> root, T value) {
    if (root == null) {
        return root;
    }

    if (value.compareTo(root.data) < 0) {
        root.left = deleteNode(root.left, value);
    } else if (value.compareTo(root.data) > 0) {
        root.right = deleteNode(root.right, value);
    } else {
        if (root.left == null) {
            return root.right;
        } else if (root.right == null) {
            return root.left;
        }

        Node<T> temp = findMin(root.right);
        root.data = temp.data;
        root.right = deleteNode(root.right, temp.data);
    }
    return root;
}

public void deleteMethod(T value) {
    root = deleteNode(root, value);
}
```

The code provides two functions: findMin and deleteNode, and a public function deleteMethod, that uses the deleteNode function to delete a node from the BST.

The findMin function is a helper function that finds the minimum node in a given subtree. It starts from the given node and traverses the left children until it reaches the leftmost node, which contains the smallest value in the subtree. It returns the pointer to this minimum node.

The deleteNode function is another helper function responsible for deleting a node from the BST. It uses recursion to traverse the tree and find the node with the value node to be deleted. Once the target node is found, there are three possible cases:

1. The node has no children or only one child (left or right). In this case, the function simply removes the node and links its parent to its child, if any.
2. The node has two children. In this case, the function finds the inorder successor of the node **(the minimum node in its right subtree)**. The value of the inorder successor replaces the value of the node to be deleted, and the function is then recursively called to delete the inorder successor node.

The deleteMethod function is the public interface for deleting a node from the BST. It calls the deleteNode function, passing the root of the BST and the value of the node to be deleted. This initiates the search for the node starting from the root, and the node is deleted if found.

#### Example:

Let's delete the node with value 3 from the following BST:

![Delete demo](https://www.designgurus.io/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fdownload%2Fstorage%2Fv1%2Fb%2Fdesigngurus-prod.appspot.com%2Fo%2F81a5e864e783846bdcb88c001%3Fgeneration%3D1693423938029978%26alt%3Dmedia&w=2048&q=75)

### Searching:

Searching for an element in a BST involves traversing the tree based on comparisons between the target value and the node values until the target value is found or the search reaches a leaf node.

Python3:
```python
def search(self, value):
    current = self.root
    while current is not None:
        if current.data == value:
            return True
        elif value < current.data:
            current = current.left
        else:
            current = current.right
    return False
```

The above code recursively searches for a node with the given value in the BST. If the current node is null (empty) or its value matches the value, we return the current node. Otherwise, we continue searching in the left or right subtree depending on the comparison between value and the current node's value.

#### Example:

Let's search for the key value 8 in the following BST:

![Search](https://www.designgurus.io/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fdownload%2Fstorage%2Fv1%2Fb%2Fdesigngurus-prod.appspot.com%2Fo%2F81a5e864e783846bdcb88c002%3Fgeneration%3D1693424107558547%26alt%3Dmedia&w=2048&q=75)

In the above tree, the following steps are performed to search for the desired value:

1. The value 8 is compared with the root value 5. The traversal is moved to the right subtree since the value is greater than the root value.
2. Again, the value 8 is greater than the right child 7, and the traversal is moved towards the right side of the tree.
3. The right child contains the desired value.

## Traversing a Binary Search Tree (BST)

Traversing a BST involves visiting each node in a specific sequence. There are three common types of BST traversals:

### 1. In-order Traversal:
In-order traversal visits the left subtree, the current node, and then the right subtree, resulting in the elements being visited in ascending order.

Let's discuss the In-order Traversal implementation :

Python3
```python
def in_order_helper(self, node):
  if node is not None:
      self.in_order_helper(node.left)
      print(node.data, end=" ")
      self.in_order_helper(node.right)

def in_order(self):
    self.in_order_helper(self.root)
    print()
```

Golang:
```Golang
func (s *Solution) InOrderHelper(node *TreeNode) {
    if node != nil {
        s.InOrderHelper(node.Left)
        fmt.Print(node.Data, " ")
        s.InOrderHelper(node.Right)
    }
}

func (s *Solution) InOrder() {
    s.InOrderHelper(s.Root)
    fmt.Println()
}
```

The above code provides the implementation of in-order traversal for a binary search tree (BST) template class.

1. The function inOrderHelper() is a private helper function used for the in-order traversal of the BST. It takes a node p to the current node as input and recursively traverses the tree in the following manner:
  - The function proceeds with the traversal if the current node p is not null (i.e., the subtree is not empty).
  - First, it recursively calls inOrderHelper(p->left), which traverses the left subtree of the current node in an in-order fashion.
  - Next, it prints the value of the current node (p->data) to the console.
  - Finally, it recursively calls inOrderHelper(p->right), which traverses the right subtree of the current node in an in-order fashion.
2. The inOrder() function is a public function that serves as the interface for the in-order traversal of the BST. It starts the in-order traversal from the root of the BST by calling the inOrderHelper(root) function.
3. After the inOrderHelper(root) call is completed, the std::cout << std::endl; statement is used to print a new line, separating the output from any other output in the program.

![tree](https://www.designgurus.io/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fdownload%2Fstorage%2Fv1%2Fb%2Fdesigngurus-prod.appspot.com%2Fo%2Fa80c9aab76d957ddfbabe4200%3Fgeneration%3D1693427716187113%26alt%3Dmedia&w=2048&q=75)

In-order traversal of this BST results in the sequence: 1, 2, 3, 5, 6, 8, 9.

### 2. Pre-order Traversal:

Pre-order traversal visits the current node, the left subtree, and the right subtree. Let's discuss the code for the pre-order traversal of a BST.

Python3:
```python
def pre_order_helper(self, node):
    if node is not None:
        print(node.data, end=" ")
        self.pre_order_helper(node.left)
        self.pre_order_helper(node.right)

def pre_order(self):
    self.pre_order_helper(self.root)
    print()
```

The above code implements pre-order traversal for a binary search tree (BST) template class.

1. The function preOrderHelper(Node<T> *p) is a private helper function used for the pre-order traversal of the BST. It takes a pointer p to the current node as input and recursively traverses the tree in the following manner:
    - The function proceeds with the traversal if the current node p is not null (i.e., the subtree is not empty).
    - First, it prints the value of the current node (p->data) to the console, followed by a space, using std::cout << p->data << " ".
    - Then, it recursively calls preOrderHelper(p->left), which traverses the left subtree of the current node in a pre-order fashion.
    - Finally, it recursively calls preOrderHelper(p->right), which traverses the right subtree of the current node in a pre-order fashion.

2. The preOrder() function is a public function that serves as the interface for the pre-order traversal of the BST. It starts the pre-order traversal from the root of the BST by calling the preOrderHelper(root) function.

3. After the preOrderHelper(root) call is completed, the std::cout << std::endl; statement is used to print a new line, separating the output from any other output in the program.

#### Example:

Consider the following BST:

![tree](https://www.designgurus.io/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fdownload%2Fstorage%2Fv1%2Fb%2Fdesigngurus-prod.appspot.com%2Fo%2Fa80c9aab76d957ddfbabe4200%3Fgeneration%3D1693427716187113%26alt%3Dmedia&w=2048&q=75)

Pre-order traversal of this BST results in the sequence: 5, 2, 1, 3, 8, 6, 9.

### 3. Post-order Traversal:

Post-order traversal visits the left subtree, the right subtree, and then the current node.

```python
def post_order_helper(self, node):
    if node is not None:
        self.post_order_helper(node.left)
        self.post_order_helper(node.right)
        print(node.data, end=" ")

def post_order(self):
    self.post_order_helper(self.root)
    print()
```
![tree](https://www.designgurus.io/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fdownload%2Fstorage%2Fv1%2Fb%2Fdesigngurus-prod.appspot.com%2Fo%2Fa80c9aab76d957ddfbabe4200%3Fgeneration%3D1693427716187113%26alt%3Dmedia&w=2048&q=75)

Post-order traversal of this BST results in the sequence: 1, 3, 2, 6, 9, 8, 5.

### Complete ADT

Here is the complete code for the BST implementation with a sample driver code:

Please check code files

## Time and Space Complexity of Binary Search Trees (BST)

Binary Search Trees (BSTs) offer efficient searching, insertion, and deletion operations under certain conditions. However, the time and space complexity of these operations can vary depending on the structure of the BST. This section will explore the time and space complexity for searching, insertion, and deletion in a BST.

### Best Case Time Complexity for Searching: O(log n)

The best-case time complexity for searching in a BST occurs when the tree is balanced. In a balanced BST, each level approximately halves the search space. As a result, the time complexity for searching is logarithmic with respect to the number of nodes (n) in the BST.

#### Example:

Consider the following balanced BST:
![tree](https://www.designgurus.io/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fdownload%2Fstorage%2Fv1%2Fb%2Fdesigngurus-prod.appspot.com%2Fo%2Fa80c9aab76d957ddfbabe4200%3Fgeneration%3D1693427716187113%26alt%3Dmedia&w=2048&q=75)

The best-case time complexity for searching in this BST is O(log n). For example, to search for the value 6, we start at the root (5), move to the right child (7), and then move to the left child (6), finding the value in just three steps.

### Worst Case Time Complexity for Searching: O(n) (for unbalanced trees)

The worst-case time complexity for searching in a BST occurs when the tree is completely unbalanced, forming a linked list. In this scenario, each node has only one child, and the search becomes linear, requiring O(n) operations to traverse through all nodes in the BST.

#### Example:

Consider the following unbalanced BST (linked list):

![worest case](https://www.designgurus.io/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fdownload%2Fstorage%2Fv1%2Fb%2Fdesigngurus-prod.appspot.com%2Fo%2Fcf649688a1a52214dab299a01%3Fgeneration%3D1693428473896936%26alt%3Dmedia&w=2048&q=75)

The worst-case time complexity for searching in this BST is O(n). For example, to search for the value 4, we need to traverse through all nodes, resulting in four steps.

### Best Case Time Complexity for Insertion/Deletion: O(log n)

The best-case time complexity for insertion and deletion in a BST occurs when the tree is balanced. Similar to searching, the time complexity is O(log n) for balanced BSTs, as we can find the appropriate position for insertion or deletion in a logarithmic number of steps.

#### Example:

Consider the following balanced BST:

![tree](https://www.designgurus.io/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fdownload%2Fstorage%2Fv1%2Fb%2Fdesigngurus-prod.appspot.com%2Fo%2Fa80c9aab76d957ddfbabe4200%3Fgeneration%3D1693427716187113%26alt%3Dmedia&w=2048&q=75)

The best-case time complexity for insertion and deletion in this BST is O(log n). For example, to insert the value 7, we start at the root (5), move to the right child (8), then move to the left child (6), and finally insert the value as the right child of 6, taking three steps.

### Worst Case Time Complexity for Insertion/Deletion: O(n) (for unbalanced trees)

The worst-case time complexity for insertion and deletion in a BST occurs when the tree is entirely unbalanced, forming a linked list. In this scenario, each node has only one child, and the insertion or deletion operation may require traversing through all nodes in the BST, resulting in a linear time complexity of O(n).

#### Example:

Consider the following unbalanced BST (linked list):

![worest case](https://www.designgurus.io/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fdownload%2Fstorage%2Fv1%2Fb%2Fdesigngurus-prod.appspot.com%2Fo%2Fcf649688a1a52214dab299a01%3Fgeneration%3D1693428473896936%26alt%3Dmedia&w=2048&q=75)

The worst-case time complexity for insertion and deletion in this BST is O(n). For example, to insert the value 5, we need to traverse through all nodes, resulting in five steps.

### Space Complexity: O(n)
The space complexity of a BST refers to the amount of memory required to store the tree and its elements. In a BST, each node requires a certain amount of memory to store the value and references to its left and right children. The space complexity of a BST is O(n), as it requires space proportional to the number of nodes (n) in the tree.

#### Example:

Consider the following BST:

![tree](https://www.designgurus.io/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fdownload%2Fstorage%2Fv1%2Fb%2Fdesigngurus-prod.appspot.com%2Fo%2Fa80c9aab76d957ddfbabe4200%3Fgeneration%3D1693427716187113%26alt%3Dmedia&w=2048&q=75)

The space complexity of this BST is O(7) ≈ O(n) since it contains seven nodes.

### Issues with BSTs

Binary Search Trees (BSTs) have several issues and limitations that can affect their performance and efficiency in specific scenarios. Some of the key issues with BSTs include:

1. Unbalanced BSTs: BSTs can become unbalanced due to the order in which elements are inserted. The tree can degenerate into a linked list if elements are inserted in a sorted or nearly sorted order. Unbalanced BSTs lead to poor time complexities for searching, insertion, and deletion operations, becoming closer to linear time (O(n)) instead of the optimal logarithmic time (O(log n)).

  Example: A BST with elements inserted in sorted order: 1, 2, 3, 4.
  ![worest case](https://www.designgurus.io/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fdownload%2Fstorage%2Fv1%2Fb%2Fdesigngurus-prod.appspot.com%2Fo%2Fcf649688a1a52214dab299a01%3Fgeneration%3D1693428473896936%26alt%3Dmedia&w=2048&q=75)

2. Degenerate Trees: Degenerate trees are extreme cases of unbalanced BSTs where each node has only one child, essentially forming a linked list. Degenerate trees result in very poor time complexities for all operations, rendering the advantages of using BSTs ineffective.

  Example: A degenerate BST with elements inserted in descending order: 4, 3, 2, 1.
  ![degenerate BST](https://www.designgurus.io/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fdownload%2Fstorage%2Fv1%2Fb%2Fdesigngurus-prod.appspot.com%2Fo%2F565f500c197270546e53dc900%3Fgeneration%3D1693428801132562%26alt%3Dmedia&w=2048&q=75)

3. Performance Issues: Unbalanced and degenerate BSTs can lead to significantly degraded performance for common operations like searching, insertion, and deletion. In the worst-case scenario, when the tree is degenerate, these operations can take linear time (O(n)), negating the primary benefit of using a BST.

4. Complex Balancing: Ensuring a BST remains balanced after insertion and deletion requires complex balancing algorithms. While self-balancing BSTs like AVL trees and Red-Black trees exist, implementing and maintaining these balancing mechanisms adds overhead and complexity to the code.

5. Lack of Unique Keys: BSTs generally do not support duplicate keys. The behavior might vary depending on the implementation when attempting to insert a duplicate key. Some implementations might overwrite the existing value, while others might reject the insertion.

6. Memory Overhead: Each node in a BST requires additional memory for storing pointers to the left and right children. The memory overhead can become significant for large datasets, especially if the tree is poorly balanced.

7. Not Suitable for Dynamic Datasets: BSTs are not well-suited for datasets that frequently change in size. Insertions and deletions can lead to imbalanced trees, requiring additional balancing operations, which can be computationally expensive.

8. Limited Search Performance for Equal Keys: While BSTs provide efficient search times for unique keys, searching for the next greater or lesser element for equal keys requires additional operations and may be less efficient.

Various self-balancing BSTs like AVL trees, Red-Black trees, and Splay trees have been developed to overcome these issues. These structures automatically maintain balance during insertions and deletions, ensuring optimal performance for searching and other operations. Depending on the specific use case and dataset characteristics, self-balancing BSTs might be a better choice than traditional BSTs.

## Conclusion

Binary Search Trees (BSTs) are hierarchical data structures that play a significant role in computer science and various applications. In this conclusion, we recap the fundamental concepts of BSTs, highlight their importance in different fields, and encourage exploring self-balancing trees for optimal performance.

Binary Search Trees are versatile data structures that find applications in diverse fields of computer science. Understanding their properties and applications empowers developers to design efficient algorithms, improve data management, and optimize search operations. Furthermore, adopting self-balancing trees ensures optimal performance even in dynamic environments, making BSTs a valuable tool in the software development arsenal.