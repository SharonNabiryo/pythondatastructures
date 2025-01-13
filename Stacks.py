class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        tmp = self.top
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next

    def push(self, value):
        #create a new_node
        #point its next to the top
        # top = new_node
        #if list is empty, new_node becomes the top
        #increment height

        new_node = Node(value)
        if self.top is None:
            self.top = new_node

        else:
            new_node.next = self.top
            self.top = new_node
            self.height += 1
        return True

    def pop(self):
        # edge case if stack is empty, and 1
        #if not, create a tmp valribale
        # point it to top
        #top = top.next
        #tmp.next = None
        # reduce height
        #return tmp

        if self.height == 0:
            return None

        tmp = self.top
        self.top = self.top.next
        tmp.next = None
        self.height -= 1
        return tmp

my_stack = Stack(2)
my_stack.push(1)
my_stack.pop()
my_stack.print_stack()

