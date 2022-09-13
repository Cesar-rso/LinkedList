import subprocess

class Node:
    def __init__(self, value, nxt = None):
        self.value = value
        self.nxt = nxt


class LinkedList:

    def __init__(self):
        self.head = None

   # Insert value at the end
    def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            tail = self.head
            while tail.nxt is not None:
                tail = tail.nxt
            tail.nxt = Node(value)

    # Remove value at the end
    def pop(self):
        if self.head is not None:
            tail = self.head
            prev = None
            while tail.nxt is not None:
                prev = tail
                tail = tail.nxt
            prev.nxt = None
    
    # Remove the first value
    def shift(self):
        self.head = self.head.nxt
    
    # Insert value in first position
    def unshift(self, value):
        NewNode = Node(value)
        NewNode.nxt = self.head
        self.head = NewNode
        
    def printList(self):
        tail = self.head
        while tail is not None:
            print(tail.value, '-|')
            tail = tail.nxt
            
if __name__ == "__main__":
    LL = LinkedList()
    option = int(input("Choose an option: \n1- push \n2- pop \n3-shift \n4-unshift \n5-Print list \n\n ---Any negative value closes the program--- \n"))
    while option > 0:
        if option == 1:
            value = int(input('Type the value to add to the end of the list: '))
            LL.push(value)
            subprocess.run(['clear'])
            
        if option == 2:
            LL.pop()
            subprocess.run(['clear'])
            
        if option == 3:
            LL.shift()
            subprocess.run(['clear'])
            
        if option == 4:
            value = int(input('Type the value to add to the beginning of the list: '))
            LL.unshift(value)
            subprocess.run(['clear'])
            
        if option == 5:
            subprocess.run(['clear'])
            LL.printList()
            
        option = int(input("Choose an option: \n1- push \n2- pop \n3-shift \n4-unshift \n5-Print list \n\n ---Any negative value closes the program--- \n"))
        
    
