object QuickSort {

    //  This method follws the standard approach, mirroring that of the java implementation
    //  Declare method to perform the sort, taking an array as param
    fun quickSortAlpha(arr: IntArray, firstIndex: Int, lastIndex: Int) {
        //  Quick sort: Selects an index (pivot) and sorts around it, meaning that all left items are lesser and
        //  all right items are larger. This is performed recursively on either side of the pivot
        //  Time Complexity: Best - O(n log2 n) Average - O(n log2 n) Worst - O(n^2)

        //  Declare i, j, pivot, and temp as integers
        var i: Int
        var j: Int
        val pivot: Int
        val temp: Int

        //  Verify that a valid range has been given/ that the indices do not match
        //  When the indices match, there will only be 1 item in the array to sort
        if (firstIndex < lastIndex) {
            //  Select a value to pivot around, in this case the first index is selected
            //  This is not always ideal, however in many cases this is fine
            pivot = firstIndex

            //  Set values for iterators i and j
            i = firstIndex
            j = lastIndex

            //  Whilst i is less than j, make comparisons that close around the pivot
            while (i < j) {
                //  Whilst the value at index i is less than or equal to that of the pivot
                //  and i is less than the end of the array, increment i
                while (arr[i] <= arr[pivot] && i < lastIndex) {
                    i++
                }
                //  Whilst the value at index j is larger than that at the pivot, decrement j
                while (arr[j] > arr[pivot]) {
                    j--
                }
                //  If i is less than j, swap the values at the index locations
                //  As prior loops filter until a swap is needed, this is where the swap takes place
                if (i < j) {
                    arr[i] = arr[i] + arr[j]
                    arr[j] = arr[i] - arr[j]
                    arr[i] = arr[i] - arr[j]
                }
            }

            //  Update the value of the pivot index
            //  NOTE: Arithmetic swapping here causes erroneous results, possibly due to overlapping values
            temp = arr[pivot]
            arr[pivot] = arr[j]
            arr[j] = temp

            //  As the pivot should now be placed correctly, sort the subarrays on either side of it
            quickSortAlpha(arr, firstIndex, j - 1)
            quickSortAlpha(arr, j + 1, lastIndex)
        }
    }

    //  This approach is more elegant and utilises functions built into the Kotlin language to speed up the process
    //  This function does not work in place, however could be adjusted to alter the array in place in a future version
    fun quickSortBeta(arr: IntArray): IntArray {

        //  Verify that the array is not empty (this uses the inbuilt isNotEmpty function)
        return if (arr.isNotEmpty()) {
            //  Define the pivot to use the value at the start of the intArray
            val pivot = arr[0]

            //  Use the filter method to extract all values that are equal to the pivot
            //  and convert the resultant list to an intArray
            val equal = arr.filter { it == pivot }.toIntArray()

            //  Use the filter method to extract all values that are less than the pivot
            //  and convert the resultant list to an intArray
            val less = arr.filter { it < pivot }.toIntArray()

            //  Use the filter method to extract all values that are larger than the pivot
            //  and convert the resultant list to an intArray
            val larger = arr.filter { it > pivot }.toIntArray()

            //  Recursively apply the function to the less and larger intArrays
            //  This will repeat until the array is empty, at which point all sorting will be done
            //  Build a final intArray by concatenating the lesser values, equal values, and larger values
            quickSortBeta(less) + equal + quickSortBeta(larger)
        } else {
            //  If the array is empty, return the array
            //  This will avoid an infinite recursion
            arr
        }
    }
}
