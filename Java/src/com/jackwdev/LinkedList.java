package com.jackwdev;

public class LinkedList {
    private Node firstNode = null;
    private Node lastNode = null;
    private int listLength = 0;

    // Setters and Getters for LinkedList values

    public Node getFirstNode() {
        return firstNode;
    }

    public void setFirstNode(Node firstNode) {
        this.firstNode = firstNode;
    }

    public Node getLastNode() {
        return lastNode;
    }

    public void setLastNode(Node lastNode) {
        this.lastNode = lastNode;
    }

    public int getListLength() {
        return listLength;
    }

    // Method to increment ListLength by 1
    public void incrementListLength() {
        this.listLength += 1;
    }

    // Method to decrement ListLength by 1
    public void decrementListLength() {
        this.listLength -= 1;
    }

    // Constructor method
    public LinkedList(Node node) {
        this.firstNode = node;
        this.lastNode = node;
        this.listLength = 1;
    }

    // Append a node to the end of the LinkedList
    public void appendNode(Node node) {
        // Point the previousNode property to the current last node
        node.setPreviousNode(this.getLastNode());

        // Update the value of nextNode for the current last node to point at the new node
        this.getLastNode().setNextNode(node);
        // this.lastNode.setNextNode(node); would also work here
        // I opted to use setters and getters where possible in this example

        // Update the value of lastNode to be the newly appended node
        this.setLastNode(node);

        // Increment the node counter
        this.incrementListLength();
    }

    // Append a node to the end of the LinkedList
    public void appendNodeByValue(int value) {
        // Create a new node
        Node node = new Node(value);

        // Point the previousNode property to the current last node
        node.setPreviousNode(this.getLastNode());

        // Update the value of nextNode for the current last node to point at the new node
        this.getLastNode().setNextNode(node);

        // Update the value of lastNode to be the newly appended node
        this.setLastNode(node);

        // Increment the node counter
        this.incrementListLength();
    }

    // Insert a node at the beginning of the LinkedList
    public void prependNode(Node node) {
        // Set the next node value for the new node to point at the current first node
        node.setNextNode(this.getFirstNode());

        // Set the previous node for the current first node to be the new node
        this.getFirstNode().setPreviousNode(node);

        // Set a new firstNode for the LinkedList object
        this.setFirstNode(node);

        // Increment the node counter
        this.incrementListLength();
    }

    // Insert a node at the beginning of the LinkedList
    public void prependNodeByValue(int value) {
        // Create a new node
        Node node = new Node(value);

        // Set the next node value for the new node to point at the current first node
        node.setNextNode(this.getFirstNode());

        // Set the previous node for the current first node to be the new node
        this.getFirstNode().setPreviousNode(node);

        // Set a new firstNode for the LinkedList object
        this.setFirstNode(node);

        // Increment the node counter
        this.incrementListLength();
    }

    // Method to "pop" or "dequeue" the first node from the LinkedList
    public void removeFirstNode() {
        // Output the data from the first node
        System.out.println("Removed node value: " + this.getFirstNode().getValue());

        // Set the first node to point at the next node for the existing first node
        this.setFirstNode(this.getFirstNode().getNextNode());

        // Set the previous node for the new start node to null
        this.getFirstNode().setPreviousNode(null);

        // Decrement the list length
        this.decrementListLength();
    }

    // Method to "pop" or "dequeue" the last node from the LinkedList
    public void removeEndNode() {
        // Output the data from the first node
        System.out.println("Removed node value: " + this.getLastNode().getValue());

        // Set the first node to point at the next node for the existing first node
        this.setLastNode(this.getLastNode().getPreviousNode());

        // Set the next node for the new end node to null
        this.getLastNode().setNextNode(null);

        // Decrement the list length
        this.decrementListLength();
    }

    // Method to step through a linked list, printing the node values
    public void printLinkedList() {
        System.out.println("Linked list values:");
        // Check that the first node is not NULL
        if (this.getFirstNode() != null) {
            // Get the current node as the fist node
            Node currentNode = this.getFirstNode();

            int counter = 0;

            // While there is a value in nextNode, print the current node value and update currentNode to be nextNode
            while (currentNode.getNextNode() != null) {
                System.out.println(counter + ": " + currentNode.getValue());
                currentNode = currentNode.getNextNode();
                counter++;
            }

            // As the loop will exit when the last node is reached, we must output the value of lastNode here
            System.out.println(counter + ": " + currentNode.getValue());
            System.out.println();
        }
    }

    //  NODE INSERTION BETWEEN NODES IS CURRENTLY NOT AVAILABLE
//  THE GENERAL CONCEPT HAS BEEN LEFT IN FOR ANY WHO ARE INTERESTED
//  COMING SOON
//    // Insert a node between two nodes in the LinkedList
//    // i.e. [1, 2, 3] insert 4 between 1 and 2 becomes [1, 4, 2, 3]
//    public void insertNode(Node node, Node previous, Node next) {
//        // Set the next node value for the previous node to point at the new node
//        previous.setNextNode(node);
//
//        // Set the previous node value for the next node to point to the new node
//        next.setPreviousNode(node);
//
//        // Set the value of next node for the new node to be the old next node
//        node.setNextNode(next);
//
//        // Set the value of previous node for the new node to be the old previous node
//        node.setPreviousNode(previous);
//
//        // Increment the node counter
//        this.incrementListLength();
//    }
//
//    // Insert a node between two nodes in the LinkedList
//    public void insertNodeByValue(int value, Node previous, Node next) {
//        // Create a new node
//        Node node = new Node(value);
//
//        // Set the next node value for the previous node to point at the new node
//        previous.setNextNode(node);
//
//        // Set the previous node value for the next node to point to the new node
//        next.setPreviousNode(node);
//
//        // Set the value of next node for the new node to be the old next node
//        node.setNextNode(next);
//
//        // Set the value of previous node for the new node to be the old previous node
//        node.setPreviousNode(previous);
//
//        // Increment the node counter
//        this.incrementListLength();
//    }
}

