class Solution:
    def simplifyPath(self, path):
        # ToDo: Write Your Code Here.
        stack = []
        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p != "." and p:
                stack.append(p)

        if stack:
            return "/" + "/".join(stack)
        return "/";


sol = Solution()
print(sol.simplifyPath("/home/")) # "/home"

print(sol.simplifyPath("/a//b////c/d//././/.."))