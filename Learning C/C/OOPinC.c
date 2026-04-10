//The C programming language doesn't directly have Object-Oriented Programming like C++, it's descendant. 
//So what is Object-Oriented Programming (OOP)? How do we simulate OOP in C?
//Object-Oriented Programming is a way to group data like adding attributes and functions into objects. Think of a car, it has a color, manufacturer, model, etc.

//In this case we will simulate an OOP by using struct like a class. This is how to manually make an OOP.

#include <stdio.h>
#include <string.h>


//We use struct (Structure) to simulate a class. We give the name Car to ensure that people reading the code understands it's a car.
//Without typedef, we must use 'struct Car' every time we declare a variable
struct Car
{
    //Here we give variables to the class with attributes.
    char color[20];
    char manufacturer[50];
    char model[50];
    int year;
};

//Here we use void to declare our return type. Which will showcase our object's data.
//The issue here is that although it works, it copies the whole structure... I'll show how to get around that.
void displayCar(const struct Car c) {
    printf("Car information:\n");
    printf("Color: %s\n", c.color);
    printf("Manufacturer: %s\n", c.manufacturer);
    printf("Model: %s\n", c.model);
    printf("Year: %d\n", c.year);
}

int main() {
    //Here we create the object as Car1.
    struct Car Car1;

    strcpy(Car1.color, "Blue");
    strcpy(Car1.manufacturer, "Ford");
    strcpy(Car1.model, "GT500");
    Car1.year = 1967;

    displayCar(Car1);
    
    return 0;
}


//This is an improved version. I'll explain why.
//Here we use typedef it lets us declare variables as Vehicle directly, without repeating the struct keyword.
typedef struct Vehicle
{
    //Here we give variables to the class with attributes.
    char vehicleType[50];
    char color[20];
    char manufacturer[50];
    char model[50];
    int year;
} Vehicle;

//We are also going to use * to create a pointer. *v is what it will be, it holds the memory address for the structure rather than having a copy of it. This improves efficiency.
//Const makes sure the data can't be modified through the pointer.
void displayVehicle(const struct Vehicle *v) {
    printf("Car information:\n");
    //Here we use the arrow operators to follow the address and access the fields individually. 
    printf("Vehicle Type %s\n", v->vehicleType);
    printf("Color: %s\n", v->color);
    printf("Manufacturer: %s\n", v->manufacturer);
    printf("Model: %s\n", v->model);
    printf("Year: %d\n", v->year);
}

int main() {
    //Here we create the object as Vehicle1. Notice how i didn't have to use struct?
    //We get to write Vehicle instead of using struct.
    Vehicle Vehicle1;
    strcpy(Vehicle1.vehicleType, "Car");
    strcpy(Vehicle1.color, "Blue");
    strcpy(Vehicle1.manufacturer, "Ford");
    strcpy(Vehicle1.model, "GT500");
    Vehicle1.year = 1967;

    //& oasses the memory address of Vehicle1 rather than the copy of it.
    displayVehicle(&Vehicle1);
    
    return 0;
}