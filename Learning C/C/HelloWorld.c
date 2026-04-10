//This is a file using the C programming language. Here we are accessing a library called stdio.h.
//We use #include to include a header file that lets us use input/output functions like printf().

//Blank lines are ignored by C, we can use them to make them more readable for us.

#include <stdio.h>

//Here is a function, we call it by using int which means it will return a number and giving the function a name called main. Main is the starting function of every C program.
//We use curly brackets to execute the code inside them.
//Int main will always run on start.
int main() {
    //To print or get an output we use double quotes to tell the print that this is a string. (text)
    printf("Hello World");
    //We use return 0 to have an exit code. 0 means return success and tells the program to end. We will learn more about it later.
    return 0;
}

//Another example on how we can write this function is:
int main(){printf("Hello World"); return 0;}
//This however becomes hard to read if you're writing a lot of code.

//To break a line in C we use \n. This is an example.
int main() {
    prinft("Hello \n World");
    return 0;
}