#   This function will build a max heap
def heapify_max(input_arr, n, i):
    #   This will be the root
    largest_index = i

    #   When represented using an array, if the root is i, the left child is 2i+1 and the right is 2i+2
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    #   If the left child is greater than the root
    if left_child < n and input_arr[i] < input_arr[left_child]:
        largest_index = left_child

    #   If the right child is greater than the largest found so far
    if right_child < n and input_arr[largest_index] < input_arr[right_child]:
        largest_index = right_child

    #   If the largest index is not equal to i, the index must have changed
    if largest_index != i:
        #   Swap the value in position i with that of the largest index
        input_arr[i], input_arr[largest_index] = input_arr[largest_index], input_arr[i]

        #   Repeat this process using the sub tree
        heapify_max(input_arr, n, largest_index)


#   This function will build a min heap
def heapify_min(input_arr, n, i):
    #   This will be the root
    smallest_index = i

    #   When represented using an array, if the root is i, the left child is 2i+1 and the right is 2i+2
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    #   If the left child is smaller than the root
    if left_child < n and input_arr[left_child] < input_arr[smallest_index]:
        smallest_index = left_child

    #   If the right child is greater than the smallest found so far
    if right_child < n and input_arr[right_child] < input_arr[smallest_index]:
        smallest_index = right_child

    #   If the smallest index is not equal to i, the index must have changed
    if smallest_index != i:
        #   Swap the value in position i with that of the smallest index
        input_arr[i], input_arr[smallest_index] = input_arr[smallest_index], input_arr[i]

        #   Repeat this process using the sub tree
        heapify_min(input_arr, n, smallest_index)


#   sort
def heap_sort(input_arr, heap_type="max"):
    #   If max heap is chosen, sort in ascending order
    if heap_type == "max":
        #   Create a max heap
        for i in range(len(input_arr), -1, -1):
            heapify_max(input_arr, len(input_arr), i)

        #   Extract the largest element and place it into the sorted portion of the array
        for i in range(len(input_arr) - 1, 0, -1):
            #   As the array has been heapified, the largest unsorted element will be the root
            #   Swap the root value with the value at the last index in the array and repeat using i as array length
            #   (i will decrement each iteration, meaning that the sorted values will remain untouched)
            input_arr[i], input_arr[0] = input_arr[0], input_arr[i]
            heapify_max(input_arr, i, 0)

    #   If min heap is chosen, sort in descending order
    elif heap_type == "min":
        #   Create a min heap
        for i in range(len(input_arr), -1, -1):
            heapify_min(input_arr, len(input_arr), i)

        #   Extract the smallest element and place it into the sorted portion of the array
        for i in range(len(input_arr) - 1, 0, -1):
            #   As the array has been heapified, the smallest unsorted element will be the root
            #   Swap the root value with the value at the last index in the array and repeat using i as array length
            #   (i will decrement each iteration, meaning that the sorted values will remain untouched)
            input_arr[i], input_arr[0] = input_arr[0], input_arr[i]
            heapify_min(input_arr, i, 0)


#   Driver code
if __name__ == "__main__":
    my_array = [45, 3, 54, 89, 7, 11, 39, 4, 33, 95]

    print("Using a max heap:")

    print("Before sort:")
    print(my_array)

    heap_sort(my_array, "max")

    print("After sort:")
    print(my_array)

    my_array = [56, 33, 5, 63, 754, 1, 32, 3, 5, 7]

    print("Using a min heap:")

    print("Before sort:")
    print(my_array)

    heap_sort(my_array, "min")

    print("After sort:")
    print(my_array)
