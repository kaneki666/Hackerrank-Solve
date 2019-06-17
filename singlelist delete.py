
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
    def deleteNode(self, position):
        if self.head is None:
            return
        cur_node = self.head
        if position == 0:
            self.head = cur_node.next
            cur_node = None
            return
        for i in range(position -1):
            cur_node = cur_node.next
            if cur_node is None:
                break
        if cur_node is None:
            return
        if cur_node.next is None:
            return
        next =cur_node.next.next
        cur_node.next = None
        cur_node.next = next 

firstNode = Node("1")
linkedlist = LinkedList()
linkedlist.insertEnd(firstNode)
secondNode = Node("2")
linkedlist.insertEnd(secondNode)
thirdNode = Node("3")
linkedlist.insertEnd(thirdNode)
fourthNode = Node("4")
linkedlist.insertEnd(fourthNode)
linkedlist.deleteNode(3)
linkedlist.printList()