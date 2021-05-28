object BubbleSort {
    //  Declare method to perform the sort, taking an array as param
    fun bubbleSort(arr: IntArray): IntArray {
        //  Bubble sort: Works from left to right, moving the largest value to the correct position in each pass.
        //  Time Complexity: Best - O(n) Average - O(n^2) Worst - O(n^2)

        //  Loop through the array until the array length is met
        var i = 0
        while (i < arr.size - 1) {

            //  Loop through the array - iteration from prior loop as outer most value will be sorted already - 1 (index from 0)
            var j = 0
            while (j < arr.size - i - 1) {

                //  Compare value to the following position and swap if following value is smaller
                if (arr[j] > arr[j + 1]) {

                    //  Use arithmetic to swap values without needing a temp variable
                    arr[j] = arr[j] + arr[j + 1]
                    arr[j + 1] = arr[j] - arr[j + 1]
                    arr[j] = arr[j] - arr[j + 1]
                }
                j++
            }
            i++
        }

        //  Return the sorted array
        return arr
    }
}