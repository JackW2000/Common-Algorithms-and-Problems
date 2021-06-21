#   Node class represents each item within the Tree structure
class Node:
    #   Function to initialise a tree node
    #   Each node can hold a value, a left node, and a right node
    def __init__(self, data):
        self.data = data
        self.left_node = self.right_node = None


#   Tree class implemented using linked list style node structure
#   The only property directly implemented for the tree is a root node
#   all other nodes are linked using the node's properties
class Tree:

    #   Function to initialise the root node
    #   Each node can hold a value, a left node, and a right node
    def __init__(self, data):
        #   Initialise a root node using the data passed
        self.root = Node(data)

    #   Function for inserting a new node into the tree
    #   This function will place the node in the correct location within the tree
    def insert(self, data):
        #   If the value in the current node is less than the new data
        if self.root.data < data:
            #   If the right node is empty
            if self.root.right_node is None:
                #   Add the data as a new node to the right of the existing node
                self.root.right_node = Tree(data)
            else:
                #   Repeat the process until an empty position is found for the new node
                self.root.right_node.insert(data)
        #   If the value in the current node is larger than the new data
        else:
            #   If the left node is empty
            if self.root.left_node is None:
                #   Add the data as a new node to the left of the existing node
                self.root.left_node = Tree(data)
            else:
                #   Repeat the process until an empty position is found for the new node
                self.root.left_node.insert(data)

    #   Function will print the data of the root node for the tree
    #   This will also output left and right node data
    def printRoot(self):
        if self.root.data is not None:
            if self.root.left_node is not None and self.root.right_node is not None:
                print("Data:", self.root.data,
                      "Left node:", self.root.left_node.root.data,
                      "Right node:", self.root.right_node.root.data)
            elif self.root.left_node is not None and self.root.right_node is None:
                print("Data:", self.root.data,
                      "Left node:", self.root.left_node.root.data,
                      "Right node: None")
            elif self.root.left_node is None and self.root.right_node is not None:
                print("Data:", self.root.data,
                      "Left node: None",
                      "Right node:", self.root.right_node.root.data)
            else:
                print("Data:", self.root.data,
                      "Left node: None",
                      "Right node: None")
        else:
            print("Tree is empty.")

    # #   Output the tree in a structured order
    # #   This will output all left nodes, then the middle, and then the right
    # def printTree(self):
    #     #   Check if the current node has another node to the left
    #     if self.root.left_node:
    #         #   If it does, repeat this process until the lowest depth left node is found
    #         self.root.left_node.printTree()
    #
    #     #   Output the data of the node
    #     print(self.root.data, end=' ')
    #
    #     #   Check if the current node has another node to the right
    #     if self.root.right_node:
    #         #   If it does, repeat this process until the lowest depth right node is found
    #         self.root.right_node.printTree()

    #   Function will output the tree in order (left to root to right)
    #   This is the same output as the now commented out "printTree" function
    def inorderTraversal(self, tree):
        inorder_tree = []
        if tree:
            inorder_tree = self.inorderTraversal(tree.root.left_node)
            inorder_tree.append(tree.root.data)
            inorder_tree = inorder_tree + self.inorderTraversal(tree.root.right_node)
        return inorder_tree

    #   Function will output the tree in order (root to left to right)
    def preorderTraversal(self, tree):
        preorder_tree = []
        if tree:
            preorder_tree.append(tree.root.data)
            preorder_tree = preorder_tree + self.preorderTraversal(tree.root.left_node)
            preorder_tree = preorder_tree + self.preorderTraversal(tree.root.right_node)
        return preorder_tree

    #   Function will output the tree in order (left to right to root)
    def postorderTraversal(self, tree):
        postorder_tree = []
        if tree:
            postorder_tree = self.postorderTraversal(tree.root.left_node)
            postorder_tree = postorder_tree + self.postorderTraversal(tree.root.right_node)
            postorder_tree.append(tree.root.data)
        return postorder_tree

    #   Function will search for a value within the tree
    #   This will return true if the value is within the tree and false if not
    def searchTree(self, value):
        if self.root.data == value:
            return True
        if self.root.left_node is not None:
            temp = self.root.left_node.searchTree(value)
            if temp is not False:
                return True
        if self.root.right_node is not None:
            temp = self.root.right_node.searchTree(value)
            if temp is not False:
                return True
        return False


#   Driver code
if __name__ == "__main__":
    #   Initialise tree using H as the root node value
    tree = Tree("H")
    print("Tree created using H as the root value")

    # tree.printTree()

    #   Print the tree in order
    print("Inorder traversal:")
    print(tree.inorderTraversal(tree))

    #   Print the root details for the tree
    print("Outputting root details for the tree:")
    tree.printRoot()

    #   Insert values into the tree
    print("Inserting values \"D\", \"P\", \"A\", \"B\", \"R\" into the tree.")
    tree.insert("D")
    tree.insert("P")
    tree.insert("A")
    tree.insert("B")
    tree.insert("R")

    # tree.printTree()

    #   Print the tree in order
    print("Inorder traversal:")
    print(tree.inorderTraversal(tree))

    #   Print the root details for the tree
    print("Outputting root details for the tree:")
    tree.printRoot()

    #   Print the tree in order
    print("Inorder traversal:")
    print(tree.inorderTraversal(tree))

    #   Print the tree pre order

    print("Preorder traversal:")
    print(tree.preorderTraversal(tree))

    #   Print the tree post order
    print("order traversal:")
    print(tree.postorderTraversal(tree))

    #   Search the tree for a value that is within it
    print("Searching for value \"A\"")
    print(tree.searchTree("A"))

    #   Search the tree for a value that is not within it
    print("Searching for value \"U\"")
    print(tree.searchTree("U"))
