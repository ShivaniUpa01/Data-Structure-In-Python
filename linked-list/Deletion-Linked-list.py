from InsertionLinkedList import LinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# def del_middle():
#     erase = self.head


def append():
    linked_list = LinkedList()
    linked_list.insert_front(1)
    linked_list.insert_front(2)
    linked_list.insert_front(3)
    linked_list.insert_front(4)
    linked_list.insert_front(5)

    return linked_list


class DelLinkedList:
    del_list = append()

    def __init__(self):
        self.head = self.del_list.head

    def del_front(self):
        erase = self.del_list.head
        self.del_list.head = erase.next
        erase.next = None

    def del_end(self):
        erase = self.head
        pre = None
        while erase.next is not None:
            pre = erase
            erase = erase.next
        pre.next = None

    def del_middle(self):
        erase = self.head
        count = 0
        pre = None
        while erase:
            erase = erase.next
            count += 1
        pos = int(input("Enter any position in between 0 to %d" % count))
        print(pos)
        if pos == 0:
            print("Enter the correct position")
        else:
            while pos - 1 != 0:
                pre = erase
                erase = erase.next
            pre.next = erase.next

    # new_node = Node(new_data)
    # start = self.head
    # while start == None:
    #     start = start.next


call = DelLinkedList()
call.del_list.display()
print("\n")
call.del_front()
call.del_list.display()

