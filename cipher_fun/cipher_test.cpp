#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <random>
#include <string>
#include <fstream>

using namespace std;

int main(int argc, char** args){
    FILE* f = fopen(args[1], "r");
    char c = fgetc(f);
    int key = 11;
    
    int mod = 25;
    int gap = 6;
    int offset_male = 97;
    int offset_velike = 65;
    
    key %= mod;
    int map[200];
    while ( c != EOF) {
        int shifted;
        // velika
        if(64 < c && c < 91){
            shifted = (c+key)%('Z'+1);
            if(shifted < offset_velike){
                shifted += offset_velike;
            }
        // mala 
        }else if(96 < c && c < 123){
            shifted = (c+key)%('z'+1);
            if(shifted < offset_male){
                shifted += offset_male;
            }
        // locilo
        }else{
            shifted = c;
        }
        if(c != shifted){
            printf("%c - > %c\n", c, shifted);

        }
        c = fgetc(f);
    }
    /*
    printf("\n\nMap:\n");
    for(int i=30; i<130; i++){
        printf("%d -> %c \n", i, i);
    }
    */

    return 0;
}   