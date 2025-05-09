#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float red = (float) image[i][j].rgbtRed;
            float green = (float) image[i][j].rgbtGreen;
            float blue = (float) image[i][j].rgbtBlue;

            float average = round((red + green + blue) / 3);

            image[i][j].rgbtRed = (int) average;
            image[i][j].rgbtGreen = (int) average;
            image[i][j].rgbtBlue = (int) average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            int tmp_red = image[i][j].rgbtRed;
            int tmp_green = image[i][j].rgbtGreen;
            int tmp_blue = image[i][j].rgbtBlue;

            image[i][j].rgbtRed = image[i][width - j - 1].rgbtRed;
            image[i][j].rgbtGreen = image[i][width - j - 1].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width - j - 1].rgbtBlue;

            image[i][width - j - 1].rgbtRed = tmp_red;
            image[i][width - j - 1].rgbtGreen = tmp_green;
            image[i][width - j - 1].rgbtBlue = tmp_blue;
        }
    } // The classic "swap" function
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE original[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            original[i][j] = image[i][j];
        } //The original image will be stored in a different 2D array
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float red = 0, green = 0, blue = 0;
            int count = 0;

            for (int x = i - 1; x <= i + 1; x++)
            {
                if (x >= 0 && x < height)
                {
                    for (int y = j - 1; y <= j + 1; y++)
                    {
                        if (y >= 0 && y < width)
                        {
                            count++;
                            red += (float) original[x][y].rgbtRed;
                            green += (float) original[x][y].rgbtGreen;
                            blue += (float) original[x][y].rgbtBlue;
                        }
                    }
                }
            } //That nested loop will check the main pixel with the ones next to it

            image[i][j].rgbtRed = (int) round(red / count);
            image[i][j].rgbtGreen = (int) round(green / count);
            image[i][j].rgbtBlue = (int) round(blue / count);

            //The average values of colors will be assigned here

        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    //RGBTRIPLE original[height + 2][width + 2];
    RGBTRIPLE original[height][width];

    int gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};
    //Sobel operator constants stored in array, so it will be easier to use

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            original[i][j] = image[i][j];
        } //The original image will be copied to another 2D array
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float gx_red = 0, gx_green = 0, gx_blue = 0;
            float gy_red = 0, gy_green = 0, gy_blue = 0;

            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    if (i + x < 0 || i + x >= height)
                    {
                        continue;
                    } //Check if columns go beyond the image
                    if (j + y < 0 || j + y >= width)
                    {
                        continue;
                    } //Check if rows go beyond the image

                    gx_red += (float) original[i + x][j + y].rgbtRed * gx[x + 1][y + 1];
                    gy_red += (float) original[i + x][j + y].rgbtRed * gy[x + 1][y + 1];
                    gx_green += (float) original[i + x][j + y].rgbtGreen * gx[x + 1][y + 1];
                    gy_green += (float) original[i + x][j + y].rgbtGreen * gy[x + 1][y + 1];
                    gx_blue += (float) original[i + x][j + y].rgbtBlue * gx[x + 1][y + 1];
                    gy_blue += (float) original[i + x][j + y].rgbtBlue * gy[x + 1][y + 1];
                }
            } //That nested loop will check the main pixel with the ones next to it

            int red = round((float)sqrt(gx_red * gx_red + gy_red * gy_red));
            int blue = round((float)sqrt(gx_blue * gx_blue + gy_blue * gy_blue));
            int green = round((float)sqrt(gx_green * gx_green + gy_green * gy_green));

            if (red > 255)
            {
                red = 255;
            }
            if (green > 255)
            {
                green = 255;
            }
            if (blue > 255)
            {
                blue = 255;
            } //To cap the limit to 255

            image[i][j].rgbtRed = red;
            image[i][j].rgbtGreen = green;
            image[i][j].rgbtBlue = blue;
        }
    }
    return;
}