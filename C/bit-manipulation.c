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


    //  The Bitwise << (LEFT SHIFT) operator
    //  In Bitwise operation, a double less than sign (<<) acts as a left shift
    //  This will shift all bits x positions to the left, where x is an integer value
    //  Below is an example to demonstrate this

    //  Declare and initialise values L (in this case as 25)
    int valueL, valueM;

    valueL = 25;

    printf("Bitwise << (LEFT SHIFT)\n\r");

    //  Output the values
    printf("%d\n\r", valueL);

    //  Output the result of performing a Bitwise & comparison of the values
    valueM = valueL << 2;
    printf("%d << 2 = %d\n\r", valueL, valueM);

    //  How does applying << 2 to return 100?
    //  If you convert 25 to binary form, you get           0001 1001
    //  If you shift all bits 2 spaces to the left, you get 0110 0100
    //  Convert 0110 0100 back to decimal and the result is 100


    //  The Bitwise >> (RIGHT SHIFT) operator
    //  In Bitwise operation, a double greater than sign (>>) acts as a right shift
    //  This will shift all bits x positions to the right, where x is an integer value
    //  Below is an example to demonstrate this

    //  Declare and initialise values M (in this case as 152)
    int valueN, valueO;

    valueN = 152;

    printf("Bitwise >> (RIGHT SHIFT)\n\r");

    //  Output the values
    printf("%d\n\r", valueN);

    //  Output the result of performing a Bitwise & comparison of the values
    valueO = valueN >> 3;
    printf("%d >> 3 = %d\n\r", valueN, valueO);

    //  How does applying >> 3 to return 19?
    //  If you convert 152 to binary form, you get           1001 1000
    //  If you shift all bits 3 spaces to the right, you get 0001 0011
    //  Convert 0001 0011 back to decimal and the result is 19

    //  NOTE: For both Bitwise Shift operations, values do not wrap
    //  This means that if a 1 or 0 is shifted to exceed the size limitation of the value, the value is lost
    //  E.g. 0000 1010 >> 3 = 0000 0001 - In this case, the initial 010 are lost as they have been shifted out

    //  Bit Masking - A concept utilising Bitwise manipulation
    //  Bit masking is the idea that a value can have a "mask" applied using bitwise manipulation
    //  This concept can be applied to achieve a variety of things, such as:
    //  - Extracting a subset of bits
    //  - Toggling a subset of bits
    //  - Setting a subset of bits
    //  For example, if we treat an 8 bit value as being 8 switches, where 0 means off and 1 means on
    //  we can say that in the pattern 0100 0011 that switches 2, 7, 8 are on (left to right counting from 1)
    //  But what if we wanted to do more with this value? Masking allows this in a variety of ways
    //  Below are some examples

    //  Example 1 - AND masking

    //  Declare and initialise values P (in this case as 0110 1100 (108 decimal))
    //  For this example, lets say that we want to check the state of bits 2 and 5
    //  To achieve this using an AND, we must remember that the value being used to mask must also be set to 1 in positions 2 and 5
    //  Therefore, we initialise Q as 0100 1000 (72 decimal)
    int valueP, valueQ, valueR;

    valueP = 108;
    valueQ = 72;

    printf("Bitwise AND mask\n\r");

    //  Output the values
    printf("%d\n\r", valueP);
    printf("%d\n\r", valueQ);

    //  Output the result of performing a Bitwise & comparison of the values
    valueR = valueP & valueQ;
    printf("%d & %d = %d\n\r", valueP, valueQ, valueR);

    //  So what does this tell us?
    //  In this case, the result being 72 tells us that for the value being
    //  masked, both the bit in position 2 and 5 are 1
    //  We can say this as if either was 0, the resultant value would not match
    //  the mask value as a 0 would have been returned
    //  Written explanation:
    //  0110 1100 (108)
    //  0100 1000 (72)
    //  Apply an AND operation
    //  0100 1000 (72)
    //  The values of the bits in decimal are not relevant here, this is specifically used to check the status of a bit


    //  Example 2 - OR masking

    //  Declare and initialise values S (in this case as 1100 1011 (203 decimal))
    //  For this example, lets say that we want to set bits 3, 6, and 7 to be on
    //  To achieve this using an OR, we must remember that the value being used to mask must also be set to 1 in positions 3, 6 and 7
    //  Therefore, we initialise T as 0010 0110 (38 decimal)
    int valueS, valueT, valueU;

    valueS = 203;
    valueT = 38;

    printf("Bitwise OR mask\n\r");

    //  Output the values
    printf("%d\n\r", valueS);
    printf("%d\n\r", valueT);

    //  Output the result of performing a Bitwise & comparison of the values
    valueU = valueS | valueT;
    printf("%d | %d = %d\n\r", valueS, valueT, valueU);

    //  So what does this tell us?
    //  In this case, the result being 239 tells us that for the value being
    //  masked, bits 3, 6 and 7 are now true
    //  Written explanation:
    //  1100 1011 (203)
    //  0010 0110 (38)
    //  Apply an OR operation
    //  1110 1111 (239)
    //  The values of the bits in positions 3, 6 and 7 are now all set to 1


    //  Example 3 - XOR masking

    //  Declare and initialise values V (in this case as 1010 1010 (170 decimal))
    //  For this example, lets say that we want to turn on bits 2 and 4, and turn off bit 7 (we know that this is on)
    //  To achieve this using an XOR, we must remember that the value being used to mask must also be set to 1 in positions 2, 4 and 7
    //  Therefore, we initialise W as 0101 0010 (82 decimal)
    int valueV, valueW, valueX;

    valueV = 170;
    valueW = 82;

    printf("Bitwise XOR mask\n\r");

    //  Output the values
    printf("%d\n\r", valueV);
    printf("%d\n\r", valueW);

    //  Output the result of performing a Bitwise & comparison of the values
    valueX = valueV ^ valueW;
    printf("%d ^ %d = %d\n\r", valueV, valueW, valueX);

    //  So what does this tell us?
    //  In this case, the result being 248 tells us that for the value being
    //  masked, bits 2, 4 and 7 have been flipped
    //  Written explanation:
    //  1010 1010 (170)
    //  0101 0010 (82)
    //  Apply an XOR operation
    //  1111 1000 (239)
    //  The values of the bits in positions 2, 4 and 7 are now inverted


    //  The masking examples show how a value's bits can be utilised as toggles and flags
    //  and that the value of a specific bit can be viewed and adjusted through the use of bitwise manipulation

    return 0;
}
