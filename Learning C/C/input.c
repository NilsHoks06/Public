//In this user input we will ask the user some questions and give an output.
//We are going to use the scanf() function to recieve data from an input.
//We will paste this data into variables.

#include <stdio.h>

int main() {
//We don't have to fill these out as they wil be filled out by the input using references.
//To not have an error we have to set a parameter in the string array.
char name[30];
int age;

printf("What is your name?: \n");

//Here we have to specify the data type we are using and referencing to the variable we want to insert the data to.
//For strings, the array name already acts as a pointer, so we don't use &
scanf("%s", name);

printf("What is your age?: \n");
//Here we are using a pointer
scanf("%d", &age);

printf("Your name is: %s\n", name);
printf("Your age is: %d\n", age);

//If you want the result on the same line or same page you can also insert them like this:
printf("Your name is %s and your age is %d", name, age)
//This would give the result of name and age in the same output.

//Here we have another example of getting both a number and character.
int myNum;
char myChar;

printf("Please write a number and a character.\n");

scanf("%d\n%c", &myNum, &myChar);

printf("Your number is: %d\n", myNum);
printf("Your character is: %c\n", myChar);

return 0;

}