from collections import deque

class Solution:
    def checkPalindrome(self, s):
        # Remove all non-alphanumeric characters and convert to lowercase
        s = ''.join(filter(str.isalnum, s)).lower()
        # Create a deque (double-ended queue) from the string
        q = deque(s)

        # Continue until there is 0 or 1 character left
        while len(q) > 1:
            # Remove and compare characters from both ends
            if q.popleft() != q.pop():
                return False
        return True
    
sol = Solution()
print(sol.checkPalindrome('madam'))  # returns: True
print(sol.checkPalindrome('openai'))  # returns: False
print(sol.checkPalindrome('A man a plan a canal Panama'))  # returns: True