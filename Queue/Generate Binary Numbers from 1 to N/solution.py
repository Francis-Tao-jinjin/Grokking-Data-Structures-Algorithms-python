from queue import Queue

class Solution:
    def generateBinaryNumbers(self, n):
        q = Queue()
        q.put("1")
        res = []
        while n > 0:
            current = q.get()
            res.append(current)
            q.put(current + "0")
            q.put(current + "1")
            n -= 1
        
        return res

sol = Solution()
print(sol.generateBinaryNumbers(5)) # ['1', '10', '11', '100', '101']
print(sol.generateBinaryNumbers(9)) # ['1', '10', '11', '100', '101']