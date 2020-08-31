import threading
import time
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self , value):
        self.buffer.appendleft(value)
    
    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]




def print_binary(numbers):
    numbers_list = Queue()
    numbers_list.enqueue('1')
    for _ in range(numbers):
        front = numbers_list.front()
        print( front)
        numbers_list.enqueue(front + '0')
        numbers_list.enqueue(front + '1')

        numbers_list.dequeue()


        
print_binary(10)




