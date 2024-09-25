from collections import deque

class Solution:
    def __init__(self, v1, v2):
        self.v1 = deque(v1)
        self.v2 = deque(v2)
        self.turn = 1
    
    def next(self):
        if self.v1 and self.v2:
            if self.turn == 1:
                self.turn = 2
                return self.v1.popleft()
            else:
                self.turn = 1
                return self.v2.popleft()
        elif self.v1:
            return self.v1.popleft()
        elif self.v2: 
            return self.v2.popleft()
        else:
            return None
        
    def hasNext(self):
        if self.v1 or self.v2:
            return True
        return False 
    

class Solution2:
    def __init__(self, v1, v2):
        # Initialize a queue with tuples containing the length and iterator of non-empty input lists.
        self.queue = deque([(len(v), iter(v)) for v in (v1, v2) if v])
        print(self.queue)
        
    def next(self):
        # Dequeue the next element from the iterator and reduce its length by 1.
        length, iter = self.queue.popleft()
        value = next(iter)
        if length > 1:
            self.queue.append((length-1, iter))
        return value
    
    def hasNext(self):
        # Check if there are more elements to process in the queue.
        return bool(self.queue)
    
def main():
    i = Solution2([1, 2], [3, 4, 5, 6])
    print(i.next())  # returns 1
    print(i.next())  # returns 3
    print(i.next())  # returns 2
    print(i.next())  # returns 4
    print(i.next())  # returns 5
    print(i.next())  # returns 6
    print(i.hasNext())  # returns False

main()