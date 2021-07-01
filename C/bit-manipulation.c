#define CRT_SECURE_NO_WARNINGS

#include <stdio.h>

//  Driver program to demonstrate bit manipulation and bitwise logic
int main() {
    //  In C, there are 6 key bit manipulation operations, commonly referred to as termed as "Bitwise operators".

    //  The Bitwise & (AND) operator
    //  In Bitwise operation, the ampersand (&) acts as an AND
    //  It can be thought of as a logical and gate, taking two values and comparing each, bit by bit
    //  When both values are a 1, the output is also a 1
    //  In all other cases (1 and 0, 0 and 1, 0 and 0), the result is 0
    //  Essentially, only when both values being compared are true is the output true
    //  Below is an example to demonstrate this

    //  Declare and initialise values A and B (in this case as 110 and 50)
    int valueA, valueB, valueC;

    valueA = 110;
    valueB = 50;

    printf("Bitwise & (AND)\n\r");

    //  Output the values
    printf("%d\n\r", valueA);
    printf("%d\n\r", valueB);

    //  Output the result of performing a Bitwise & comparison of the values
    valueC = valueA & valueB;
    printf("%d & %d = %d\n\r", valueA, valueB, valueC);

    //  How does comparing 110 to 50 using & return 34?
    //  If you convert 110 to binary form, you get      0110 1110
    //  If you convert 50 to binary form, you get       0011 0010
    //  Comparing these using an and gate will return   0010 0010
    //  Convert 0010 0010 back to decimal and the result is  34


    //  The Bitwise | (OR) operator
    //  In Bitwise operation, the vertical bar (|) acts as an OR
    //  It can be thought of as a logical or gate, taking two values and comparing each, bit by bit
    //  When either or both values are a 1, the output is also a 1
    //  The only case to return a 0 would be if both values are a 0
    //  Essentially, when at least one value being compared is true is the output true
    //  Below is an example to demonstrate this

    //  Declare and initialise values D and E (in this case as 90 and 30)
    int valueD, valueE, valueF;

    valueD = 90;
    valueE = 30;

    printf("Bitwise | (OR)\n\r");

    //  Output the values
    printf("%d\n\r", valueD);
    printf("%d\n\r", valueE);

    //  Output the result of performing a Bitwise & comparison of the values
    valueF = valueD | valueE;
    printf("%d | %d = %d\n\r", valueD, valueE, valueF);

    //  How does comparing 90 to 30 using | return 94?
    //  If you convert 90 to binary form, you get       0101 1010
    //  If you convert 30 to binary form, you get       0001 1110
    //  Comparing these using an or gate will return    0101 1110
    //  Convert 0101 1110 back to decimal and the result is 94


    //  The Bitwise ^ (XOR) operator
    //  In Bitwise operation, the caret (^) acts as an XOR
    //  It can be thought of as a logical exclusive or gate, taking two values and comparing each, bit by bit
    //  When both values are a 0 or 1, the output is also a 0
    //  The gate returns a 1 only when exclusively one of the two values is a 1
    //  Essentially, only when one of the values being compared is true is the output true, otherwise it is false
    //  Below is an example to demonstrate this

    //  Declare and initialise values G and H (in this case as 85 and 70)
    int valueG, valueH, valueI;

    valueG = 85;
    valueH = 70;

    printf("Bitwise | (OR)\n\r");

    //  Output the values
    printf("%d\n\r", valueG);
    printf("%d\n\r", valueH);

    //  Output the result of performing a Bitwise & comparison of the values
    valueI = valueG ^ valueH;
    printf("%d ^ %d = %d\n\r", valueG, valueH, valueI);

    //  How does comparing 85 to 70 using ^ return 19?
    //  If you convert 90 to binary form, you get       0101 0101
    //  If you convert 30 to binary form, you get       0100 0110
    //  Comparing these using an or gate will return    0001 0011
    //  Convert 0001 0011 back to decimal and the result is 19


    //  The Bitwise ~ (NOT) operator
    //  In Bitwise operation, the tilde (~) acts as a NOT
    //  It can be thought of as a logical not gate, inverting each bit of the value
    //  When a bit is 1, it becomes 0 and when it is 0, it becomes 1
    //  This is the same as applying the 1's compliment rule to the value
    //  Below is an example to demonstrate this

    //  Declare and initialise values J (in this case as 15)
    int valueJ, valueK;

    valueJ = 15;

    printf("Bitwise ~ (NOT)\n\r");

    //  Output the values
    printf("%d\n\r", valueJ);

    //  Output the result of performing a Bitwise & comparison of the values
    valueK = ~valueJ;
    printf("~%d = %d\n\r", valueJ, valueK);

    //  How does applying ~ to 15 return -16?
    //  If you convert 15 to binary form, you get       0000 1111
    //  If you invert 0000 1111, you get                1111 0000
    //  Convert 1111 0000 back to decimal using 2s compliment and the result is -16
        //  2's compliment brief explanation:
        //  In 2's comp, the most significant bit (i.e. the one furthest left in binary form) is negative
        //  Take 1010 0000 (-96) for example
        //  If you apply headers starting with the right most value being 2 to the power 0
        //  with the power incrementing to the left (the 2nd left most value being 2 to the 1 etc)
        //  for each position to the right, you will find that for an 8 bit value, the headers are as follows:
        //  128, 64, 32, 16, 8, 4, 2, 1
        //  In 2's comp, as the MSB is treated as negative, the 128 becomes -128
        //  Therefore, the value 1010 0000 can be thought as being -128 + 0 + 32 + 0 + 0 + 0 + 0 + 0 = -96


    return 0;
}
