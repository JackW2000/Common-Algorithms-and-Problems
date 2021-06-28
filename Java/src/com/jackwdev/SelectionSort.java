package com.jackwdev;

public class SelectionSort {
    //  Declare method to perform the sort, taking an array as param
    public static void selectionSort(int[] arr) {
        //   Selection sort: Divides an array into 2 portions, the left being sorted and right unsorted.
        //   Uses this segmentation to move the smallest item in each pass from the unsorted portion into the sorted portion.
        //   Each pass will always move the smallest value in the unsorted portion into the sorted portion.
        //   Time Complexity: Best - O(n2) Average - O(n2) Worst - O(n2)

        int i, j, minVal, temp;

        for (i = 0; i < arr.length; i++) {
            //   Assume index i to be the smallest for the first pass
            //   The for loop will increment this so all values below i should be sorted correctly
            minVal = i;

            //   Loop for i+1 as value at index i is being used for comparison and swap
            for (j = i + 1; j < arr.length; j++) {

                //   If the value at index j is less, update the index for minVal
                if (arr[j] < arr[minVal]) {
                    minVal = j;
                }
            }

            //   Once the j loop terminates, min_val will hold the position of the smallest value
            //   Using this index, swap the values of index i and minVal
            temp = arr[i];
            arr[i] = arr[minVal];
            arr[minVal] = temp;
        }

    }
}
