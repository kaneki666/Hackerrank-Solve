class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):

    def __init__(self,root):
        self.root = Node(root)

    def printtree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder(tree.root, "")
        else:
            print("Failed")
    # root>left>right
    def preorder(self, start, traversal):
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    #left>right>root
    def postorder(self, start, traversal):
        if start:
            traversal = self.postorder(start.left, traversal)
            self.postorder(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal
    #left>root>right
    def inorder(self, start, traversal):
        if start:
            traversal = self.inorder(start.left,traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder(start.right,traversal)
        return traversal

    def height(self,node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height,right_height)

    def size(self):
        if self.root is None:
            return 0
        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size

tree = BinaryTree(1)
tree.root.left = Node(4)
tree.root.right = Node(6)
tree.root.left.left = Node(7)
tree.root.left.right = Node(10)
tree.root.right.left = Node(12)
tree.root.right.right = Node(30)
tree.root.right.right.right = Node(3)
print(tree.printtree("preorder"))
print(tree.printtree("inorder"))
print(tree.printtree("postorder"))
print(tree.height(tree.root))
print(tree.size())