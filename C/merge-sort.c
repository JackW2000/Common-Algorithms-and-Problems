#define CRT_SECURE_NO_WARNINGS

#include <stdio.h>

//  Function for merging subarrays into a singular array
void merge(int arr[], int start_index, int midpoint, int end_index) {

    //  Declare iterators
    int main_iterator, left_iterator, right_iterator;

    //  Calculate length of each split
    int left_split_len = midpoint - start_index + 1;
    int right_split_len = end_index - midpoint;

    //  Declare temporary arrays using the lengths calculated
    int left_split[left_split_len], right_split[right_split_len];

    //  Copy data to temporary arrays
    //  (As passing an array in C turns it into a pointer, split arrays are created using passed indices instead)
    for (left_iterator = 0; left_iterator < left_split_len; left_iterator++)
        //  Start index is the first index of the left portion and left iterator counts to the length of the split
        left_split[left_iterator] = arr[start_index + left_iterator];

    for (right_iterator = 0; right_iterator < right_split_len; right_iterator++)
        //  Midpoint is the first index of the right portion and right iterator counts to the length of the split
        //  +1 will exclude the midpoint itself as it is in the left split
        right_split[right_iterator] = arr[midpoint + 1 + right_iterator];

    //  The following will merge the subarrays back into a main array
    left_iterator = 0; // Initial index of first subarray
    right_iterator = 0; // Initial index of second subarray
    main_iterator = start_index; // Initial index of merged subarray

    //  While the iterators are not at the end of each half
    while (left_iterator < left_split_len && right_iterator < right_split_len) {
        //  Compare the value of the left half at the index to that of the right half
        //  at it's respective index
        if (left_split[left_iterator] <= right_split[right_iterator]) {
            //  If the value in the left split is less than that of the right split
            //  set the current index value for the main array to hold the value of the left split
            arr[main_iterator] = left_split[left_iterator];

            //  Increment through the left split
            left_iterator++;
        } else {
            //  If the value in the right split is less than that of the left split
            //  set the current index value for the main array to hold the value of the right split
            arr[main_iterator] = right_split[right_iterator];

            //  Increment through the right split
            right_iterator++;
        }
        //  Increment to the next position in the main array
        main_iterator++;
    }

    //  Whilst the left index is not at the end of the array
    while (left_iterator < left_split_len) {
        //  Set the value at the main array index to that of the left split
        arr[main_iterator] = left_split[left_iterator];

        //  Increment the left and main array index values
        left_iterator++;
        main_iterator++;
    }

    //  Whilst the right index is not at the end of the array
    while (right_iterator < right_split_len) {
        //  Set the value at the main array index to that of the right split
        arr[main_iterator] = right_split[right_iterator];

        //  Increment the right and main array index values
        right_iterator++;
        main_iterator++;
    }
}

//  Start index is the start of the array and end index is the end of the array
//  By passing different indices, different portions of the list could be sorted
void mergeSort(int arr[], int start_index, int end_index) {
    //  Merge sort: Recursively divides the array, comparing subarrays and rebuilding a sorted array.
    //  Time Complexity: Best - O(n log(n)) Average - O(n log(n)) Worst - O(n log(n))

    int midpoint;

    if (start_index < end_index) {
        // Same as (start_index+end_index)/2, but avoids overflow for
        // large start_index and h
        midpoint = start_index + (end_index - start_index) / 2;

        //  Sort the left split (this will be start index (0) to midpoint)
        mergeSort(arr, start_index, midpoint);
        //  Sort the right split (this will be midpoint + 1 to end)
        mergeSort(arr, midpoint + 1, end_index);

        //  Merge the sorted arrays by passing the start, midpoint, and end indices
        //  (Due to C deprecating an array to a pointer when passed as a parameter,
        //  Indices are provided for the one array to allow in-place editing)
        merge(arr, start_index, midpoint, end_index);
    }
}

//  Driver program for testing the merge sort
int main() {
    int arr[100], arrLen, i;

    printf("Enter number of elements in the array: ");
    scanf("%d", &arrLen);

    printf("Enter %d integers\n\r", arrLen);

    for (i = 0; i < arrLen; i++) {
        scanf("%d", &arr[i]);
    }

    mergeSort(arr, 0, arrLen);

    printf("Printing the sorted array:\n\r");

    for (i = 0; i < arrLen; i++) {
        printf("%d\n\r", arr[i]);
    }

    return 0;
}
