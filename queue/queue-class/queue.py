class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0
    
    def enqueue(self, data):
        new_node = Node(data)
        if not self.front:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    def dequeue(self):
        if not self.front:
            return None
        data = self.front.data
        self.front = self.front.next

        # rear could also hold the last element, so we need to check
        # if front becomes None, then rear becomes None
        if not self.front:
            self.rear = None
        
        self.size -= 1
        return data
    
    def peek(self):
        if not self.front:
            return None
        
        return self.front.data
    
    def get_size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
if __name__ == "__main__":
    queue = Queue();
    
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