class Queue:
    #   Function to initialise a queue object
    def __init__(self, max_len):
        #   Define the queue as an array
        self.queue = [max_len]
        #   Initialise the front and end of the queue as 0
        self.head = self.tail = 0
        #   Define the maximum length of the queue
        self.max_len = max_len

    #   Function to add an item to the end of a queue
    def enqueue(self, data):
        #   Verify that the queue is not currently full
        if self.max_len != self.tail:
            #   Append the data to the end of the array within the queue object
            self.queue.append(data)
            #   Increment the value of tail (this will signify the current length of the queue)
            self.tail += 1
        else:
            #   The queue is full so the data item cannot be added
            print("Sorry, queue is currently full!")

    #   Function to remove an item from the front of the queue
    def dequeue(self):
        #   Verify that the queue is not empty
        if self.head is not None:
            #   Output that the value has left the queue
            print(str(self.queue[0]) + " has been removed from the start of the queue.")
            #   Remove the value (.pop is used as it accepts an index whereas .remove accepts a value)
            self.queue.pop(0)
            #   Decrement the tail as a space has been freed in the queue
            self.tail -= 1
        else:
            #   The queue is empty so no data can be removed
            print("Sorry, the queue is currently empty!")

    #   Function to output all values in the queue in order
    def display(self):
        #   Verify that there is data in the queue
        if self.head is not None:
            #   For loop for the length of the array to output the values
            for i in range(0, self.tail, 1):
                print("Position " + str(i) + " holds " + str(self.queue[i]))
        else:
            #   The queue is empty so no data can be output
            print("Sorry, the queue is currently empty!")

    #   Function to peek at the head of the queue
    def peek(self):
        #   Verify that there is data in the queue
        if self.head != self.tail:
            print(str(self.queue[0]) + " is at the front of the queue.")
        else:
            #   The queue is empty so no data can be output
            print("Sorry, the queue is currently empty!")


#   Driver code
if __name__ == "__main__":
    my_queue = Queue(5)

    my_queue.display()

    my_queue.enqueue(5)
    my_queue.enqueue(10)
    my_queue.enqueue(1)
    my_queue.enqueue(99)

    my_queue.peek()

    my_queue.display()

    my_queue.enqueue(18)
    my_queue.enqueue(79)

    my_queue.display()

    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()

    my_queue.display()