class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, element):
        if ((self.front == 0 and self.rear == self.size - 1) or
            (self.rear == (self.front - 1) % (self.size - 1))):
            print("Queue is full")
        elif self.front == -1: # Insert First Element
            self.front = self.rear = 0
            self.queue[self.rear] = element
        elif self.rear == self.size - 1 and self.front != 0: # Insert at the beginning, 
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
