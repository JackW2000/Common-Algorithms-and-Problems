package main

import (
	"fmt"
)

func main() {
	fmt.Println("    `.-::::::-.`    ")
	fmt.Println(".:-::::::::::::::-:.")
	fmt.Println("`_:::    ::    :::_`")
	fmt.Println(" .:( ^   :: ^   ):. ")
	fmt.Println(" `:::   (..)   :::. ")
	fmt.Println(" `:::::::UU:::::::` ")
	fmt.Println(" .::::::::::::::::. ")
	fmt.Println(" O::::::::::::::::O ")
	fmt.Println(" -::::::::::::::::- ")
	fmt.Println(" `::::::::::::::::` ")
	fmt.Println("  .::::::::::::::.  ")
	fmt.Println("    oO:::::::Oo     ")

	//	Bubble sort stuff
	arr := []int{3, 91, 54, 7, 2, 46, 68, 5, 9, 20}
	fmt.Println("Array before bubble sort:")
	fmt.Println(arr)
	bubbleSort(arr)
	fmt.Println("Array after bubble sort:")
	fmt.Println(arr)

	//	Linear search stuff
	fmt.Println("Array to search:")
	fmt.Println(arr)
	fmt.Println("Searching for 46")
	index := linearSearch(arr, 46)
	if index == -1 {
		fmt.Println("Value was not found.")
	} else {
		fmt.Printf("Value was found in position %d\n\r", index)
	}
	fmt.Println("Searching for 150")
	index = linearSearch(arr, 150)
	if index == -1 {
		fmt.Println("Value was not found.")
	} else {
		fmt.Printf("Value was found in position %d\n\r", index)
	}

	//	Insertion sort stuff
	arr = []int{9, 12, 4, 124, 44, 6, 8, 1415, 19, 20}
	fmt.Println("Array before insertion sort alpha:")
	fmt.Println(arr)
	insertionSortAlpha(arr)
	fmt.Println("Array after insertion sort alpha:")
	fmt.Println(arr)

	arr = []int{9, 12, 4, 124, 44, 6, 8, 1415, 19, 20}
	fmt.Println("Array before insertion sort beta:")
	fmt.Println(arr)
	insertionSortBeta(arr)
	fmt.Println("Array after insertion sort beta:")
	fmt.Println(arr)
}

func bubbleSort(arr []int) []int {
	//	Bubble sort: Works from left to right, moving the largest value to the correct position in each pass.
	//	Time Complexity: Best - O(n) Average - O(n^2) Worst - O(n^2)

	//	Loop through the array until the array length is met
	for i := 0; i < len(arr); i++ {
		//  Loop through the array - iteration from prior loop as outer most value will be sorted already - 1 (index from 0)
		for j := 0; j < len(arr)-i-1; j++ {
			//  Compare value to the following position and swap if following value is smaller
			if arr[j] > arr[j+1] {
				//  Use arithmetic to swap values without needing a temp variable
				arr[j] = arr[j] + arr[j+1]
				arr[j+1] = arr[j] - arr[j+1]
				arr[j] = arr[j] - arr[j+1]
			}
		}
	}
	//	Return sorted array
	return arr
}

func linearSearch(arr []int, searchFor int) int {
	//  Linear search: Iterates through an array until the value is found or the array is fully traversed.
	//  Time Complexity: Best - O(1) Average - O(n) Worst - O(n)
	//  NOTE: Best case is when the value is in the first index.

	//  Iterate over array, comparing value at current index to value searched for
	for i := 0; i < len(arr); i++ {
		//  Return the index if the value is found
		if arr[i] == searchFor {
			return i
		}
	}
	//  Return -1 if the value is not found and the array is fully traversed
	return -1
}

func insertionSortAlpha(arr []int) []int {
	//  Insertion sort: Works from left to right, moving the current index value to the correct position in each pass.
	//  Time Complexity: Best - O(n) Average - O(n^2) Worst - O(n^2)

	//  Declare that i, j, current are type int
	var i, j, current int

	//  Loop starting at position 1 as the value at position 0 is theoretically in a "sorted" portion of the array
	for i = 1; i < len(arr); i++ {

		//  Define the current value to sort around
		current = arr[i]

		//  Set the second index to be current - 1
		j = i - 1

		//	While loops are not implemented in Go so an alternative approach must be used
		for j >= 0 && arr[j] > current {

			//  Perform swap
			arr[j+1] = arr[j]

			//  Decrement index value of j
			j -= 1
		}

		//  Move current value into second indexer + 1 to place in correct position
		arr[j+1] = current
	}

	return arr
}

func insertionSortBeta(arr []int) []int {
	//  Insertion sort: Works from left to right, moving the current index value to the correct position in each pass.
	//  Time Complexity: Best - O(n) Average - O(n^2) Worst - O(n^2)

	//  Loop starting at position 1 as the value at position 0 is theoretically in a "sorted" portion of the array
	for i := 1; i < len(arr); i++ {

		j := i

		//	While loops are not implemented in Go so an alternative approach must be used
		for j > 0 {
			//	If the value in position j is less than the value proceeding it, swap the values
			if arr[j] < arr[j-1] {
				//	Swap the values of index j and j-1
				arr[j], arr[j-1] = arr[j-1], arr[j]
			}

			//	Decrement j
			j -= 1
		}
	}
	//	Return sorted array
	return arr
}

func insertionSort(arr []int) []int {
	//  Insertion sort: Works from left to right, moving the current index value to the correct position in each pass.
	//  Time Complexity: Best - O(n) Average - O(n^2) Worst - O(n^2)

	//  Declare that i, j, current are type int
	var i, j, current int

	//  Loop starting at position 1 as the value at position 0 is theoretically in a "sorted" portion of the array
	for i = 1; i < len(arr); i++ {

		//  Define the current value to sort around
		current = arr[i]

		//  Set the second index to be current - 1
		j = i - 1

		//  Continue swapping whilst the value at index 2 is larger than current
		for j >= 0 && arr[j] > current {

			//  Perform swap
			arr[j+1] = arr[j]

			//  Decrement index value of j
			j -= 1
		}

		//  Move current value into second indexer + 1 to place in correct position
		arr[j+1] = current
	}

	return arr
}
