'''
Time Complexity

The time complexity of the sort stack algorithm is O(n^2), 
where n is the number of elements in the stack. 
This is because, in the worst case, for every element 
that we pop from the input stack, we might have to pop 
all the elements in the temporary stack (and push them 
back to the original stack) to find the correct place 
to insert the element. Since we have to do this for all
n elements, the time complexity is: n*n = n^2.

Space Complexity
The space complexity of the algorithm is O(n). 
This is because we use an additional temporary 
stack to sort the elements.
'''

class Solution:
    def sortStack(self,stack):
        tempStack = []
        while len(stack):
            current = stack.pop()
            while len(tempStack) and tempStack[-1] > current:
                stack.append(tempStack.pop())
            tempStack.append(current)

        return tempStack

sol = Solution()
print(sol.sortStack([34, 3, 31, 98, 92, 23]))
print(sol.sortStack([4, 3, 2, 10, 12, 1, 5, 6]))
