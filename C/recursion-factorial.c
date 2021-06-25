#define CRT_SECURE_NO_WARNINGS

#include <stdio.h>

//   Recursion in programming is a term used to describe when a function makes an internal call to itself.
//   This leads to the function repeating within itself.
//   This functionality must be controlled to avoid infinitely running code, which can lead to system crashes.
//   When implemented correctly, recursion can be extremely useful in reducing code repetition.
//   Below is an example of recursion being implemented to calculate a factorial of a number.
//   (Factorial is the value found for f(n) where f() is n * n-1 *n-2 ... * 1)
//   (i.e. the value is multiplied by one less each time until finally multiplied by 1)

//  Unsigned long long is used due to the exponential growth in size of values when calculating factorial values
//  In this case, factorial(15) would return an incorrect answer due to data type overflow if int or long it was used
//  Overflow is still possible in this system, however, this is a prof of concept for how recursion can be used
unsigned long long factorial(unsigned long int inputVal) {
    //   Verify that the input value is positive
    if (inputVal < 0) {
        printf("Cannot calculate factorial of a negative value");
        return 0;
    }


    //   If the value is larger than 0
    if (inputVal > 0) {
        //   Return the input value * the return from the recursive call using value - 1
        return inputVal * factorial(inputVal - 1);
    } else {
        //   Factorial of 0 is 1
        return 1;
    }

}

//  Driver program for testing the factorial function
int main() {
    printf("%llu\n\r", factorial(0));
    printf("%llu\n\r", factorial(5));
    printf("%llu\n\r", factorial(10));
    printf("%llu\n\r", factorial(15));

    return 0;
}
