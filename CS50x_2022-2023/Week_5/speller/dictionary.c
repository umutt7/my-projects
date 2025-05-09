// Implements a dictionary's functionality

// To convert my pseudocode to actual codes, I got some help from the website below:
// gist.github.com/choaimeloo/ffb96f7e43d67e81f0d44c08837f5944

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <strings.h>
#include <stdlib.h>

#include "dictionary.h"

int word_count = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 10000;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    char get_word[LENGTH + 1];
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        get_word[i] = toupper(word[i]);
    }

    get_word[strlen(word)] = '\0';

    // Get the hash value
    int h = hash(word);

    // Create a pointer to get into the hashtable[hash value]
    node *pointing = table[h];

    while (pointing != NULL)
    {
        // If the words are same, return true
        if (strcasecmp(pointing->word, word) == 0)
        {
            return true;
        }
        // Else, go next
        else
        {
            pointing = pointing->next;
        }
    }
    return false;
}

// Hashes word to a number
// Sum of first four letters' ASCII numbers
unsigned int hash(const char *word)
{
    long sum = 0;

    for (int i = 0; i < strlen(word); i++)
    {
        sum += toupper(word[i]);
    }

    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dictionary
    FILE *dict = fopen(dictionary, "r");

    // If cannot be opened...
    if (dict == NULL)
    {
        return false;
    }

    // Create a word string to write the words from dictionary
    char word[LENGTH + 1];

    // While dictionary ends...
    while (fscanf(dict, "%s", word) != EOF)
    {
        // Allocate new memory for a new node
        node *new_node = malloc(sizeof(node));

        // If cannot be allocated...
        if (new_node == NULL)
        {
            unload();
            return false;
        }

        // Copy the words from dictionary to word string
        strcpy(new_node->word, word);

        new_node->next = NULL;

        // Calculate the index of word to insert it in hash
        int h = hash(new_node->word);

        // Initialize head to point to hash index or bucket
        node *head = table[h];

        // Insert a new node at the beginning of hash
        if (head == NULL)
        {
            table[h] = new_node;
            word_count++;
        }
        else
        {
            new_node->next = table[h];
            table[h] = new_node;
            word_count++;
        }
    }

    fclose(dict);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // Words will be counted as we load the dictionary
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        // Assign cursor
        node *n = table[i];
        // Loop through linked list
        while (n != NULL)
        {
            // Make temp equal cursor;
            node *tmp = n;
            // Point cursor to next element
            n = n->next;
            // free temp
            free(tmp);
        }
        if (n == NULL && i == N - 1)
        {
            return true;
        }
    }
    return false;
}
