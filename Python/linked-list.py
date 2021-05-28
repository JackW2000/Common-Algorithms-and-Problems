class DoubleLinkedList:
    #   Function to initialise a DoubleLinkedList object
    def __init__(self):
        self.head = None
        self.tail = None
        self.total_nodes = 0

    #   Function will provide a string representation of the data structure
    def __repr__(self):
        #   Get the first node in the structure
        node = self.head
        node_arr = []
        #   Loop through nodes until the next_node does not exist, appending the data to an array
        while node is not None:
            node_arr.append(node.data)
            node = node.next_node
        #   Append none at the end to indicate the end of the linked list
        node_arr.append("None")
        #   Return a string representation of the data structure
        return str(node_arr)

    #   Function will append a new node to the end of the linked list
    def append(self, data):
        #   If the linked list is empty, the node will be both the head and tail
        if self.head is None:
            #   Create a new node as the head
            self.head = Node(data)
            #   Update the tail to equal the head
            self.tail = self.head
            #   Increment the node count
            self.total_nodes += 1
        #   If the linked list is not empty, the new node will become the tail and the
        #   value of next_node node for the previous_node tail must be updated to point to the new node
        else:
            #   Create a new node as the next_node node for the current tail
            self.tail.next_node = Node(data)
            #   Set the previous_node node for the new node to point to the tail
            self.tail.next_node.previous_node = self.tail
            #   Update the tail to refer to the newly created node
            self.tail = self.tail.next_node
            #   Increment the node count
            self.total_nodes += 1
        return

    #   Function will insert a new node at a given index
    def insert(self, data, index):
        #   Verify whether the index is in range of the linked list/ is a valid value
        if (index > self.total_nodes) | (index < 0):
            print("Cannot insert a node as the index is not in range of the linked list.")
        #   Else, if the index is equal to the node count, the new node is to be inserted at the end
        elif index == self.total_nodes:
            #   Append the data using the custom append function
            self.append(data)
        #   Else, if the index is 0, add a new node at the start of the linked list
        elif index == 0:
            #   Create a new node and set it as the previous_node node for the current head node
            self.head.previous_node = Node(data)
            #   Set the value for next_node for the new node to equal the current head node
            self.head.previous_node.next_node = self.head
            #   Update the value of head to point to the newly inserted node
            self.head = self.head.previous_node
            #   Increment the node count
            self.total_nodes += 1
        #   Else, the index is value but is not the start or end of the linked list
        else:
            #   Get the head node
            start = self.head
            #   Iterate through the linked list until the index position is reached
            for i in range(index):
                #   Update the value of start to point to the current iteration's node
                start = start.next_node

            #   Set the value for the node prior to the index to point at the new node
            start.previous_node.next_node = Node(data)
            #   Set the value for the previous_node node of the new node to point at the node prior to the index
            start.previous_node.next_node.previous_node = start.previous_node
            #   Set the value for the next_node node for the new node to point to the index (this is the insert)
            start.previous_node.next_node.next_node = start
            #   Set the value for the previous_node node at the index to point to the newly inserted node
            start.previous_node = start.previous_node.next_node
            #   Increment the node count
            self.total_nodes += 1
        return

    #   Function for removing a node at a given index
    def remove(self, index):
        #   Verify whether the index is in range of the linked list/ is a valid value
        if (index > self.total_nodes) | (index < 0):
            print("Cannot remove a node as the index is not in range of the linked list.")
        #   Else, if the index is 0, remove the head node
        elif index == 0:
            #   Update the head to be the second node in the structure (current head is being removed)
            self.head = self.head.next_node
            #   Update the value of previous_node node for the new head to be none
            self.head.previous_node = None
            #   Decrement the node count
            self.total_nodes -= 1
        #   Else, if the index is equal to the count - 1, remove the tail node
        elif index == (self.total_nodes - 1):
            #   Update the tail to be the second to last node in the structure (current tail is being removed)
            self.tail = self.tail.previous_node
            #   Update value of next_node node for the new tail to be none
            self.tail.next_node = None
            #   Decrement the node count
            self.total_nodes -= 1
        #   Else, the index is value but is not the start or end of the linked list
        else:
            #   Get the head node
            start = self.head
            #   Iterate through the linked list until the index position is reached
            for i in range(index):
                #   Update the value of start to point to the current iteration's node
                start = start.next_node
            # Update the value of next_node node for the node prior to the index to point to the node following the
            # index Update the value of previous_node node for the node following the index to point to the node
            # prior to the index This means both the node before and after the index point at one another,
            # skipping the index as it has been removed
            start.previous_node.next_node, start.next_node.previous_node = start.next_node, start.previous_node
            #   Decrement the node count
            self.total_nodes -= 1
        return

    #   Function will provide a representation of the data structures size (count of nodes)
    def size(self):
        return self.total_nodes

    #   Function for searching for a value in the linked list
    def search_for(self, data):
        #   Start at the head node
        start = self.head
        #   Iterate through the linked list until the value is found
        for i in range(self.total_nodes):
            #   If the value is found, return the index
            if start.data == data:
                return i
            #   Else, move to the next_node node
            start = start.next_node
        #   Return none if the value is not found
        return None


class Node:
    #   Function to initialise a Node object
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None

    #   Function will provide a string representation of the data structure
    def __repr__(self):
        return str(self.data)


#   Driver code
if __name__ == "__main__":
    #   Create a DoubleLinkedList
    my_linked_list = DoubleLinkedList()

    #   Output the string representation (this calls __repr__)
    print(my_linked_list)

    #   Output the size of the linked list
    print(my_linked_list.size())

    #   Append data to the linked list
    my_linked_list.append(100)

    #   Output the size of the linked list
    print(my_linked_list.size())

    #   Append data to the linked list
    my_linked_list.append(5)
    my_linked_list.append(12)
    my_linked_list.append(234)

    #   Output the string representation (this calls __repr__)
    print(my_linked_list)

    #   Output the size of the linked list
    print(my_linked_list.size())

    #   Search for a value within the linked list
    print(my_linked_list.search_for(12))

    #   Remove values at an index within the linked list
    my_linked_list.remove(2)
    my_linked_list.remove(2)

    #   Output the string representation (this calls __repr__)
    print(my_linked_list)
