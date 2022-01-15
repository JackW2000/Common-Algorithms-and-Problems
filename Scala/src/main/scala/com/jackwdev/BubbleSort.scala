package com.jackwdev

object BubbleSort {
  //  Declare method to perform the sort, taking an array as param
  def bubbleSort(arr: Array[Int]): Unit = {
    //  Bubble sort: Works from left to right, moving the largest value to the correct position in each pass.
    //  Time Complexity: Best - O(n) Average - O(n^2) Worst - O(n^2)
    var i = 0
    var j = 0
    //  Loop through the array until the array length is met
    i = 0
    while ( {
      i < arr.length - 1
    }) { 
      //  Loop through the array - iteration from prior loop as outer most value will be sorted already - 1 (index from 0)
      j = 0
      while ( {
        j < arr.length - i - 1
      }) { 
        //  Compare value to the following position and swap if following value is smaller
        if (arr(j) > arr(j + 1)) { 
          //  Use arithmetic to swap values without needing a temp variable
          arr(j) = arr(j) + arr(j + 1)
          arr(j + 1) = arr(j) - arr(j + 1)
          arr(j) = arr(j) - arr(j + 1)
        }
        j += 1
      }
      i += 1
    }
  }
}