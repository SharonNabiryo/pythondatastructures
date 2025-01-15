class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        tmp = self.first
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next

    def enqueue(self, value): # append
        # create new_node
        #edge case is queue is empty
        # increment length

        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node

        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self): #pop_first
        #edge cases if empty or 1 item 

        if self.length == 0:
            return None

        tmp = self.first
        if self.length == 1:
            self.first = None
            self.last = None

        else:
            self.first = self.first.next
            tmp.next = None
        self.length -= 1
        return tmp

        
        
            

my_queue = Queue(4)
my_queue.enqueue(2)
my_queue.dequeue()

my_queue.print_queue()
