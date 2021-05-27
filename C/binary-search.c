#define CRT_SECURE_NO_WARNINGS

#include <stdio.h>

//  Pass in the array, the value to search for,
//  the index of the start of the array, and the index of the end of the array
//  The passing of index values will allow the same array to be utilised throughout each
//  recursion, "filtering" out values that have been checked against by only looking between the indices
int binarySearch(int arr[], int searchFor, int startIndex, int endIndex) {
    //  Binary search: (Assumes array is sorted) Splits the array in half using the midpoint,
    //  halving the data to look at each time by ignoring values that are less than or larger than
    //  the value being searched for.
    //  Time Complexity: Best - O(1) Average - O(log(n)) Worst - O(log(n))

    //  Check that there is more than one value in the array (low != high)
    if (endIndex >= startIndex) {
        int mid = startIndex + (endIndex - startIndex) / 2;

        // Check if searchFor is in the middle, if it is then return the index
        if (arr[mid] == searchFor) {
            return mid;
        }

        //  Check if the value is less than that at the mid, if it is, only look at the values to the left
        //  If not, the value is either to the right or not present so look at the right half instead
        if (arr[mid] > searchFor) {
            return binarySearch(arr, searchFor, startIndex, mid - 1);
        } else {
            return binarySearch(arr, searchFor, mid + 1, endIndex);
        }
    }

    //  If the value is not found, return -1
    return -1;
}

//  Driver program for testing the binary search
int main() {
    //  Predefined array for demo purposes
    //  NOTE: Array must be pre-sorted for use with binary search
    int arr[10] = {5, 9, 24, 38, 99, 453, 511, 632, 712, 981};

    //  The following is a trick for finding the length of an array (assuming is it not reduced to a pointer)
    int arrLen = sizeof(arr) / sizeof(arr[0]);

    int searchFor;

    printf("Enter the value you'd like to search for: ");
    scanf("%d", &searchFor);

    int indexOf = binarySearch(arr, searchFor, 0, arrLen - 1);

    if (indexOf == -1) {
        printf("%d was not found within the array.\n\r", searchFor);
    } else {
        printf("%d was found at position %d (index %d)\n\r", searchFor, indexOf + 1, indexOf);
    }
}