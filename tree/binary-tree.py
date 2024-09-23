
class BinaryTree:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  
  def insert(self, value):
    if value < self.value:
      if self.left is None:
        self.left = BinaryTree(value)
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BinaryTree(value)
      else:
        self.right.insert(value)
  
  def search(self, value):
    if (self.value == value):
      return self
    elif value < self.value and self.left is not None:
      return self.left.search(value)
    elif value > self.value and self.right is not None:
      return self.right.search(value)
    return None

  def delete(self, value):
    if value < self.left.value:
      if self.left is not None:
        self.left = self.left.delete(value)
    elif value > self.right.value:
      if self.right is not None:
        self.right = self.right.delete(value)
    else:
      if self.left is None and self.right is None:
        return None
      elif self.left is None:
        return self.right
      elif self.right is None:
        return self.left
      else:
        minLargerNode = self.right;
        while minLargerNode.left is not None:
          minLargerNode = minLargerNode.left
        
        self.value = minLargerNode.value
        self.right = self.right.delete(minLargerNode.value)
    return self
  
  def preOrder(self):
    print(self.value)
    if self.left is not None:
      self.left.preOrder()
    if self.right is not None:
      self.right.preOrder()

  def inOrder(self):
    if self.left is not None:
      self.left.inOrder()
    print(self.value)
    if self.right is not None:
      self.right.inOrder()
  
  def postOrder(self):
    if self.left is not None:
      self.left.postOrder()
    if self.right is not None:
      self.right.postOrder()
    print(self.value)

