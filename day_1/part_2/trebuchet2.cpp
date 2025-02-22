#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <random>
#include <string>
#include <fstream>

using namespace std;


int main(){
    ifstream iFile("input.txt");
    //ifstream iFile("test02.in");
    string digits[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int addvalue[] = {1,2,3,4,5,6,7,8,9};
    //int i = 0;
    long sum = 0;
    while (1) {
        
        if( iFile.eof() ) break;
        int* match = (int*)calloc(10, sizeof(int));
        string x; int k = 0; iFile >> x;
        
        cout << x << endl; //cout
        
        int j = 0;
        int lastDig = 0;
        while(x[j] != '\0'){
            if(k == 0 && isdigit(x[j]) && x[j] != '0'){
                k = x[j] - '0';
                lastDig = k;
                for(int w = 0; w < 9; w++){
                    match[w] = 0;
                }
                //cout << "fist: " << k << endl;
            }else if(isdigit(x[j]) && x[j] != '0'){
                
                lastDig = x[j] - '0';
                for(int w = 0; w < 9; w++){
                    match[w] = 0;
                }
                //cout << "second: " << lastDig << endl;
            }else{
                int found = 0;
                for(int digIx = 0; digIx < 9; digIx++){

                   
                    cout << "x: " << x[j] << " d: " << digits[digIx][match[digIx]]<< "-- "<< digits[digIx] << endl;
                    if(digits[digIx][match[digIx]] == x[j]) match[digIx]++;
                    else if(digits[digIx][0] != x[j]){
                        match[digIx] = 0;

                    }
                    if(match[digIx] == digits[digIx].length()){
                        if(k == 0){
                            found = 1;
                            k = addvalue[digIx];
                            lastDig = addvalue[digIx];
                        }else{
                            
                            lastDig = addvalue[digIx];
                        }
                        //cout << "k: " << k << endl;
                        cout << digits[digIx] << endl;
                        //cout << x[j] << endl;
                    }
                }
                if(found){
                    for(int w = 0; w < 9; w++){
                        match[w] = 0;
                    }
                }
            }
            //cout << "-------" << endl;
            j++;
        }
        k *= 10;
        k += lastDig;
        sum += k;
        //cout << "end: " << k << endl;
        //i++;
    }
    cout << sum << endl;
    return 0;
}