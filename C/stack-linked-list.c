#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

//  define a structure for each node in the linked list
struct node {
    int nodeData;
    struct node *nextNode;
};

//  declare a temporary node for use with adding and removing nodes
//  for demo purposes, the tempNode has been made global
struct node *tempNode;

//  function prototypes

//  function to push value onto the stack
void push();

//  function to pop a value from the stack
void pop();

//  function to display the stack following the LIFO structure
void display();

//  main will be used to demonstrate the implemented functions
int main() {
    int mode;

    printf("Stack simulation using a linked list\n\r");
    //  loop the following while choice is not 4 (exit)
    do {
        //  output menu options
        printf("1 - Push onto stack\n"
               "2 - Pop off of stack\n"
               "3 - Display stack\n"
               "4 - Exit\n");
        printf("Enter option: ");
        //  read in selected option
        scanf("%d", &mode);
        //  switch case for the correct functionality based on the option
        switch (mode) {
            case 1:
                // push a value onto the top of the stack
                push();
                break;
            case 2:
                //  pop the value from the top of the stack
                pop();
                break;
            case 3:
                //  display the stack
                display();
                break;
            case 4:
                //  close the application
                exit(0);
            default:
                printf("Choice invalid, please try again.\n");
                break;
        }
    } while (mode != 4);
    return 0;
}

//  function to handle simulation of pushing a value onto the stack
void push() {
    int nodeData;
    //  declare a node and allocate memory to it
    struct node *currentNode = (struct node *) malloc(sizeof(struct node));

    //  verify that the node could be successfully created
    if (currentNode == NULL) {
        //  output that the stack is full/ node could not be created
        //  assumption is made here that memory is full, meaning stack cannot be added to anyway
        printf("Stack overflow (stack is full)");
    } else {
        //  prompt for a value to push
        printf("Enter a value to push onto the stack: ");
        scanf("%d", &nodeData);
        //  if the temp node is null, the stack does not currently exist
        if (tempNode == NULL) {
            //  set the data for the current node and point it to null as there is no following node
            currentNode->nodeData = nodeData;
            currentNode->nextNode = NULL;
            //  update temp to hold the value of the node
            //  this is used to update the pointer from null when a new node is added
            tempNode = currentNode;
        } else {
            //  set the data for the current node and point it to null as there is no following node
            currentNode->nodeData = nodeData;
            currentNode->nextNode = tempNode;
            //  update temp to hold the value of the node
            //  this is used to update the pointer from null when a new node is added
            tempNode = currentNode;
        }
    }
}

//  function to simulate popping the value from the top of the stack
void pop() {
    int poppedValue;
    struct node *currentNode;

    //  check that there is a value in the stack (temp will be null if the stack is empty)
    if (tempNode == NULL) {
        //  output that the stack is empty
        printf("Stack underflow (stack is empty)\n");
    } else {
        //  store the value of the node to be popped
        poppedValue = tempNode->nodeData;
        //  update the current node to be the node held in temp
        currentNode = tempNode;
        //  update temp to be the node currently pointed at by temp
        tempNode = tempNode->nextNode;
        //  free the memory that the node was occupying
        free(currentNode);
        //  output that the value has been popped
        printf("%d has been popped from the stack\n", poppedValue);
    }
}

//  function that will display the contents of the stack
void display() {
    struct node *currentNode;
    currentNode = tempNode;

    //  check that there is a value in the stack (temp will be null if the stack is empty)
    if (currentNode == NULL) {
        //  output that the stack is empty
        printf("Stack underflow (stack is empty)\n");
    } else {
        //  loop through the linked list being used to simulate the stack
        //  output values in a "top-down" style to illustrate the values being stacked on top of one another
        printf("The following values are contained within the stack:\n");
        //  loop through the linked list until current node is null (null when there is no next node)
        while (currentNode != NULL) {
            printf("%d\n", currentNode->nodeData);
            currentNode = currentNode->nextNode;
        }
    }
}