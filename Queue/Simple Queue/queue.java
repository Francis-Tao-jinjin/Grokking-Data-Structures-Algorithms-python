class Queue<T> {
  private Node<T> front, rear;
  private int size;

  // Node class for storing data and the reference to the next node
  private static class Node<T> {
      T data;
      Node<T> next;

      Node(T data) {
          this.data = data;
          this.next = null;
      }
  }

  public Queue() {
      front = rear = null;
      size = 0;
  }

  // Add an element to the queue
  public void enqueue(T data) {
      Node<T> newNode = new Node<>(data);
      if (rear == null) {
          front = rear = newNode;
      } else {
          rear.next = newNode;
          rear = newNode;
      }
      size++;
  }

  // Remove an element from the queue
  public T dequeue() {
      if (front == null) {
          return null;
      }
      T data = front.data;
      front = front.next;
      if (front == null) {
          rear = null;
      }
      size--;
      return data;
  }

  // Check the front element of the queue
  public T peek() {
      if (front == null) {
          return null;
      }
      return front.data;
  }

  // Check if the queue is empty
  public boolean isEmpty() {
      return size == 0;
  }

  // Get the size of the queue
  public int size() {
      return size;
  }
}

// Example usage
public class Solution {
  public static void main(String[] args) {
      Queue<Integer> queue = new Queue<>();

      queue.enqueue(1);
      queue.enqueue(2);
      queue.enqueue(3);

      System.out.println("Front element: " + queue.peek());
      System.out.println("Dequeued: " + queue.dequeue());
      System.out.println("Front element: " + queue.peek());
      System.out.println("Queue size: " + queue.size());
  }
}