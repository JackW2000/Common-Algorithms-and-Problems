#define CRT_SECURE_NO_WARNINGS

#include <stdio.h>

void bubbleSort(int arr[], int arrLen) {
    //  Bubble sort: Works from left to right, moving the largest value to the correct position in each pass.
    //  Time Complexity: Best - O(n) Average - O(n^2) Worst - O(n^2)

    //  Declare that i, j are type int
    int i, j;

    //  Loop through the array until the array length is met
    for (i = 0; i < arrLen; i++) {
        //  Loop through the array - iteration from prior loop as outer most value will be sorted already - 1 (index from 0)
        for (j = 0; j < arrLen - i - 1; j++) {

            //  Compare value to the following position and swap if following value is smaller
            if (arr[j] > arr[j + 1]) {

                //  Use arithmetic to swap values without needing a temp variable
                arr[j] = arr[j] + arr[j + 1];
                arr[j + 1] = arr[j] - arr[j + 1];
                arr[j] = arr[j] - arr[j + 1];
            }
        }
    }
}

//  Driver program for testing the bubble sort
int main() {
    int arr[100], arrLen, i;

    printf("Enter number of elements in the array: ");
    scanf("%d", &arrLen);

    printf("Enter %d integers\n", arrLen);

    for (i = 0; i < arrLen; i++) {
        scanf("%d", &arr[i]);
    }

    bubbleSort(arr, arrLen);

    printf("Printing the sorted array:\n");

    for (i = 0; i < arrLen; i++) {
        printf("%d\n", arr[i]);
    }

    return 0;
}
