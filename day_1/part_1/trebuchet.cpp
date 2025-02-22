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

    //int i = 0;
    long sum = 0;
    while (1) {
        
        if( iFile.eof() ) break;
        string x; int k = 0; iFile >> x;
        //cout << x << endl;
        
        int j = 0;
        int lastDig = 0;
        while(x[j] != '\0'){
            if(k == 0 && isdigit(x[j])){
                k = x[j] - '0';
                lastDig = k;
                //cout << "fist: " << k << endl;
            }else if(isdigit(x[j])){
                
                lastDig = x[j] - '0';
                //cout << "second: " << lastDig << endl;
            }
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