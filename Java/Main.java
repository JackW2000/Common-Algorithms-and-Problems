package com.jackwdev;

public class Main {

    //  Driver code for demonstrating implemented algorithms
    public static void main(String[] args) {
        int[] unsortedArr = {10, 5, 60, 54, 1, 57, 19, 954, 15, 30};
        int[] bubbleSortedArr, insertionSortedArr;
        int index;

        System.out.println("Unsorted array:");

        for (int i = 0; i < unsortedArr.length; i++) {
            System.out.println(i + ": " + unsortedArr[i]);
        }

        //  Linear search stuff
        System.out.println("Linear search:");

        index = LinearSearch.linearSearch(unsortedArr, 54);
        System.out.println(index);

        index = LinearSearch.linearSearch(unsortedArr, 9);
        System.out.println(index);

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
    }
}
