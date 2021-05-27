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


#   Driver code
if __name__ == "__main__":
    my_array = [1, 564, 1123, 9999, 5641, 1234, 5, 14, 89, 445]

    print("Before sort:")
    print(my_array)

    insertion_sort(my_array)

    print("After sort:")
    print(my_array)
