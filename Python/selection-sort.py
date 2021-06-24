def selectionSort(arr):
    #   Selection sort: Divides an array into 2 portions, the left being sorted and right unsorted.
    #   Uses this segmentation to move the smallest item in each pass from the unsorted portion into the sorted portion.
    #   Each pass will always move the smallest value in the unsorted portion into the sorted portion.
    #   Time Complexity: Best - O(n2) Average - O(n2) Worst - O(n2)

    for i in range(len(arr)):
        #   Assume index i to be the smallest for the first pass
        #   The for loop will increment this so all values below i should be sorted correctly
        min_val = i

        #   Loop for i+1 as value at index i is being used for comparison and swap
        for j in range(i + 1, len(arr)):

            #   If the value at index j is less, update the index for min_val
            if arr[j] < arr[min_val]:
                min_val = j

        #   Once the j loop terminates, min_val will hold the position of the smallest value
        #   Using this index, swap the values of index i and min_val
        arr[i], arr[min_val] = arr[min_val], arr[i]


#   Driver code
if __name__ == "__main__":
    my_array = [54, 2, 7, 57, 4, 675, 8, 524, 725, 1]

    print("Before sort:")
    print(my_array)

    selectionSort(my_array)

    print("After sort:")
    print(my_array)
