class Stack:
    #   Function to initialise a stack object
    def __init__(self, max_len):
        #   Define the stack as an array
        self.stack = [max_len]
        #   Define the maximum length of the stack
        self.max_len = max_len
        #   Define a counter for the current top value
        self.top_index = 0

    #   Function to add an item to the top of a stack
    def push(self, data):
        #   Verify that the stack is not currently full
        if self.top_index-1 != self.max_len:
            #   Append data to the stack array
            self.stack.append(data)
            #   Increment the top index
            self.top_index += 1
        else:
            #   The stack is full so the data item cannot be added
            print("Sorry, stack is currently full!")

    #   Function to remove an item from the top of the stack
    def pop(self):
        #   Verify that the stack is not empty
        if self.stack[0] is not None:
            #   Output that the value has left the stack
            print(str(self.stack[self.top_index]) + " has been removed from the top of the stack.")
            #   Remove the value (.pop is used as it accepts an index whereas .remove accepts a value)
            self.stack.pop(self.top_index)
            #   Decrement the value of top_index
            self.top_index -= 1
        else:
            #   The stack is empty so no data can be removed
            print("Sorry, the stack is currently empty!")

    #   Function to output all values in the stack in order
    def display(self):
        #   Verify that there is data in the stack
        if self.stack[0] is not None:
            for i in range(self.top_index, 0, -1):
                print("Position " + str(self.top_index - i) + " holds " + str(self.stack[i]))
        else:
            #   The stack is empty so no data can be output
            print("Sorry, the stack is currently empty!")

    #   Function to peek at the head of the stack
    def peek(self):
        #   Verify that there is data in the stack
        if self.stack[0] is not None:
            print(str(self.stack[self.top_index]) + " is on top of the stack.")
        else:
            #   The stack is empty so no data can be output
            print("Sorry, the stack is currently empty!")


#   Driver code
if __name__ == "__main__":
    my_queue = Stack(5)

    my_queue.display()

    my_queue.push(1)
    my_queue.push(94)
    my_queue.push(46)
    my_queue.push(5656)

    my_queue.peek()

    my_queue.display()

    my_queue.push(233)
    my_queue.push(4)

    my_queue.display()

    my_queue.pop()
    my_queue.pop()
    my_queue.pop()

    my_queue.display()