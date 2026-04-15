#include <iostream>
#include <string>

/**
 * Checks if a number is even or odd in C++.
 */
std::string checkEvenOdd(int number) {
    if (number % 2 == 0) {
        return "Even";
    } else {
        return "Odd";
    }
}
