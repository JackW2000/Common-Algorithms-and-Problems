def linear_search(input_arr, search_for):
    # Linear search: Iterates through an array until the value is found or the array is fully traversed.
    # Time Complexity: Best - O(1) Average - O(n) Worst - O(n)
    # NOTE: Best case is when the value is in the first index.

    # For loop through each index of the length of the array
    for i in range(0, len(input_arr), 1):

        # If the value at the current index matches the search for value, return the index
        if input_arr[i] == search_for:
            return i

    # If the entire array is traversed and the value has not been found, return -1
    return -1


#   Driver code
if __name__ == "__main__":
    my_array = [1, 564, 1123, 9999, 5641, 1234, 5, 14, 89, 445]

    print(my_array)

    index = linear_search(my_array, 9999)

    if index != -1:
        print("Value found at index " + str(index))
    else:
        print("Value not found.")
