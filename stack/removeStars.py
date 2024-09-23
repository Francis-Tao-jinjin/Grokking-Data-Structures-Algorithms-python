class Solution:
    def removeStars(self, s):
        stack = []
        for i in s:
            if stack and i == '*':
                stack.pop()
            elif i != '*':
                stack.append(i)
        
        return "".join(stack)

sol = Solution()
print(sol.removeStars("abc*de*f")) # "abdf"
print(sol.removeStars("a*b*c*d")) # "d"
print(sol.removeStars("*a*b*c*d*")) # ""