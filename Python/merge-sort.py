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


#   Driver code
if __name__ == "__main__":
    my_array = [1, 564, 1123, 9999, 5641, 1234, 5, 14, 89, 445]

    print("Before sort:")
    print(my_array)

    merge_sort(my_array)

    print("After sort:")
    print(my_array)