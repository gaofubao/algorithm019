# 设计实现双端队列。
# 你的实现需要支持以下操作：
# MyCircularDeque(k)：构造函数,双端队列的大小为k。
# insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
# insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
# deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
# deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
# getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
# getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
# isEmpty()：检查双端队列是否为空。
# isFull()：检查双端队列是否满了。
# https://leetcode.com/problems/design-circular-deque/


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.front = 0
        self.rear = 0
        self.capacity = k + 1
        self.arr = [0 for _ in range(self.capacity)]
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.arr[self.front] = value
        return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1

        return self.arr[self.front]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1

        return self.arr[(self.rear - 1 + self.capacity) % self.capacity]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.rear
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.rear + 1) %  self.capacity == self.front


if __name__ == "__main__":
    circularDeque = MyCircularDeque(3)

    param_1 = circularDeque.insertLast(1)
    param_2 = circularDeque.insertLast(2)
    param_3 = circularDeque.insertFront(3)
    param_4 = circularDeque.insertFront(4)
    param_5 = circularDeque.getRear()
    param_6 = circularDeque.isFull()
    param_7 = circularDeque.deleteLast()
    param_8 = circularDeque.insertFront(4)
    param_9 = circularDeque.getFront()


    print(param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8, param_9)
