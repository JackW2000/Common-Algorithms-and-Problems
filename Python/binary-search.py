def binary_search(input_arr, search_for):
    # Binary search: (Assumes array is sorted) Splits the array in half using the midpoint,
    # halving the data to look at each time by ignoring values that are less than or larger than
    # the value being searched for.
    # Time Complexity: Best - O(1) Average - O(log(n)) Worst - O(log(n))

    # Set first index as the start of the array
    first_index = 0

    # Set last index to be the index of the final element in the array
    last_index = len(input_arr) - 1

    # Index will represent the index that either:
    # The value is found at or -1 if the value is not found
    index = -1

    # Loop whilst the start and end points aren't equal, and the index is not -1
    while (first_index <= last_index) and (index == -1):

        # Set midpoint to be half way through the array
        midpoint = (first_index + last_index) // 2

        # If the value is found at the midpoint, set index to equal the midpoint
        if input_arr[midpoint] == search_for:
            index = midpoint

        # If the value is not found at the midpoint
        else:

            # If the value is less than the value at the midpoint, update last index to be the midpoint - 1
            if search_for < input_arr[midpoint]:
                last_index = midpoint - 1

                # If the value is larger than the value at the midpoint, update first index to be the midpoint + 1
            else:
                first_index = midpoint + 1

    # Return the index value for the item (-1 if not found)
    return index