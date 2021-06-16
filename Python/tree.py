class Tree:

    #   Function to initialise a tree node
    #   Each node can hold a value, a left node, and a right node
    def __init__(self, data):
        self.data = data
        self.left_node = self.right_node = None

    #   Function for inserting a new node into the tree
    #   This function will place the node in the correct location within the tree
    def insert(self, data):
        #   If the value in the current node is less than the new data
        if self.data < data:
            #   If the right node is empty
            if self.right_node is None:
                #   Add the data as a new node to the right of the existing node
                self.right_node = Tree(data)
            else:
                #   Repeat the process until an empty position is found for the new node
                self.right_node.insert(data)
        #   If the value in the current node is larger than the new data
        else:
            #   If the left node is empty
            if self.left_node is None:
                #   Add the data as a new node to the left of the existing node
                self.left_node = Tree(data)
            else:
                #   Repeat the process until an empty position is found for the new node
                self.left_node.insert(data)

    #   Output the tree in a structured order
    #   This will output all left nodes, then the middle, and then the right
    def printTree(self):
        #   Check if the current node has another node to the left
        if self.left_node:
            #   If it does, repeat this process until the lowest depth left node is found
            self.left_node.printTree()

        #   Output the data of the node
        print(self.data, end=' ')

        #   Check if the current node has another node to the right
        if self.right_node:
            #   If it does, repeat this process until the lowest depth right node is found
            self.right_node.printTree()

    #   Function for inserting a new root node
    def new_root(self, data):
        temp = self.data
        self.data = data
        self.insert(temp)

    #   Function will print the data of the root node for the tree
    #   This will also output left and right node data
    def printRoot(self):
        print("Root node details:")
        if self.data is not None:
            if self.left_node is not None and self.right_node is not None:
                print("Data:", self.data,
                      "\nLeft node:", self.left_node.data,
                      "\nRight node:", self.right_node.data)
            elif self.left_node is not None and self.right_node is None:
                print("Data:", self.data,
                      "\nLeft node:", self.left_node.data,
                      "\nRight node: None")
            elif self.left_node is None and self.right_node is not None:
                print("Data:", self.data,
                      "\nLeft node: None",
                      "\nRight node:", self.right_node.data)
            else:
                print("Data:", self.data,
                      "\nLeft node: None",
                      "\nRight node: None")
        else:
            print("Tree is empty.")


#   Driver code
if __name__ == "__main__":
    tree = Tree("H")
    tree.printTree()
    print()
    print()
    tree.printRoot()
    print()
    tree.insert("D")
    tree.insert("P")
    tree.insert("A")
    tree.insert("B")
    tree.insert("R")
    tree.printTree()
    print()
    print()
    tree.new_root("Z")
    tree.printTree()
    print()
    print()
    tree.printRoot()
