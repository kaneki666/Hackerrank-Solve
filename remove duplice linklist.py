
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertEnd(self, newNode):

        if self.head is None:
            self.head = newNode
        else:
            lastNode =self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next

            lastNode.next = newNode

    def printList(self):

        if self.head is None:
            print("List is Empty!")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
#1>2>3>4>3>4
#1>2>3>4

    def remove_duplicate(self):
        cur = self.head
        prev = None 
        dup_values = { }
        while cur:
            if cur.data in dup_values:
                prev.next = cur.next
                cur = None
                pass
            else:
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next






firstNode = Node("1")
linkedlist = LinkedList()
linkedlist.insertEnd(firstNode)
secondNode = Node("2")
linkedlist.insertEnd(secondNode)
thirdNode = Node("3")
linkedlist.insertEnd(thirdNode)
fourthNode = Node("4")
linkedlist.insertEnd(fourthNode)
fifthNode = Node("3")
linkedlist.insertEnd(fifthNode)
sixthNode = Node("4")
linkedlist.insertEnd(sixthNode)
linkedlist.remove_duplicate()
linkedlist.printList()
