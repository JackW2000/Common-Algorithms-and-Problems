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

	arr := []int{3, 91, 54, 7, 2, 46, 68, 5, 9, 20}

	fmt.Println("Array before bubble sort:")
	fmt.Println(arr)
	bubblesort(arr)
	fmt.Println("Array after bubble sort:")
	fmt.Println(arr)
}

//	Function
func bubblesort(arr []int) []int {
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
