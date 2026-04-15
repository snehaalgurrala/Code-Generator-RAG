#include <stdio.h>

/**
 * Checks if a number is even or odd in C.
 */
const char* checkEvenOdd(int number) {
    if (number % 2 == 0) {
        return "Even";
    } else {
        return "Odd";
    }
}
