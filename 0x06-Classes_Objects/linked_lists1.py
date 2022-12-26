#!/usr/bin/python3
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval  # data values or elements
        self.nextval = None  # variable pointer to next node/item in list

class SLinkedList:
    def __init__(self):
        self.headval = None  # create a variable that will hold the head node

list1 = SLinkedList()  # create an instance of linked list
list1.headval = Node('Sun')  # assign the head of the list
e2 = Node('Tue')
e3 = Node('Wed')

# link first node to second node
list1.headval.nextval = e2

# link second node to third node
e2.nextval = e3
