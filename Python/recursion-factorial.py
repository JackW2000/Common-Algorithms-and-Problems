#   Recursion in programming is a term used to describe when a function makes an internal call to itself.
#   This leads to the function repeating within itself.
#   This functionality must be controlled to avoid infinitely running code, which can lead to system crashes.
#   When implemented correctly, recursion can be extremely useful in reducing code repetition.
#   Below is an example of recursion being implemented to calculate a factorial of a number.
#   (Factorial is the value found for f(n) where f() is n * n-1 *n-2 ... * 1)
#   (i.e. the value is multiplied by one less each time until finally multiplied by 1)

def factorial(input_val):
    #   Verify that the input value is positive
    if input_val < 0:
        print("Cannot calculate factorial of a negative value")
        return

    #   If the value is larger than 0
    if input_val > 0:
        #   Return the input value * the return from the recursive call using value - 1
        return input_val * factorial(input_val - 1)
    else:
        #   Factorial of 0 is 1
        return 1


#   Driver code
if __name__ == "__main__":
    print(factorial(0))
    print(factorial(5))
    print(factorial(10))
    print(factorial(15))
