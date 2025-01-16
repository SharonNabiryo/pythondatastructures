class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self): # print all the values in the linked list
        tmp = self.head  # start with the head
        while tmp is not None: # if the pointer to the head is not none
            print(tmp.value)  # print the value of the node
            tmp = tmp.next  # continue to the next value

    def append(self, value):
        # created a new Node
        #if empty that new node becomes the head and tail (edge case)
        # get tail.next and point it to the new_node
        #tail now becomes the new node
        #increase length
        
        new_node = Node(value)
        if self.head is None: # if head and tail point to None (List empty)
           self.head = new_node  # we make them point to the new created node
           self.tail = new_node
           
        else:
            self.tail.next = new_node # we get the tail to point to the new created node
            self.tail = new_node # now the new node becomes the tail
        self.length += 1  # increase the length
        return True  # optional
            
    def pop(self):
        # removing from the end
        #self.tail becomes the previous
        # removed node becomes temp
        #iterate through
        #tmp and current become head
        # reduce length
        #return removed node
        #tail points to none
        #if length is zero, both should become none
        
        if self.length == 0:
            return None
        
        tmp = self.head
        current = self.head
        while tmp.next is not None:
            current = tmp
            tmp = tmp.next
        self.tail = current
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return tmp

    def prepend(self, value):
        #create new Node
        # point it to Head
        # head becomes new Node
        # add length
        # edge cases
        new_node = Node(value) # Create Node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def popFirst(self):
        # create a temp variable
        # set it to head
        # set head to next
        # reduce length
        # return tmp and set it none
        # edge cases if empty, one item and more than 1
        if self.length == 0:
            return None

        else:
            tmp = self.head
            self.head = self.head.next
            tmp.next = None # remove the node
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        return tmp

    def get(self, index):
        #first edge case of out of bounds
        #create a temp variable
        #traverse through
        # use the next attribute to get the index
        if index < 0 or index >= self.length:
            return None
        tmp = self.head
        for _ in range(index):
            tmp = tmp.next
        return tmp
        

    def set_value(self, index, value):
        # create tmp variable
        # check out of bounds
        # asign value
        tmp = self.get(index)
        if tmp is not None:
            tmp.value = value
            return True
        return False

    def insert(self, index, value):
        # 3 edge cases
        # create a new Node
        # create a tmp variable
        # point it to the index of the node before where you want to put the new node
        # new node should point to tmp.next
        # tmp should point to new node
        # add length
        #return true
        
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        tmp = self.get(index -1) # point it to the index before
        new_node.next = tmp.next
        tmp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        # 3 edge cases
        # create a tmp variable for target node
        # create prev variable before target node
        # prev node points to temp node
        # set tmp to point at None
        # reduce the length
        # return removed node
        
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length:
            return self.pop()
        prev = self.get(index -1)
        tmp = prev.next
        prev.next = tmp.next
        tmp.next = None
        self.length -= 1
        return tmp

    #Rverse a linked list
    # set temp = head
    #head = tail
    #tail = temp
    # create two more variables, after and before
    # after = temp.next
    #before = None
    #loop that goes through the length of the loop
    # set after to be equal to temp.next
    # reverse the arrow and make tmp.next = before
    # set before = temp
    # temp = after

    def reverse(self):
        tmp = self.head
        self.head = self.tail
        self.tail = tmp
        after = tmp.next
        before = None
        for _ in range(self.length):
            after = tmp.next
            tmp.next = before # reverses the pointer
            before = tmp
            tmp = after
        
 
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)
my_linked_list.insert(1,1)

my_linked_list.print_list()
print()

my_linked_list.pop()

my_linked_list.prepend(8)
my_linked_list.print_list()
print()

my_linked_list.popFirst()
my_linked_list.print_list()
print()

print(my_linked_list.get(0))
print(my_linked_list.set_value(1,4))

print(my_linked_list.remove(2))

my_linked_list.print_list()
print()

my_linked_list.reverse()
my_linked_list.print_list()
print()



