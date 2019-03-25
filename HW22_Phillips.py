#Follow the instruction on this page, create the Node Class and the linkedList Class. Instantiate a linked list object from the linkedList Class and test all the methods designed in the class. 

# Node Class
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        #To append data to a list, you must wrap the data into a Node object first:
        newNode = Node(data)
        #If linked list is empty, assign newNode to the Head pointer & terminate.
        if self.head == None:
            self.head = newNode
            return
        #move Head pointer to the last Node and assign newNode to the last Node's 'next' pointer. 
        else:
            lastNode = self.head #duplicate Head pointer
            while lastNode.next != None:
                lastNode = lastNode.next
            lastNode.next = newNode
    def prepend(self,data):
        newNode = Node(data) # wrap data into a Node object
        if self.head == None: # set newNode as the Head Node if list is already empty
            self.head = newNode
            return
        else:
            newNode.next = self.head # connect old self.head pointer to tail of new node
            self.head = newNode # set newNode as address for new Head pointer
    def insertAfterNode(self, prevNode, data):
        newNode = Node(data)
        newNode.next = prevNode.next 
        prevNode.next = newNode
    def printList(self):
        curNode = self.head #duplicate so you are not losing 'self.head'
        while curNode != None:
            print(curNode.data)
            curNode = curNode.next
    def deleteNode(self, key):
        curNode = self.head #duplicate the head pointer first
        if curNode != None and curNode.data == key: #the head node is the one to be deleted 
            self.head = curNode.next
            curNode = None
            return
        else:
            prev = None
            while curNode != None and curNode.data != key:
                prev = curNode
                curNode = curNode.next
            if curNode == None: #why it is not curNode.next == None???? If the original linkedlist is empty, then there is no curNode.next at all. If the scan pointer 'curNode' is already pointing to the 'None' after the last node, then there is no None.next as well
                pritn('The data is not found i nthe list')
                return
            else:
                prev.next = curNode.next
                curNode = None #Why it is not curNode.next = None??? When you don't need this node anymore, just point the entire Node to None....

#Test append 

team = LinkedList()
team.append('P')
team.append('i')
team.append('r')
team.append('a')
team.append('t')
team.append('e')
team.append('s')
team.printList()
print()

#Test prepend

team.prepend('Z')
team.printList()
print()

#Test deletenode

team.deleteNode('Z')
team.printList()
print()

#Test insertafternode

team.insertAfterNode(team.head.next,'Z')
team.printList()
