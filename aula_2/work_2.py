class Node:   
    def __init__(self, data):
        self.data = data  
        self.next = None  
        
class Stack:   
    def __init__(self):
        self.top = None        
        self.length = 0

    def is_empty(self):
        return self.top == None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.length += 1

    def pop(self):
        if self.top == None:
            return
        temp = self.top
        self.top = temp.next
        self.length -= 1
        return temp;
    
#Implementando uma Fila:

class Queue:   
    # Function to initialize the queue
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0   

    
    def get_size(self):
        return self.length    

    def push(self, data):
        
        node = Node(data)        
        
        #add primeiro elemento
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

        return
    def pop(self):
        if self.head is None: #teste de sanidade

            return

        temp = self.head
        
        self.head = self.head.next
        self.length -= 1
        del temp

        return

    def print(self):
        if self.head is None: #teste de sanidade            
            return

        it = self.head
        while it is not None:
            print(it.data)
            it = it.next
    
lista = Queue()

lista.push(10)
lista.push(20)
lista.push(30)
lista.push(40)
lista.print()
print('--------')

lista.pop()
lista.print() 

print('--------')
lista.push(50)
lista.print()
print('--------')

lista.pop()
lista.print()

print('--------')