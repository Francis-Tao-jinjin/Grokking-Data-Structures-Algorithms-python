import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

public class Solution {
    public List<Integer> printMax(int[] arr, int k) {
        Deque<Integer> deque = new LinkedList<Integer>();
        List<Integer> result = new ArrayList<Integer>();
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            // Remove the elements which are out of this window
            while (!deque.isEmpty() && deque.peek() < i - k + 1)
                deque.poll();

            // Remove all elements smaller than the currently being added element
            // (remove useless elements)
            while (!deque.isEmpty() && arr[i] >= arr[deque.peekLast()])
                deque.pollLast();

            // Add current element at the rear of deque
            deque.offer(i);

            if (i >= k - 1)
                result.add(arr[deque.peek()]);
        }

        return result;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int arr[] = { 12, 1, 78, 90, 57, 89, 56 };
        int k = 3;
        List<Integer> result = s.printMax(arr, k);

        // Print the result array
        System.out.println(result);
    }
}
