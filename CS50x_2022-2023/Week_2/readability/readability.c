#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
//A function to find number of letters in given string.
int count_words(string text);
//A function to find number of words in given string.
int count_sentences(string text);
//A function to find number of sentences in given string.

int main(void)
{
    string n = get_string("Text: ");
    int letters, words, sentences;
    float index, letters_per_words, sentences_per_words;
    //Because the Coleman-Liau index can have decimal results, we store those variables as floats.

    //printf("%s\n", n);

    letters = count_letters(n);
    words = count_words(n);
    sentences = count_sentences(n);

    letters_per_words = ((float) letters / words) * 100;
    sentences_per_words = ((float) sentences / words) * 100;

    index = round(0.0588 * letters_per_words - 0.296 * sentences_per_words - 15.8);
    //The Coleman-Liau index

    //printf("%i letters\n", letters);
    //printf("%i words\n", words);
    //printf("%i sentences\n", sentences);

    if (index > 16)
    {
        printf("Grade 16+\n");
    }//If the result of index is bigger than 16, "16+" will be printed.
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %.0f\n", index);
    }//Else, the rounded result will be printed.
}

int count_letters(string text)
{
    int letter = 0;

    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (islower(text[i]) || isupper(text[i]))
        {
            letter++;
        }//If the current character of the string is a lowercase or a uppercase character, letter counter will increase.
    }

    return letter;
}

int count_words(string text)
{
    int word = 0;

    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isspace(text[i]) || i == n - 1)
        {
            word++;
        }
    }//If the current character of the string is a whitespace character, or is the latest character, word counter will increase.

    return word;
}

int count_sentences(string text)
{
    int sentence = 0;

    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentence++;
        }
    }//If the current character of the string is a dot, exclamation point, or question mark, sentence counter will increase.

    return sentence;
}