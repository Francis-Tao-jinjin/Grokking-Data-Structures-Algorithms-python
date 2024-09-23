class Solution:
    def removeDuplicates(self, s):
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
              stack.append(i)
        return "".join(stack)


sol = Solution()
print(sol.removeDuplicates("abbaca")) # "ca"
print(sol.removeDuplicates("azxxzy")) # "ay"
print(sol.removeDuplicates("abba")) # "ay"