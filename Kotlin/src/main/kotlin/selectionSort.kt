object SelectionSort {
    //   Selection sort: Divides an array into 2 portions, the left being sorted and right unsorted.
    //   Uses this segmentation to move the smallest item in each pass from the unsorted portion into the sorted portion.
    //   Each pass will always move the smallest value in the unsorted portion into the sorted portion.
    //   Time Complexity: Best - O(n2) Average - O(n2) Worst - O(n2)

    fun selectionSortAlpha(arr: IntArray) {
        var j: Int
        var minVal: Int
        var temp: Int
        var i = 0
        while (i < arr.size) {

            //   Assume index i to be the smallest for the first pass
            //   The for loop will increment this so all values below i should be sorted correctly
            minVal = i

            //   Loop for i+1 as value at index i is being used for comparison and swap
            j = i + 1
            while (j < arr.size) {


                //   If the value at index j is less, update the index for minVal
                if (arr[j] < arr[minVal]) {
                    minVal = j
                }
                j++
            }

            //   Once the j loop terminates, min_val will hold the position of the smallest value
            //   Using this index, swap the values of index i and minVal
            temp = arr[i]
            arr[i] = arr[minVal]
            arr[minVal] = temp
            i++
        }
    }

    fun selectionSortBeta(arr: IntArray) {
        //  Declare temp (use to swap values later)
        var temp: Int

        //  Iterate over the array using the indices property
        for (i in arr.indices) {
            var minIndex = i

            //  Iterate over the array size -1 (the end of the array)
            //  Using downto to work from a large value down to the value of i
            //  This will have the effect of counting from the largest index and decrementing until i is reached
            for (j in arr.size - 1 downTo i) {
                //  If the value at index j is less than that of minIndex, update the minIndex
                if (arr[j] < arr[minIndex])
                    minIndex = j
            }

            //  If the value of i is not the minIndex, swap the values in positions i and minIndex
            //  This has the effect of moving the smallest value to the correct position for the pass
            if (i != minIndex) {
                temp = arr[i]
                arr[i] = arr[minIndex]
                arr[minIndex] = temp
            }
        }
    }
}