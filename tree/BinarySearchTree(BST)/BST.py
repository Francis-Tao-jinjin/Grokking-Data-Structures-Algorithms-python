class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
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
    
    def in_order_helper(self, node):
        if node is not None:
            self.in_order_helper(node.left)
            print(node.data, end=" ")
            self.in_order_helper(node.right)
    
    def in_order(self):
        self.in_order_helper(self.root)
        print()
    
    def pre_order_helper(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)
    
    def pre_order(self):
        self.pre_order_helper(self.root)
        print()
    
    def post_order_helper(self, node):
        if node is not None:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            print(node.data, end=" ")
    
    def post_order(self):
        self.post_order_helper(self.root)
        print()

# Main function
if __name__ == "__main__":
    obj = BST()
    obj.insert(5)
    obj.insert(3)
    obj.insert(7)
    obj.insert(2)
    obj.insert(4)
    obj.insert(6)
    obj.insert(8)
    
    obj.in_order()
    obj.pre_order()
    obj.post_order()

    obj.delete_method(2)

    obj.in_order()
