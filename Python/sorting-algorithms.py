# This file contains Python implementations of common sorting algorithms

def bubble_sort(input_arr):
    # Bubble sort: Works from left to right, moving the largest value to the correct position in each pass.
    # Time Complexity: Best - O(n) Average - O(n^2) Worst - O(n^2)

    # Flag to indicate if a swap has been made
    swapped = True

    # Counter value to track total iterations
    iterations = 0

    # Loop whilst a value has been swapped (no swaps means list is sorted)
    while swapped:

        # Change state of swapped flag to false
        swapped = False

        # Loop through the list, subtracting the iteration counter each time as the largest
        # unsorted value should always "bubble" to the end of the list on each iteration
        for i in range(0, (len(input_arr) - iterations - 1), 1):

            # Compare the value at the current index to the value in the following index
            if input_arr[i] > input_arr[i + 1]:

                # Swap values positions if the value in index "i" is larger than that in "i+1"
                input_arr[i], input_arr[i + 1] = input_arr[i + 1], input_arr[i]

                # Set swapped flag to indicate that a swap has occurred
                swapped = True

            # Increment the iteration counter
        iterations += 1


def insertion_sort(input_arr):
    # Insertion sort: Works from left to right, moving the current index value to the correct position in each pass.
    # Time Complexity: Best - O(n) Average - O(n^2) Worst - O(n^2)

    # For loop starting at position 1 (position 0 is separated into separate arr)
    for i in range(1, len(input_arr), 1):

        # Copy value of current index into storage variable
        current_value = input_arr[i]
        current_pos = i

        # Whilst the index is not 0 and the value at the current position is less than
        # the value at the position previous
        while current_pos > 0 and input_arr[current_pos - 1] > current_value:

            # Move the value at the current position-1 into the next position (current)
            input_arr[current_pos] = input_arr[current_pos - 1]

            # Change current position to look at the index previous as a swap was made
            current_pos = current_pos - 1

        # If the while loop is exited, it means that the current position is 0 or that
        # the value being looked at has been correctly positioned

        # Insert current value into the current position as all larger values should now have been
        # incremented, leaving a gap for the value to fill
        input_arr[current_pos] = current_value


def merge_sort(input_arr):
    # Merge sort: Recursively divides the array, comparing subarrays and rebuilding a sorted array.
    # Time Complexity: Best - O(n log(n)) Average - O(n log(n)) Worst - O(n log(n))

    # Can't perform merge sort if input array length is less than 2
    if len(input_arr) > 1:

        # Calculate the midpoint (using // will ensure the value is int)
        midpoint = len(input_arr) // 2

        # Use splicing to split the list into two halves
        left_split = input_arr[:midpoint]
        right_split = input_arr[midpoint:]

        # Call the function on each half to repeat the process (recursive)
        merge_sort(left_split)
        merge_sort(right_split)

        # Two iterators for traversing the two halves
        left_iterator = 0
        right_iterator = 0

        # Iterator for the main list
        main_iterator = 0

        # While the iterators are not at the end of each half
        while left_iterator < len(left_split) and right_iterator < len(right_split):

            # Compare the value of the left half at the index to that of the right half
            # at it's respective index
            if left_split[left_iterator] < right_split[right_iterator]:

                # If the value in the left split is less than that of the right split
                # set the current index value for the main array to hold the value of the left split
                input_arr[main_iterator] = left_split[left_iterator]

                # Increment through the left split
                left_iterator += 1
            else:

                # If the value in the right split is less than that of the left split
                # set the current index value for the main array to hold the value of the right split
                input_arr[main_iterator] = right_split[right_iterator]

                # Increment through the right split
                right_iterator += 1

            # Increment to the next position in the main array
            main_iterator += 1

        # Whilst the left index is not at the end of the list
        while left_iterator < len(left_split):
            
            # Set the value at the main array index to that of the left split
            input_arr[main_iterator] = left_split[left_iterator]

            # Increment the left and main array index values
            left_iterator += 1
            main_iterator += 1

        # Whilst the right index is not at the end of the list
        while right_iterator < len(right_split):
            # Set the value at the main array index to that of the right split
            input_arr[main_iterator] = right_split[right_iterator]

            # Increment the right and main array index values
            right_iterator += 1
            main_iterator += 1
