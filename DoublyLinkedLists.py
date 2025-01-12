# start by creating a node
# its constructor will have value, next and prev

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # starts out pointing to nothing
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value) # create a new node
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        if self.length == 0:
            return None
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next

    def append(self, value):
        # created a new Node
        #if empty that new node becomes the head and tail (edge case)
        # get tail.next and point it to the new_node
        # new_node.prev will also point back to tail
        #tail now becomes the new node
        #increase length

        new_node = Node(value)
        if self.length == 0: # // if self.head is None
            self.head  = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
        return True

    def pop(self):
         # create a temp variable and set oit to tail
         # set tail to be = tail.prev
         #set tail.next to be = None
         #set tmp.prev = None
         # reduce length
         # return tmp
         #edge cases, empty list
         # 1 item in the list

        if self.length == 0:
            return None
        tmp = self.tail
        if self.length == 1: # Because the 1 item is going to be popped off
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            tmp.prev = None
        self.length -= 1
        return tmp


    def prepend(self, value):
        #create a new node
        #newnode.next point to head
        #head.prev point to new_node
        #head becomes = new_node
        #increase length
        #edge cases 1 item

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        #create tmp variable
        #tmp = head
        #head = head.next
        #head.prev = None
        #tmp.none
        #reduce the length
        #edgecases ( an empty list and a list with 1 node
        #return tmp

        if self.length == 0:
            return None
        tmp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:  
            self.head = self.head.next
            self.head.prev = None
            tmp.next = None
        self.length -= 1
        return tmp
            
    def get(self, index): # for doubly-linked lists, we iterate from the side that is effecient, shorter to the target
        #deal with edge cases
        # iterate till the index
        #tmp variable set to head or tail
        #move tmp to next/ prev
        # we optimize accprding to the position of the target node

        
        if index < 0 or index >= self.length:
            return None

        if index < self.length/2: # if index is smaller than the first half
            tmp = self.head
            for _ in range(index):
                tmp = tmp.next
        else:                      # bigger than the second half
            tmp = self.tail 
            for _ in range(self.length -1, index, -1): # start, stop. step
               tmp = tmp.prev
        return tmp

    def set_value(self, index, value): # changing the value
        tmp = self.get(index)
        if tmp is not None:
            tmp.value = value
            return True
        return False

    # create node
    # iterate to the index
    #get the index before
    #create two variables before and after
    #make before point to the new node and vice versa
    #new node point at tmp.next
    #3 edge cases

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index -1)
        after = before.next
        
        new_node.next = after
        new_node.prev = before
        before.next = new_node
        after.prev = new_node
        
        self.length += 1
        return True
        

    def remove(self, index):
        # 3 edge cases
        # get the index of target node
        # assign two variables before and after
        # before = tmp.prev
        # after = tmp.next
        # before.next = after
        # after.prev = before
        # make the pointers of tmp .prev and .next point to None
        # reduce length
        # return tmp 
        
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()

        tmp = self.get(index)
        before = tmp.prev
        after = tmp.next
        before.next = after
        after.prev = before
        tmp.next = None
        tmp.prev = None
        
        self.length -= 1
        return tmp
        
        

my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(8)
my_doubly_linked_list.prepend(6)
my_doubly_linked_list.prepend(5)
my_doubly_linked_list.prepend(4)

#print(my_doubly_linked_list.get(2))
my_doubly_linked_list.set_value(1, 9)
my_doubly_linked_list.insert(1, 5)
my_doubly_linked_list.print_list()
print()
my_doubly_linked_list.remove(2)

#print(my_doubly_linked_list.pop()) #2 items

#print(my_doubly_linked_list.pop()) #1 item

#print(my_doubly_linked_list.pop()) # No item

my_doubly_linked_list.print_list()
