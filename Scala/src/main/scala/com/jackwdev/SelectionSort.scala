package com.jackwdev

object SelectionSort { 
  //  Declare method to perform the sort, taking an array as param
  def selectionSort(arr: Array[Int]): Unit = { //   Selection sort: Divides an array into 2 portions, the left being sorted and right unsorted.
    //   Uses this segmentation to move the smallest item in each pass from the unsorted portion into the sorted portion.
    //   Each pass will always move the smallest value in the unsorted portion into the sorted portion.
    //   Time Complexity: Best - O(n2) Average - O(n2) Worst - O(n2)
    var i = 0
    var j = 0
    var minVal = 0
    var temp = 0
    i = 0
    while ( {
      i < arr.length
    }) { 
      //   Assume index i to be the smallest for the first pass
      //   The for loop will increment this so all values below i should be sorted correctly
      minVal = i
      //   Loop for i+1 as value at index i is being used for comparison and swap
      j = i + 1
      while ( {
        j < arr.length
      }) { //   If the value at index j is less, update the index for minVal
        if (arr(j) < arr(minVal)) minVal = j

        j += 1
      }
      //   Once the j loop terminates, min_val will hold the position of the smallest value
      //   Using this index, swap the values of index i and minVal
      temp = arr(i)
      arr(i) = arr(minVal)
      arr(minVal) = temp

      i += 1
    }
  }
}
