package com.jackwdev;

import java.util.Arrays;

public class MergeSort {
    //  Merge sort: Recursively divides the array, comparing subarrays and rebuilding a sorted array.
    //  Time Complexity: Best - O(n log(n)) Average - O(n log(n)) Worst - O(n log(n))

    public static void mergeSort(int[] arr) {

        //  Can't perform merge sort if input array length is less than 2
        if (arr.length < 2) {
            return;
        }

        //  Calculate the midpoint of the array
        int mid = arr.length / 2;

        //  Create 2 sub arrays, one for the left half and another for the right
        //  Using the copyOfRange function will allow array content to be cloned between the given indices
        //  This means leftSplit will contain values from index 0 to the midpoint and the rightSplit
        //  will contain values from the midpoint to the end of the array
        int[] leftSplit = Arrays.copyOfRange(arr, 0, mid);
        int[] rightSplit = Arrays.copyOfRange(arr, mid, arr.length);

        //  Recursively calling the function to divide the subarrays further
        mergeSort(leftSplit);
        mergeSort(rightSplit);

        //  Calling the merge method to recombine splits in a sorted order
        merge(leftSplit, rightSplit, arr);
    }

    public static void merge(int[] leftSplit, int[] rightSplit, int[] arr) {
        int mainIterator = 0, leftIterator = 0, rightIterator = 0;

        //  While the iterators are not at the end of each half
        while (leftIterator < leftSplit.length && rightIterator < rightSplit.length) {

            //  Compare the value of the left half at the index to that of the right half
            //  at it's respective index
            if (leftSplit[leftIterator] < rightSplit[rightIterator]) {

                //  If the value in the left split is less than that of the right split
                //  set the current index value for the main array to hold the value of the left split
                arr[mainIterator] = leftSplit[leftIterator];

                //  Increment through the left split
                leftIterator++;
            } else {
                //  If the value in the right split is less than that of the left split
                //  set the current index value for the main array to hold the value of the right split
                arr[mainIterator] = rightSplit[rightIterator];

                //  Increment through the right split
                rightIterator++;
            }

            //  Increment to the next position in the main array
            mainIterator++;
        }

        //  Whilst the left index is not at the end of the array
        while (leftIterator < leftSplit.length) {
            //  Set the value at the main array index to that of the left split
            arr[mainIterator] = leftSplit[leftIterator];

            //  Increment the left and main array index values
            leftIterator++;
            mainIterator++;
        }

        //  Whilst the right index is not at the end of the array
        while (rightIterator < rightSplit.length) {
            //  Set the value at the main array index to that of the right split
            arr[mainIterator] = rightSplit[rightIterator];

            //  Increment the right and main array index values
            rightIterator++;
            mainIterator++;
        }
    }
}
