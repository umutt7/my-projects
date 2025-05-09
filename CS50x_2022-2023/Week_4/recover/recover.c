#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    } // If user didn't give us any argv, prompt this and return 1

    FILE *input_file = fopen(argv[1], "r");

    if (input_file == NULL)
    {
        printf("The file cannot be opened.\n");
        return 1;
    } // If the file cannot be opened, prompt this and return 1

    BYTE buffer[BLOCK_SIZE];
    // Assigning a buffer int with the size of BLOCK_SIZE = 512.

    int found = 0, jpg_count = 0;
    // found is to check if the assigned buffer contains the .jpg file
    // jpg_count to name the found .jpg files

    FILE *jpg_file = NULL;
    // The name of the jpg_file is currently null, nothing


    while (fread(buffer, BLOCK_SIZE, 1, input_file) == 1) // while the reading process continues...
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
            // If the first four elements of buffer is exactly like this...
        {
            if (found == 1)
            {
                fclose(jpg_file);
            }
            // If you previously found a jpg file before, close that, and create a new one in next steps
            else
            {
                found = 1;
            } // Assign 1 to found

            char jpg_name[8];
            // The name of the jpg files

            sprintf(jpg_name, "%03i.jpg", jpg_count);
            // Think like this as a dynamic string creator function...

            jpg_file = fopen(jpg_name, "a");
            // The jpg file be opened with the assigned name, "a" represents appending

            jpg_count++;
            // Increase the counter to assign new names for upcoming jpg files
        }

        if (found == 1)
        {
            fwrite(buffer, BLOCK_SIZE, 1, jpg_file);
            // If you found a buffer that belongs to a jpg, write the buffer to the jpg file
        }
    }

    fclose(input_file);
    fclose(jpg_file);
    // Close the files if they are still open

    return 0;

}