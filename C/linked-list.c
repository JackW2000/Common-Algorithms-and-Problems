#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

//  this is a basic implementation of a linked list structure in C
//  the linked list here is only linked in one direction, meaning it can only be traversed
//  in one direction - start to end

//  node structure
struct node {
    // sata of the node
    int num;
    //  address of the next node
    struct node *nextPtr;
} *startNode;

//  function prototypes

//  function to create the list
void createNodeList(int n);

//  function to display the list
void displayList();

//  function to display the list in reverse
void displayReversedList(struct node *a);

//  assigns new node to be the beginning of the linked list
void addNewStartNode();

//  assigns new node to be the end of the linked list
void addNewEndNode();

//  assigns new node to be the midpoint of the linked list
void addNewMidNode();

//  removes the node at the midpoint of the linked list
void deleteMidNode();

//  searches for an entity within the list, returning the position and memory location in which it is found, null if not in list
void listSearch();

//  main will demonstrate interactivity of all functions
int main() {
    int n;
    printf("\n\nLinked List : To create and display Singly Linked List :\n");
    printf("-------------------------------------------------------------\n");
    printf("Input the number of nodes : ");
    scanf("%d", &n);
    createNodeList(n);
    printf("\nData entered in the list : \n");
    displayList();
    printf("\nData in the list in reverse : \n");
    displayReversedList(startNode);
    addNewStartNode();
    displayList();
    addNewEndNode();
    displayList();
    addNewMidNode();
    displayList();
    deleteMidNode();
    displayList();
    listSearch();
    return 0;
}

void createNodeList(int n) {
    //  declare 2 nodes
    struct node *fnNode, *temp;
    int num, i;
    //  initialise startNode using malloc
    startNode = (struct node *) malloc(sizeof(struct node));
    //  verify node creation by validating if memory was allocated
    if (startNode == NULL) {
        printf("Memory can not be allocated.");
    } else {
        printf("Input data for node 1 : ");
        scanf("%d", &num);
        //  store data in node
        startNode->num = num;
        startNode->nextPtr = NULL; // links the address field to NULL
        temp = startNode;
        //  creating n nodes and adding to linked list
        for (i = 2; i <= n; i++) {
            fnNode = (struct node *) malloc(sizeof(struct node));
            if (fnNode == NULL) {
                printf("Memory can not be allocated.");
                break;
            } else {
                printf("Input data for node %d : ", i);
                scanf("%d", &num);
                //  links the num field of fnNode with num
                fnNode->num = num;
                //  links the address field of fnNode with NULL
                fnNode->nextPtr = NULL;
                //  links previous node i.e. temp to the fnNode
                temp->nextPtr = fnNode;
                temp = temp->nextPtr;
            }
        }
    }
}

void displayList() {
    //  declare node
    struct node *temp;
    //  verify that the node holds data
    if (startNode == NULL) {
        printf("List is empty.");
    } else {
        temp = startNode;
        //  loop through nodes until no more nodes in list
        while (temp != NULL) {
            //  prints the data of current node
            printf("Data = %d\n", temp->num);
            //  advances the position of current node
            temp = temp->nextPtr;
        }
    }
}

//  this function uses recursion to traverse to the end and output the list in reverse
//  when the final node is reached, a will be NULL and data will be output starting at the final node
void displayReversedList(struct node *a) {
    //  if the node is null, the list is empty
    if (a == NULL) {
        return;
    }
    //  pass in the next node to the function recursively
    displayReversedList(a->nextPtr);
    //  output the data held in the node
    printf("Data = %d\n", a->num);
}

void addNewStartNode() {
    //  declare node
    struct node *newNode;
    //  allocate memory for the new node
    newNode = (struct node *) malloc(sizeof(struct node));
    //  verify whether memory has been successfully allocated to the node
    if (newNode == NULL) {
        printf("Memory can not be allocated.");
    } else {
        printf("Input data for new start node: ");
        //  define the data and nextNode values for the new start node
        scanf("%d", &newNode->num);
        newNode->nextPtr = startNode;
        //  replace the initial startNode with the new node
        startNode = newNode;
        printf("Data inserted as first node\n");
    }
}

void addNewEndNode() {
    //  declare nodes
    struct node *newNode, *temp, *temp2;
    //  allocate memory for the new node
    newNode = (struct node *) malloc(sizeof(struct node));
    //  verify whether memory has been successfully allocated to the node
    if (newNode == NULL) {
        printf("Memory can not be allocated.");
    } else {
        printf("Input data for new end node: ");
        scanf("%d", &newNode->num);
        //  using temporary nodes, move the nodes around to insert a new node at the end
        struct node *temp;
        temp = startNode;
        while (temp != NULL) {
            temp2 = temp;
            temp = temp->nextPtr;
        }
        temp2->nextPtr = newNode;
        newNode->nextPtr = NULL;
    }
    printf("Data inserted as final node\n");
}

void addNewMidNode() {
    int count = 0, mp = 0;
    //  declare nodes
    struct node *newNode, *temp, *temp2;
    //  allocate memory for the new node
    newNode = (struct node *) malloc(sizeof(struct node));
    //  verify whether memory has been successfully allocated
    if (newNode == NULL) {
        printf("Memory can not be allocated.");
    } else {
        printf("Input data for new midpoint node: ");
        scanf("%d", &newNode->num);
        //  check if the list exists
        if (startNode == NULL) {
            printf("List is empty.");
        } else {
            //  traverse the list, incrementing count until the end is reached
            temp = startNode;
            while (temp != NULL) {
                count++;
                temp = temp->nextPtr;
            }
            //  determine the midpoint for the list
            if (count % 2 == 0) {
                mp = count / 2;
            } else {
                mp = (count + 1) / 2;
            }
            count = 0;
            temp = startNode;
            //  traverse to the midpoint, adjusting node pointers until is is reached
            while (count != mp) {
                temp2 = temp;
                temp = temp->nextPtr;
                count++;
            }
            //  insert the node at the midpoint, pointing it to the following node
            temp2->nextPtr = newNode;
            newNode->nextPtr = temp;
            printf("Data inserted as midpoint node\n");
        }
    }
}

void deleteMidNode() {
    int count = 0, mp = 0;
    //  declare nodes
    struct node *temp, *temp2;
    //  verify that the list exists
    if (startNode == NULL) {
        printf("List is empty.");
    } else {
        temp = startNode;
        //  traverse the list to determine it's length
        while (temp != NULL) {
            count++;
            temp = temp->nextPtr;
        }
        //  calculate the midpoint
        if (count % 2 == 0) {
            mp = count / 2;
        } else {
            mp = (count + 1) / 2;
        }
        count = 0;
        temp = startNode;
        //  traverse to the midpoint of the list
        while (count != mp) {
            temp2 = temp;
            temp = temp->nextPtr;
            count++;
        }
        // set the next pointer value of the node at mp-1 to point to the node mp +1
        temp2->nextPtr = temp->nextPtr;
        //  free the memory that the midpoint node was occupying
        free(temp);
    }
    printf("Midpoint node has been removed and memory deallocated\n");
}

void listSearch() {
    //  declare nodes
    struct node *temp, *temp2;
    int lookFor, count = 1, flag = 0;
    //  prompt for input on value to find
    printf("Input a value that you wish to search for: ");
    scanf("%d", &lookFor);
    //  verify that the list exists
    if (startNode == NULL) {
        printf("List is empty.");
    } else {
        temp = startNode;
        //  traverse the list until the node is NULL or the value is found
        while (temp != NULL) {
            //  if the value of the node matches the search, output the position and memory address
            //  ser a flag to avoid failed to find message
            if (temp->num == lookFor) {
                printf("%d found at position %d in the list with the memory address of %d", lookFor, count, temp2);
                flag = 1;
                //  set temp to NULl to exit traversal
                temp = NULL;
                //  else clause will increment counter and node held in temp to be the next in the list
            } else {
                temp2 = temp;
                temp = temp->nextPtr;
                count += 1;
            }
        }
        //  output the following if the value is never found
        if (flag == 0) {
            printf("Item not in list\n");
        }
    }
}
