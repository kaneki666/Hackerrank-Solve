class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.head is None:
                    break
                lastNode = newNode.next
            lastNode.next = newNode
    def printlist(self):
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode = currentnode.next
            



firstnode = Node("Sadman")
linkedlist = Linkedlist()
linkedlist.insert(firstnode)
secondnode = Node("Tanin")
linkedlist.insert(secondnode)
thirdnode = Node("Digonto")
linkedlist.insert(thirdnode)
linkedlist.printlist()