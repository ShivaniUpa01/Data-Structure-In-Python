'''# Linked List in Python
# Representation of Linked List in Python
#Create Class Node
class Node:
    #Function to Initialize the node object
    def __init__(self, data):
        self.data = data #Assign data
        self.next = None #Initialize next as null

#Create another class as Linked List
class LinkedList:
    #Function to Initialize the Linked List object
    def __init__(self):
        self.head = None'''
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # Address of next Node
              
class LinkedList:
    def __init__ (self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp = self.head
            while temp:   # while temp is not None:
                print(temp.data, "-->",end=" ")
                temp = temp.next

call = LinkedList()
n = Node(10)
call.head = n
n1 = Node(20)
n.next = n1 # call.head.next = n1
call.display()
