#include <cs50.h>
#include <stdio.h>

void bricks(int n);
//# koymak için hazırlanan bir fonksiyon, n kadar #

int main(void)
{
    int h;
    do
    {
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);
    //1 ve 8 arasında input almak için do-while

    for (int i = 0; i < h; i++)
    {
        //Baştaki boşluk sayısı için özel for
        for (int j = 0; j < h - i - 1; j++)
        {
            printf(" ");
        }
        bricks(i + 1);
        //Piramidin sol kısmı
        printf("  ");
        //Ortadaki iki boşluk
        bricks(i + 1);
        //Piramidin sağ kısmı
        printf("\n");
        //Satır sonu
    }
}

void bricks(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("#");
    }
}