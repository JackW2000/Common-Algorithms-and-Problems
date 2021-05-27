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


#   Driver code
if __name__ == "__main__":
    my_array = [1, 564, 1123, 9999, 5641, 1234, 5, 14, 89, 445]

    print("Before sort:")
    print(my_array)

    bubble_sort(my_array)

    print("After sort:")
    print(my_array)
