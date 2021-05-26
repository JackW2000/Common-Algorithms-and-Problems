package com.jackwdev;

public class InsertionSort {
    //  Declare method to perform the sort, taking an array as param
    public static int[] insertionSort(int[] arr){
        //  Insertion sort: Works from left to right, moving the current index value to the correct position in each pass.
        //  Time Complexity: Best - O(n) Average - O(n^2) Worst - O(n^2)

        //  Declare that i, j, current are type int
        int i, j, current;

        //  Loop starting at position 1 as the value at position 0 is theoretically in a "sorted" portion of the array
        for (i = 1; i < arr.length; i++) {

            //  Define the current value to sort around
            current = arr[i];

            //  Set the second index to be current - 1
            j = i - 1;

            //  Continue swapping whilst the value at index 2 is larger than current
            while (j >= 0 && arr[j] > current) {

                //  Perform swap
                arr[j + 1] = arr[j];

                //  Decrement index value of j
                j -= 1;
            }

            //  Move current value into second indexer + 1 to place in correct position
            arr[j + 1] = current;
        }

        //  Return the sorted array
        return arr;
    }

}
