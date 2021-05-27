package com.jackwdev;

public class Main {

    //  Driver code for demonstrating implemented algorithms
    public static void main(String[] args) {
        int[] unsortedArr = {10, 5, 60, 54, 1, 57, 19, 954, 15, 30};
        int[] bubbleSortedArr, insertionSortedArr;
        int linearSearchIndex, binarySearchIndex;

        System.out.println("Unsorted array:");

        for (int i = 0; i < unsortedArr.length; i++) {
            System.out.println(i + ": " + unsortedArr[i]);
        }

        //  Linear search stuff
        System.out.println("Linear search:");

        linearSearchIndex = LinearSearch.linearSearch(unsortedArr, 54);
        System.out.println(linearSearchIndex);

        linearSearchIndex = LinearSearch.linearSearch(unsortedArr, 9);
        System.out.println(linearSearchIndex);

        //  Bubble sort stuff
        System.out.println("Bubble sort:");

        bubbleSortedArr = BubbleSort.bubbleSort(unsortedArr);

        for (int i = 0; i < bubbleSortedArr.length; i++) {
            System.out.println(i + ": " + bubbleSortedArr[i]);
        }

        //  Insertion sort stuff
        System.out.println("Insertion sort:");

        insertionSortedArr = InsertionSort.insertionSort(unsortedArr);

        for (int i = 0; i < insertionSortedArr.length; i++) {
            System.out.println(i + ": " + insertionSortedArr[i]);
        }

        //  Binary search stuff
        System.out.println("Binary search");

        binarySearchIndex = BinarySearch.binarySearch(bubbleSortedArr, 60, 0, bubbleSortedArr.length);

        if (binarySearchIndex == -1) {
            System.out.println("Value not found in the array.");
        } else {
            System.out.println("Value was found at position " + (binarySearchIndex + 1) + " (index " + binarySearchIndex + ")");
        }
    }
}