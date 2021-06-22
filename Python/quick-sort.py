#   Though technically this function will execute a quicksort, as it is not in place
#   it will take longer to execute in most cases and will be more computationally expensive.
#   As this sort is supposed to be quick (hence the name), I'd recommend using the solution implemented further down.
def quick_sort_return(input_arr):
    #   Quick sort: Selects an index (pivot) and sorts around it, meaning that all left items are lesser and
    #   all right items are larger. This is performed recursively on either side of the pivot
    #   Time Complexity: Best - O(n log2 n) Average - O(n log2 n) Worst - O(n^2)

    #   Initialise 3 arrays: one for values less than pivot value,
    #   one for values equal to pivot value,
    #   and one for values larger than pivot value.
    less_arr = []
    equal_arr = []
    greater_arr = []

    #   Check that the array is larger than one value in length
    if len(input_arr) > 1:
        #   Declare the pivot (in this case, the value at index 0)
        pivot = input_arr[0]

        #   For loop over the array, checking each value within the array
        for value in input_arr:

            #   If the value is less than the pivot, append it to the less array
            if value < pivot:
                less_arr.append(value)

            #   If the value is equal to the pivot, append it to the equal array
            elif value == pivot:
                equal_arr.append(value)

            #   If the value is larger than the pivot, append it to the larger array
            elif value > pivot:
                greater_arr.append(value)

        #   Build a single list in form less + equal + larger and return it.
        #   Inside this return, the less and larger portions are recursively sorted.
        #   This repeats until the array length is 1, at which point all values should be in the correct positions.
        #   Following this, a fully sorted array should be returned.
        return quick_sort_return(less_arr) + equal_arr + quick_sort_return(greater_arr)

    #   If there is only one value in the array, it is already sorted and can be returned as is
    else:
        return input_arr


#   This implementation of quick sort works in place, meaning that the original array is altered by the function.
#   This requires less computation than the above solution and in most cases will be faster.
def quick_sort(arr, first_index, last_index):
    #  Quick sort: Selects an index (pivot) and sorts around it, meaning that all left items are lesser and
    #  all right items are larger. This is performed recursively on either side of the pivot
    #  Time Complexity: Best - O(n log2 n) Average - O(n log2 n) Worst - O(n^2)

    #  Verify that a valid range has been given/ that the indices do not match
    #  When the indices match, there will only be 1 item in the array to sort
    if first_index < last_index:
        #  Select a value to pivot around, in this case the first index is selected
        #  This is not always ideal, however in many cases this is fine
        pivot = first_index

        #  Set values for iterators i and j
        i = first_index
        j = last_index

        #  Whilst i is less than j, make comparisons that close around the pivot
        while i < j:
            #  Whilst the value at index i is less than or equal to that of the pivot
            #  and i is less than the end of the array, increment i
            while arr[i] <= arr[pivot] and i < last_index:
                i += 1

            #  Whilst the value at index j is larger than that at the pivot, decrement j
            while arr[j] > arr[pivot]:
                j -= 1

            #  If i is less than j, swap the values at the index locations
            #  As prior loops filter until a swap is needed, this is where the swap takes place
            if i < j:
                arr[i] = arr[i] + arr[j]
                arr[j] = arr[i] - arr[j]
                arr[i] = arr[i] - arr[j]

        #  Update the value of the pivot index
        #  NOTE: Arithmetic swapping here causes erroneous results, possibly due to overlapping values
        temp = arr[pivot]
        arr[pivot] = arr[j]
        arr[j] = temp

        #  As the pivot should now be placed correctly, sort the subarrays on either side of it
        quick_sort(arr, first_index, j - 1)
        quick_sort(arr, j + 1, last_index)


#   Driver code
if __name__ == "__main__":
    #   Quick sort using returns (higher runtime usually as not in place)
    print("Quick sort using return and recursion:")

    my_array = [31, 343, 6, 653, 75, 3445, 5, 261, 2, 42]

    print("Before sort:")
    print(my_array)

    my_array = quick_sort_return(my_array)

    print("After sort:")
    print(my_array)

    #   Quick sort sorting array in place
    print("In place quick sort:")

    my_array = [31, 343, 6, 653, 75, 3445, 5, 261, 2, 42]

    print("Before sort:")
    print(my_array)

    quick_sort(my_array, 0, len(my_array) - 1)

    print("After sort:")
    print(my_array)

