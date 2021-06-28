package com.jackwdev;

public class Main {

    //  Driver code for demonstrating implemented algorithms
    public static void main(String[] args) {
        int[] unsortedArr = {10, 5, 60, 54, 1, 57, 19, 954, 15, 30};
        int searchIndex;

        //  Print unsorted array
        System.out.println("Unsorted array:");

        for (int i = 0; i < unsortedArr.length; i++) {
            System.out.println(i + ": " + unsortedArr[i]);
        }

        System.out.println();

        //  Linear search stuff
        System.out.println("Linear search:");

        searchIndex = LinearSearch.linearSearch(unsortedArr, 54);

        if (searchIndex == -1) {
            System.out.println("Value not found in the array.");
        } else {
            System.out.println("Value (54) was found at position " + (searchIndex + 1) + " (index " + searchIndex + ")");
        }

        System.out.println();

        //  Bubble sort stuff
        System.out.println("Bubble sort:");

        BubbleSort.bubbleSort(unsortedArr);

        for (int i = 0; i < unsortedArr.length; i++) {
            System.out.println(i + ": " + unsortedArr[i]);
        }

        System.out.println();

        //  Re-initialise unsorted array
        unsortedArr = new int[]{235, 6, 346, 769, 13, 537, 1119, 1, 15, 30};

        //  Print unsorted array
        System.out.println("Unsorted array:");

        for (int i = 0; i < unsortedArr.length; i++) {
            System.out.println(i + ": " + unsortedArr[i]);
        }

        System.out.println();

        //  Insertion sort stuff
        System.out.println("Insertion sort:");

        InsertionSort.insertionSort(unsortedArr);

        for (int i = 0; i < unsortedArr.length; i++) {
            System.out.println(i + ": " + unsortedArr[i]);
        }

        System.out.println();

        //  Binary search stuff
        System.out.println("Binary search:");

        searchIndex = BinarySearch.binarySearch(unsortedArr, 769, 0, unsortedArr.length);

        if (searchIndex == -1) {
            System.out.println("Value not found in the array.");
        } else {
            System.out.println("Value (769) was found at position " + (searchIndex + 1) + " (index " + searchIndex + ")");
        }

        System.out.println();

        //  Re-initialise unsorted array
        unsortedArr = new int[]{122, 53, 5, 78, 90, 6, 45, 4, 7, 84};

        //  Print unsorted array
        System.out.println("Unsorted array:");

        for (int i = 0; i < unsortedArr.length; i++) {
            System.out.println(i + ": " + unsortedArr[i]);
        }

        System.out.println();

        //  Merge sort stuff
        System.out.println("Merge sort:");

        MergeSort.mergeSort(unsortedArr);

        for (int i = 0; i < unsortedArr.length; i++) {
            System.out.println(i + ": " + unsortedArr[i]);
        }

        System.out.println();

        //  Re-initialise unsorted array
        unsortedArr = new int[]{5, 45, 755, 4, 453, 7, 55, 47, 11, 17};

        //  Print unsorted array
        System.out.println("Unsorted array:");

        for (int i = 0; i < unsortedArr.length; i++) {
            System.out.println(i + ": " + unsortedArr[i]);
        }

        System.out.println();

        //  Selection sort stuff
        System.out.println("Selection sort:");

        SelectionSort.selectionSort(unsortedArr);

        for (int i = 0; i < unsortedArr.length; i++) {
            System.out.println(i + ": " + unsortedArr[i]);
        }

        System.out.println();
    }
}