#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>

char cargo[81][9];
void hardcode();
int heights[9] = {2, 7, 6, 6, 5, 7, 4, 3, 7};
//int heights[3] = {1, 2, 0};
void printarr();

int main(int argc, char* argv[])
{
    if(argc != 2)
    {
        return 1;
    }

    char* file = argv[1];
    FILE* fp = fopen(file, "r");
    if(fp == NULL)
    {
        return 1;
    }
    hardcode();
    printarr();
    for(int i = 0; i < 501; i++)
    {
        char line[30];
        fgets(line, 30, fp);
        int length = strlen(line);
        int amount = 0;
        int source = 0;
        int destination = 0;
        int counter = 0;
        for(int j = 0; j < length; j++)
        {
            if(isdigit(line[j]))
            {
                if(counter == 0)
                {
                    amount = line[j] - '0';
                    if(isdigit(line[j + 1]))
                    {
                        amount *= 10;
                        amount += line[j + 1] - '0';
                        j++;
                    }
                    counter++;
                }else if (counter == 1)
                {
                    source = line[j] - '0';
                    if(isdigit(line[j + 1]))
                    {
                        amount *= 10;
                        amount += line[j + 1] - '0';
                        j++;
                    }
                    counter++;
                }else if (counter == 2)
                {
                    destination = line[j] - '0';
                    if(isdigit(line[j + 1]))
                    {
                        amount *= 10;
                        amount += line[j + 1] - '0';
                        j++;
                    }
                    counter++;
                    break;
                }
            }
        }
        source--;
        destination--;
        //debugging
        printf("line %s\n", line);
        printf("source %i destination %i amount %i\n\n\n", source, destination, amount);
        for(int j = 0; j < amount; j++)
        {
            printf("source:%d char:%c dest:%d char:%c\n", source, cargo[heights[source]][source], destination, cargo[heights[destination]][destination]);
            printarr();  
            printf("swap\n\n");

            //swap code
            heights[destination]++;
            cargo[heights[destination]][destination] = cargo[heights[source]][source];
            cargo[heights[source]][source] = ' ';
            heights[source]--;



            printf("source:%d char:%c dest:%d char:%c\n", source, cargo[heights[source]][source], destination, cargo[heights[destination]][destination]);
            printarr();  
            printf("done\n\n\n\n");
        }

    }
    printarr();
    for(int i = 0; i < 9; i++)
    {
        printf("%c", cargo[heights[i]][i]);
        
    }
    printf("\n");
    return 0;

}

void printarr()
{
    printf("Cargo: \n");
    for(int k = 0; k < 9; k++)
    {
        printf("%d: %d : ", k, heights[k]);
        for(int l = 0; l <= heights[k]; l++)
        {

            printf("%c", cargo[heights[k] - l][k]);
        }
        printf("\n");
    }
}

void hardcode()
{


        /*
        [D]    
    [N] [C]    
    [Z] [M] [P]
    1   2   3 */
    /*
    cargo[0][0] = 'Z';
    cargo[0][1] = 'M';
    cargo[0][2] = 'P';
    cargo[1][0] = 'N';
    cargo[1][1] = 'C';
    cargo[1][2] = ' ';
    cargo[2][0] = ' ';
    cargo[2][1] = 'D';
    cargo[2][2] = ' ';
*/



    /*
        [C]             [L]         [T]
        [V] [R] [M]     [T]         [B]
        [F] [G] [H] [Q] [Q]         [H]
        [W] [L] [P] [V] [M] [V]     [F]
        [P] [C] [W] [S] [Z] [B] [S] [P]
    [G] [R] [M] [B] [F] [J] [S] [Z] [D]
    [J] [L] [P] [F] [C] [H] [F] [J] [C]
    [Z] [Q] [F] [L] [G] [W] [H] [F] [M]
    1   2   3   4   5   6   7   8   9 
    */
    cargo[0][0] = 'Z';
    cargo[0][1] = 'Q';
    cargo[0][2] = 'F';
    cargo[0][3] = 'L';
    cargo[0][4] = 'G';
    cargo[0][5] = 'W';
    cargo[0][6] = 'H';
    cargo[0][7] = 'F';
    cargo[0][8] = 'M';
    cargo[1][0] = 'J';
    cargo[1][1] = 'L';
    cargo[1][2] = 'P';
    cargo[1][3] = 'F';
    cargo[1][4] = 'C';
    cargo[1][5] = 'H';
    cargo[1][6] = 'F';
    cargo[1][7] = 'J';
    cargo[1][8] = 'C';
    cargo[2][0] = 'G';
    cargo[2][1] = 'R';
    cargo[2][2] = 'M';
    cargo[2][3] = 'B';
    cargo[2][4] = 'F';
    cargo[2][5] = 'J';
    cargo[2][6] = 'S';
    cargo[2][7] = 'Z';
    cargo[2][8] = 'D';
    cargo[3][0] = ' ';
    cargo[3][1] = 'P';
    cargo[3][2] = 'C';
    cargo[3][3] = 'W';
    cargo[3][4] = 'S';
    cargo[3][5] = 'Z';
    cargo[3][6] = 'B';
    cargo[3][7] = 'S';
    cargo[3][8] = 'P';
    cargo[4][0] = ' ';
    cargo[4][1] = 'W';
    cargo[4][2] = 'L';
    cargo[4][3] = 'P';
    cargo[4][4] = 'V';
    cargo[4][5] = 'M';
    cargo[4][6] = 'V';
    cargo[4][7] = ' ';
    cargo[4][8] = 'F';
    cargo[5][0] = ' ';
    cargo[5][1] = 'F';
    cargo[5][2] = 'G';
    cargo[5][3] = 'H';
    cargo[5][4] = 'Q';
    cargo[5][5] = 'Q';
    cargo[5][6] = ' ';
    cargo[5][7] = ' ';
    cargo[5][8] = 'H';
    cargo[6][0] = ' ';
    cargo[6][1] = 'V';
    cargo[6][2] = 'R';
    cargo[6][3] = 'M';
    cargo[6][4] = ' ';
    cargo[6][5] = 'T';
    cargo[6][6] = ' ';
    cargo[6][7] = ' ';
    cargo[6][8] = 'B';
    cargo[7][0] = ' ';
    cargo[7][1] = 'C';
    cargo[7][2] = ' ';
    cargo[7][3] = ' ';
    cargo[7][4] = ' ';
    cargo[7][5] = 'L';
    cargo[7][6] = ' ';
    cargo[7][7] = ' ';
    cargo[7][8] = 'T';
    cargo[8][0] = ' ';
    cargo[8][1] = ' ';
    cargo[8][2] = ' ';
    cargo[8][3] = ' ';
    cargo[8][4] = ' ';
    cargo[8][5] = ' ';
    cargo[8][6] = ' ';
    cargo[8][7] = ' ';
    cargo[8][8] = ' ';  
    //*/
}

