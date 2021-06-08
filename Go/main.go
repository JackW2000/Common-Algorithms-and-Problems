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
