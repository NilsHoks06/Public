/*
int is a data type used to store whole numbers, and also used as the return type of main()
Char is used to store a single character, to write a string we must use []. Remember to use double quotations for strings.
Float is like an integer, but it lets us use decimals to write stuff like 3.14. It's useful for accurate math.

To write the code correctly we have to use format specifiers. 
For a string we would use %s.
For a character we would use %c
For an integer it would be %d
For a float we would use %f.
*/

#include <stdio.h>

int main() {
    //These are local values.
    //This is an example of a string
    char firstName[] = "John";
    char lastName[] = "Pork";
    //This is an integer
    int age = 22;
    //This is a character
    char grade = 'B';
    //This is a float.
    float feesDue = 26.3;

    //Here we have to use two string formats to ensure that both firstName and lastName will show up. If we forget this it would only print out firstName.
    printf("Hello, %s %s\n", firstName, lastName);
    
    printf("Due to an error we would like to check if your information is correct.\n");
    
    printf("Are you %d years old?\n", age);
    
    printf("Is your grade %c?\n", grade);

    // We can limit decimals to two places using %.2f
    printf("Your fees due are %.2f$?\n", feesDue);

    //return 0; tells the program to end successfully.
    return 0;

}