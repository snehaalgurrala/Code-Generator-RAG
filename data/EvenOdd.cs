using System;

/**
 * Checks if a number is even or odd in C# (.NET).
 */
public class EvenOddProgram
{
    public static string CheckEvenOdd(int number)
    {
        if (number % 2 == 0)
        {
            return "Even";
        }
        else
        {
            return "Odd";
        }
    }
}
