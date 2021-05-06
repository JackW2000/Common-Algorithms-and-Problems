#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

//  this is a basic implementation of a stack using arrays in C
//  this implementation does not handle stack limits or removal of data very well
//  though data is removed in simulation, the data is actually just set to 0
//  additionally, using an array can limit the stack size or utilise more memory
//  in real world implementations, a linked list would likely be better due to
//  potentially less memory usage and for allowing a wider range of queue sizes dynamically

//  define a limit for the stack size
#define STACK_LIMIT 50

//  declare an array of size LIMIT
//  for demo purposes, the stack and related variables have been declared as global
int stack[STACK_LIMIT];
int topIndex;

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

    printf("Stack simulation using an array\n\r");
    //  set the top to be -1 as default (initialises a flag that the stack is empty)
    topIndex = -1;
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
    int element;
    //  check that there is a value in the stack (topIndex == -1 indicates the stack is empty)
    if (topIndex == (STACK_LIMIT - 1)) {
        //  output that the stack is empty
        printf("Stack underflow (stack is empty)\n");
    } else {
        //  prompt for a value to push
        printf("Enter a value to push onto the stack: ");
        scanf("%d", &element);
        //  increment the index
        topIndex++;
        //  store the value in the index (in this case, this will be the new top position of the stack)
        stack[topIndex] = element;
    }
}

//  function to simulate popping the value from the top of the stack
void pop() {
    int element;
    //  check that there is a value in the stack (topIndex == -1 indicates the stack is empty)
    if (topIndex == (STACK_LIMIT - 1)) {
        //  output that the stack is empty
        printf("Stack underflow (stack is empty)\n");
    } else {
        //  output that the value has been popped
        printf("%d has been popped from the stack\n", stack[topIndex]);
        //  set the value to 0 to clear the data that was stored in the index (not required)
        stack[topIndex] = 0;
        //  decrement the topIndex value to point at the value below in the stack
        topIndex--;
    }
}

//  function that will display the contents of the stack
void display() {
    int i;

    //  check that there is a value in the stack (topIndex == -1 indicates the stack is empty)
    if (topIndex == (STACK_LIMIT - 1)) {
        //  output that the stack is empty
        printf("Stack underflow (stack is empty)\n");
    } else if (topIndex > 0) {
        //  loop through the array being used to simulate the stack, starting at the end
        //  output values in a "top-down" style to illustrate the values being stacked on top of one another
        printf("The following values are contained within the stack:\n");
        //  loop to traverse the array backwards
        for (i = topIndex; i >= 0; i--) {
            printf("%d\n", stack[i]);
        }
    } else {
        //  output if there is only one value on the stack
        printf("Only one value on the stack: %d\n", stack[topIndex]);
    }
}