#include <cs50.h>
#include <stdio.h>
#include <math.h>

long card = 0;

int digit_finder(long n);
//A function that finds how many digits in the given long-type input

int main(void)
{
    long card_temp;
    long starting_digits = 0;
    long sum = 0, checksum = 0, digits, temp;

    card = get_long("Number: ");

    digits = digit_finder(card);
    //To use in a for loop, we find the number of digits in given card number.

    if (digits < 17 && digits > 12)
    {
        card_temp = card;
        //To use the given card number in next processes without changing the original number, we assign the same value to a temporary number.
        //By doing that, we can make operations and change the value if needed without changing the original card number.

        for (int i = 1; i <= digits; i++)
        {
            if (i % 2 == 1)
            {
                checksum += card_temp % 10;
            } //If the digit is in the last, third to last, fifth to last, etc, the value will be directly used in Luhn's algorithm.
            else
            {
                temp = card_temp % 10;
                if (temp * 2 > 9)
                {
                    sum += (temp * 2 % 10) + (temp * 2 / 10);
                }
                else
                {
                    sum += temp * 2;
                }
            } //If the digit is in second to last, fourth to last, sixth to last, etc, the value needs to be processed to be used in Luhn's algorithm.
            //After the processes, the summary of those numbers will be stored in a temporary sum value.
            //When all the processes are over, sum and checksum will be added up.

            if (card_temp > 9 && card_temp < 100)
            {
                starting_digits += card_temp;
            } //That will help us to determine the very first two digits of the given card number.
            //It's required to determine the brand of the cards.

            card_temp = card_temp / 10;
        }

        //printf("Starting digits: %li and %li\n", starting_digits, starting_digits / 10);
        //printf("Sum and checksum: %li and %li\n", sum, checksum);
        //These are my controlling codes.

        if ((sum + checksum) % 10 == 0)
        {
            if ((digits == 15) && (starting_digits == 34 || starting_digits == 37))
            {
                printf("AMEX\n");
            }
            else if ((digits == 16) && (starting_digits < 56 && starting_digits > 50))
            {
                printf("MASTERCARD\n");
            }
            else if ((digits == 13 || digits == 16) && (starting_digits / 10 == 4))
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        } // If the ones digit of the result of sum+checksum is zero, it's a valid card. To find the brand, there are also some conditionals.
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

int digit_finder(long n)
{
    int digits = 0;

    do
    {
        digits++;
        n /= 10;
    }
    while (n != 0);

    return digits;
} // A typical digit counter.
