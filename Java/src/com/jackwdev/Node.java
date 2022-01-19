package com.jackwdev;

// Standard Node class for modelling an item in a LinkedList
public class Node {

    private int value;
    private Node previousNode;
    private Node nextNode;

    // Constructor method
    public Node(int value) {
        this.value = value;
    }

    // Setters and Getters for Node values

    public void setPreviousNode(Node previousNode) {
        this.previousNode = previousNode;
    }

    public Node getPreviousNode() {
        return previousNode;
    }

    public Node getNextNode() {
        return nextNode;
    }

    public void setNextNode(Node nextNode) {
        this.nextNode = nextNode;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
}
