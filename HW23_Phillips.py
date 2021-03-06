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
    def deleteAtPos(self, pos):
        curNode = self.head
        if pos == 0:
            self.head = curNode.next
            curNode = None
            return
        else:
            cnt = 0
            prev = None
            while curNode != None and cnt != pos:
                prev = curNode
                curNode = curNode.next
                cnt += 1
            if curNode == None:
                print('The Node does not exist.') #maybe the indes is longer than the list
                return
            else:
                prev.next = curNode.next
                curNode = None
    def len_iterative(self):
        cnt = 0
        curNode = self.head
        while curNode != None:
            curNode = curNode.next
            cnt += 1
        return cnt
    def len_recursive(self, headNode):
        if headNode is None:
            return 0
        else:
            return 1 + self.len_recursive(headNode.next)
    def swapNode(self,key1,key2):
        if key1 == key2:
            print('The two nodes are the same nodes, cannot be swapped.')
            return

        prev1 = None
        curNode1 = self.head 
        while curNode1 != None and curNode1.data != key1:
            prev1 = curNode1
            curNode1 = curNode1.next 

        prev2 = None
        curNode2 = self.head 
        while curNode2 != None and curNode2.data != key2:
            prev2 = curNode2
            curNode2 = curNode2.next

        if curNode1 == None or curNode2 == None: #scan reaches end but not found 
            print('The nodes doe not exist in the list.')
            return
        else:
            if prev1 == None: #key1 is in the head node, key2 is not 
                self.head = curNode2
                prev2.next = curNode1
            elif prev2 == None: #key2 is not in the head node, key 1 is not
                self.head = curNode1
                prev1.next = curNode2
            else: #none are the head node
                prev1.next = curNode2
                prev2.next = curNode1

            #swap the .next pointer
            temp1 = curNode1.next
            temp2 = curNode2.next
            curNode1.next = temp2
            curNode2.next = temp1

    def reverse_iterative(self):
        prev = None
        curNode = self.head 
        while curNode != None:
            nxt_temp = curNode.next
            curNode.next = prev #flip the .next point to point to the front 
            # think about why it is not prev = curNode.next

            prev = curNode 
            curNode = nxt_temp
        self.head = prev 

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
print()

#Test deleteAtPos

team.deleteAtPos(2)
team.printList()
print()

#Test len_iterative

print(team.len_iterative())
print()

#Test len_recursive

print(team.len_recursive(team.head))
print()

#Test swapNode

team.swapNode('P','a') #not working right?????
team.printList()
print()

#Test reverse_iterative

team.reverse_iterative()
team.printList()
