//In this part of the C program, i'm gonna tell you how to change a value.
#include <stdio.h>

//As of now the value is 100
int value = 100; //Global variable.




int value1() {
    //If i wanted to change the value only for the function i would need to use int.
    int value = 20;
    //If i were to print the value the following result would be 20.
    //You must remember to use double quotes and declare the type you're trying to print.
    printf("%d", value);

    return 0;
}

//If i were to print now i would change the value globally to 30. This would only happen if second() would run before third()
//Running this changes it for the rest of the program, be careful using this.
int value2() {
    value = 30;
    printf("%d", value);

    return 0;
}

int value3() {
    //If i call value now it would be 30.
    printf("%d", value);

    return 0;
}

int value4() {
    //I can also add value to the global value
    int anothervalue = 50;
    value = value + anothervalue;
    printf("%d", value);

    return 0;

}

//It would look like this:

int main() {

    //We start off with the value of 100
    printf("%d", value);

    value1(); //Now we locally print 20 keeping the global value 100.
    printf("%d", value);
    
    value2(); //Now we will change the global value to 30.

    value3(); //Now when printing the value it will still be 30.

    value4(); //This will return 80.
    return 0;
}