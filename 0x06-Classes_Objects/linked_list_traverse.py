#!/usr/bin/python3
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval  # data values or elements
        self.nextval = None  # variable pointer to next node/item in list

class SLinkedList:
    def __init__(self):
        self.headval = None  # create a variable that will hold the head node

    def printlist(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


list1 = SLinkedList()  # create an instance of linked list
list1.headval = Node('Sun')  # assign the head of the list
e2 = Node('Mon')
e3 = Node('Tue')

# link first node to second node
list1.headval.nextval = e2

# link second node to third node
e2.nextval = e3

list1.printlist()
