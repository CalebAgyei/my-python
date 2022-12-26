#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class SLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)  # insert at the beginning
        self.head = node  # make the new insertion now the head

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next_node

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next_node:
            itr = itr.next_node

        itr.next_node = Node(data, None)


if __name__ == '__main__':
    ll = SLinkedList()  # creates a linked lists with nodes
    ll.insert_at_end(33)
    ll.insert_at_beginning(100)
    ll.insert_at_end(56)
    ll.insert_at_end(580)
    ll.insert_at_beginning(256)
    ll.print()  # calls the print method to print the linked list
