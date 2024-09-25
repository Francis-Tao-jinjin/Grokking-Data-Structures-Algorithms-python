from collections import deque

class Solution:
    def printMax(self, arr, k):
        # Create a deque to store the indices of elements in the window
        dq = deque()

        # Create an empty list to store the maximum elements
        result = []

        n = len(arr)

        # Process first k (or less) input values
        for i in range(min(k, n)):
            # For every element, the previous smaller elements are useless, so remove them from dq
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
            
            # Add new element at the rear of both result and dq
            dq.append(i)

        # Process the rest of the elements
        for i in range(k, n):
            # The element at the front of the dq is the largest element of the previous window
            result.append(arr[dq[0]])
            # Remove the elements which are out of this window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove all elements smaller than the currently being added element
            # (Remove useless elements)
            # 先检查 dq 的尾部（rear）是为了确保双端队列中的元素保持递减顺序，
            # 从而使得队列的头部（front）始终是当前窗口的最大值。
            # 移除无用元素：如果当前元素 arr[i] 大于或等于 dq 尾部的元素（arr[dq[-1]]），
            # 那么 dq 尾部的元素在当前窗口中已经没有用了，因为它们不可能成为最大值。
            # 因此，需要将这些元素移除。
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()

            # Add the current element at the rear of dq
            dq.append(i)
        
        # Element at the front of the deque is the largest element of the last window
        result.append(arr[dq[0]])
        return result

sol = Solution()
arr = [9, 7, 2, 4, 6, 8, 2, 11, 1]
k = 3
result = sol.printMax(arr, k)

# Print the result
print(result)
