//  Driver code to demo implementations
fun main(args: Array<String>) {
    var arr: IntArray
    var index: Int

    //  Bubble sort stuff

    println("Bubble sort:")

    arr = intArrayOf(86, 231, 54, 213, 6, 23, 5345, 34, 5411, 3)

    println("Unsorted array:")
    println(arr.contentToString())

    BubbleSort.bubbleSort(arr)

    println("Sorted array:")
    println(arr.contentToString())


    //  Insertion sort stuff

    println("Insertion sort:")

    arr = intArrayOf(541, 114, 24, 75, 16, 2254, 44, 975, 8, 244)

    println("Unsorted array:")
    println(arr.contentToString())

    InsertionSort.insertionSort(arr)

    println("Sorted array:")
    println(arr.contentToString())

    //  Merge sort stuff

    println("Merge sort:")

    arr = intArrayOf(4, 747, 1, 4564, 6, 54, 412, 95, 18, 24)

    println("Unsorted array:")
    println(arr.contentToString())

    MergeSort.mergeSort(arr)

    println("Sorted array:")
    println(arr.contentToString())

    //  Linear search stuff

    println("Linear search:")

    arr = intArrayOf(114, 2, 124, 445, 2226, 945, 213, 5, 11, 4474)

    println("Array:")
    println(arr.contentToString())

    index = LinearSearch.linearSearch(arr, 945)

    if (index == -1) {
        println("Value not found in array.")
    } else {
        println("Value found at position ${index + 1} (index: $index)")
    }

    //  Binary search stuff

    println("Binary search:")

    arr = intArrayOf(5, 12, 14, 45, 61, 95, 100, 125, 451, 474)

    println("Array:")
    println(arr.contentToString())

    index = BinarySearch.binarySearch(arr, 45, 0, arr.size)

    if (index == -1) {
        println("Value not found in array.")
    } else {
        println("Value found at position ${index + 1} (index: $index)")
    }

    //  Quick sort stuff

    //  Alpha is a similar implementation to that in the Java
    println("Quick sort alpha:")

    arr = intArrayOf(546, 4, 345, 76, 5, 678, 12, 1, 75, 3)

    println("Unsorted array:")
    println(arr.contentToString())

    QuickSort.quickSortAlpha(arr, 0, arr.size - 1)

    println("Sorted array:")
    println(arr.contentToString())

    //  Beta utilises inbuilt functions within Kotlin but does not work in place
    println("Quick sort beta:")

    arr = intArrayOf(45, 786, 4, 6456, 87, 6, 786, 3, 5, 47)

    println("Unsorted array:")
    println(arr.contentToString())

    arr = QuickSort.quickSortBeta(arr)

    println("Sorted array:")
    println(arr.contentToString())
}