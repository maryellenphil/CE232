#Mary-Ellen

#Task 1

class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items

#   divided by two problem

def decimalToBinary(base10):
    s = Stack()
    base2 = ''
    while base10 > 0:
        r = base10 % 2
        base10 = base10 // 2
        s.push(r)
    while not s.is_empty():
        base2 += str(s.pop())
    return base2

print(decimalToBinary(11))

#   reverse a string problem

def invertString(string):
    s = Stack()
    invstr = ''
    for i in range(len(string)):
        s.push(string[i])
    while not s.is_empty():
        invstr += s.pop()
    return invstr

print(invertString('OLLEH'))

#   parenthesis balance check problem

def is_match(p1,p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    else:
        return False
    
def balanceCheck(string):
    s = Stack()
    i = 0
    balanced = True
    parenthesis1 = '([{'
    parenthesis2 = ')]}'
    if string == '':
        balanced = False
        return balanced
    elif string[-1] not in parenthesis2:
        balanced = False
        return balanced
    else:
        while i < len(string) and balanced == True:
            if string[i] in parenthesis1:
                s.push(string[i])
            else:
                if s.is_empty():
                    balanced = False
                elif is_match(s.pop(),string[i]):
                    balanced = True
                else:
                    balanced = False
                    return balanced
            i += 1
    if s.is_empty() and balanced == True:
        return True
    
print(balanceCheck('[]'))