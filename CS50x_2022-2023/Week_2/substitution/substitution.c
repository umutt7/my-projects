#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }//If the user won't enter a key while launching the program, the program will tell the usage of program and returns 1.
    else if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }//If the key doesn't contain 26 characters, the user will be informed and the program will return 1.

    string key = argv[1];

    for (int i = 0; i < 26; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (key[j] == key[i])
            {
                printf("The key has the same letter multiple times.\n");
                return 1;
            }//The key will be checked for the same letters.
        }
        if (isalpha(key[i]) == 0 && key[i] != '\n')
        {
            printf("The key contains invalid characters.\n");
            return 1;
        }//To check if the key contains invalid characters.
    }


    int diff = 0;

    string plaintext = get_string("plaintext: ");
    string ciphertext[strlen(plaintext)];

    printf("ciphertext: ");

    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        if (islower(plaintext[i]))
        {
            diff = (int) plaintext[i] - 97;
            printf("%c", tolower(key[diff]));
        }//If plaintext[i] is lowercase, the corresponding letter will be printed lowercase.
        else if (isupper(plaintext[i]))
        {
            diff = (int) plaintext[i] - 65;
            printf("%c", toupper(key[diff]));
        }//If plaintext[i] is uppercase, the corresponding letter will be printed uppercase.
        else
        {
            printf("%c", plaintext[i]);
        }//If plaintext[i] is not a letter, it will be printed as it is.
    }

    printf("\n");

    return 0;

}