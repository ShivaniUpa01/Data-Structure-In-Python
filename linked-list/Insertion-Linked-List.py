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
    
    def insert_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_end(self,new_data):
        new_node = Node(new_data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        
    def insert_middle (self,new_data):
        new_node = Node(new_data)
        temp = self.head
        pos = int(input("Enter element's position"))
        if pos == 0:
            self.insert_front(new_data)
            return
        while pos -1 != 0 and temp != None:
            temp = temp.next
            pos-=1
        if pos == 1:
            new_node.next =temp.next
            temp.next = new_node
        elif pos > 1 and temp == None:
            print("Position out of range")
    
    
call = LinkedList()
n = Node(10)
call.head = n
n1 = Node(20)
n.next = n1 # call.head.next = n1+-*
call.insert_front(50)
call.insert_end(60)
call.insert_middle(80)
call.display()

if __name__ == "__main__":
    print("inside main")
