'''
Time Complexity: The worst-case time complexity of this algorithm is O(n)
as every element is pushed and popped from the stack exactly once.

Space Complexity: The space complexity of this algorithm is O(n)
as we are using a stack and an array to store the next greater elements.
'''

class Solution:
    def nextGreaterElement(self, arr):
        stack = []
        res = [-1] * len(arr)
        for i in range(len(arr) -1, -1, -1):
            while len(stack) and stack[-1] <= arr[i]:
                stack.pop()
            
            if len(stack):
                res[i] = stack[-1]
            stack.append(arr[i])
        
        return res
    
sol = Solution()

print(sol.nextGreaterElement([4, 5, 2, 10])) # [5, 10, 10, -1]
print(sol.nextGreaterElement([13, 7, 6, 12])) # [-1, 12, 12, 13]