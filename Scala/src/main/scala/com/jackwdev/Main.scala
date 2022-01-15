package com.jackwdev

object Main {
  //  Driver code for demonstrating implemented algorithms
  def main(args: Array[String]): Unit = {
    var unsortedArr = Array(10, 5, 60, 54, 1, 57, 19, 954, 15, 30)
    var searchIndex = 0
    //  Print unsorted array
    System.out.println("Unsorted array:")
    for (i <- unsortedArr.indices) {
      System.out.println(i + ": " + unsortedArr(i))
    }
    System.out.println()
    //  Linear search stuff
    System.out.println("Linear search:")
    searchIndex = LinearSearch.linearSearch(unsortedArr, 54)
    if (searchIndex == -1) System.out.println("Value not found in the array.")
    else System.out.println("Value (54) was found at position " + (searchIndex + 1) + " (index " + searchIndex + ")")
    System.out.println()
    //  Bubble sort stuff
    System.out.println("Bubble sort:")
    BubbleSort.bubbleSort(unsortedArr)
    for (i <- unsortedArr.indices) {
      System.out.println(i + ": " + unsortedArr(i))
    }
    System.out.println()
    //  Re-initialise unsorted array
    unsortedArr = Array[Int](235, 6, 346, 769, 13, 537, 1119, 1, 15, 30)
    System.out.println("Unsorted array:")
    for (i <- unsortedArr.indices) {
      System.out.println(i + ": " + unsortedArr(i))
    }
    System.out.println()
    //  Insertion sort stuff
    System.out.println("Insertion sort:")
    InsertionSort.insertionSort(unsortedArr)
    for (i <- unsortedArr.indices) {
      System.out.println(i + ": " + unsortedArr(i))
    }
    System.out.println()
    //  Binary search stuff
    System.out.println("Binary search:")
    searchIndex = BinarySearch.binarySearch(unsortedArr, 769, 0, unsortedArr.length)
    if (searchIndex == -1) System.out.println("Value not found in the array.")
    else System.out.println("Value (769) was found at position " + (searchIndex + 1) + " (index " + searchIndex + ")")
    System.out.println()
    unsortedArr = Array[Int](122, 53, 5, 78, 90, 6, 45, 4, 7, 84)
    System.out.println("Unsorted array:")
    for (i <- unsortedArr.indices) {
      System.out.println(i + ": " + unsortedArr(i))
    }
    System.out.println()
    //  Merge sort stuff
    System.out.println("Merge sort:")
    MergeSort.mergeSort(unsortedArr)
    for (i <- unsortedArr.indices) {
      System.out.println(i + ": " + unsortedArr(i))
    }
    System.out.println()
    unsortedArr = Array[Int](5, 45, 755, 4, 453, 7, 55, 47, 11, 17)
    System.out.println("Unsorted array:")
    for (i <- unsortedArr.indices) {
      System.out.println(i + ": " + unsortedArr(i))
    }
    System.out.println()
    //  Selection sort stuff
    System.out.println("Selection sort:")
    SelectionSort.selectionSort(unsortedArr)
    for (i <- unsortedArr.indices) {
      System.out.println(i + ": " + unsortedArr(i))
    }
    System.out.println()
    unsortedArr = Array[Int](554, 4, 78, 21, 3, 45, 11, 19, 42, 72)
    System.out.println("Unsorted array:")
    for (i <- unsortedArr.indices) {
      System.out.println(i + ": " + unsortedArr(i))
    }
    System.out.println()
    //  Quick sort stuff
    System.out.println("Quick sort:")
    QuickSort.quickSort(unsortedArr, 0, unsortedArr.length - 1)
    for (i <- unsortedArr.indices) {
      System.out.println(i + ": " + unsortedArr(i))
    }
    System.out.println()
  }
}