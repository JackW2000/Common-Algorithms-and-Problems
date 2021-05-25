#define CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int linearSearch(int arr[], int arrLen, int searchFor) {
    //  Linear search: Iterates through an array until the value is found or the array is fully traversed.
    //  Time Complexity: Best - O(1) Average - O(n) Worst - O(n)
    //  NOTE: Best case is when the value is in the first index.

    //  Declare i as type int
    int i;

    //  Iterate over array, comparing value at current index to value searched for
    for (i = 0; i < arrLen; i++) {

        if (arr[i] == searchFor) {
            //  Return the index if the value is found
            return i;
        }
    }

    //  Return -1 if the value is not found and the array is fully traversed
    return -1;
}

//  Driver program for testing the linear search
int main() {
    int arr[100], arrLen, i, searchFor, result;

    printf("Enter number of elements in the array: ");
    scanf("%d", &arrLen);

    printf("Enter %d integers\n\r", arrLen);

    for (i = 0; i < arrLen; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter the value you'd like to search for: ");
    scanf("%d", &searchFor);

    result = linearSearch(arr, arrLen, searchFor);

    if (result != -1) {
        printf("%d was found in position %d (index %d).\n\r", searchFor, result + 1, result);
    } else {
        printf("%d was not found in the array.\n\r", searchFor);
    }

    return 0;
}