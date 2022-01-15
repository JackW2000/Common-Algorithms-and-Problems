package com.jackwdev

object LinearSearch { 
  //  Declare method to perform the search, taking an array and searchFor as params
  def linearSearch(arr: Array[Int], searchFor: Int): Int = { 
    //  Linear search: Iterates through an array until the value is found or the array is fully traversed.
    //  Time Complexity: Best - O(1) Average - O(n) Worst - O(n)
    //  NOTE: Best case is when the value is in the first index.
    //  Iterate over array until fully traversed
    for (i <- 0 until arr.length) { 
      //  If the value at the current index is the searchFor value, return the index
      if (arr(i) == searchFor) return i
    }
    //  If the value is not found, return -1
    -1
  }
}