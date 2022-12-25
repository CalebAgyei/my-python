#!/usr/bin/python3

class daynames:
    def __init__(self, name=None):
        self.name = name
        self.next_day = None

e1 = daynames('Sun')
e2 = daynames('Mon')
e3 = daynames('Tue')
e4 = daynames('Wed')
e5 = daynames('Thu')
e6 = daynames('Fri')
e7 = daynames('Sat')

e1.next_day = e2
e2.next_day = e3
e3.next_day = e4
e4.next_day = e5
e5.next_day = e6
e6.next_day = e7

# Traversing the nodes

today = e1

while today:
    print(today.name)  # print name of day via class variable 'dataval'
    today = today.next_day
