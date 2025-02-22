#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <random>
#include <string>
#include <fstream>

using namespace std;

// 12 red cubes, 13 green cubes, and 14 blue cubes
pair<int, int> map(string s){
    int num_start = s.find(" ")+1;
    int start = s.rfind(" ")+1;
    int count = stoi(s.substr(num_start, start-num_start));
    
    //cout << "c: " << count << endl;
    
    string color = s.substr(start, s.size()-start);
    //cout << color << endl;
    if(color == "red"){
        return make_pair(count, 0);
    }if(color == "green"){
        return make_pair(count, 1);
    }if(color == "blue"){
        return make_pair(count, 2);
    }
    return make_pair(-1, -1);
}

bool checkGame(string s, const int* m){
    size_t start = 0;
    size_t end = s.find(",", start);

    //const int r = 0; const int g = 1; const int b = 2;
    int outOfBag[] = {0, 0, 0};

    while(end != std::string::npos){
        //cout << s.substr(start, end-start) << endl;
        
        string gameStr = s.substr(start, end-start);
        pair<int, int> p = map(gameStr); // count, color
        outOfBag[p.second] += p.first;
        if(outOfBag[p.second] > m[p.second]){
            printf("too many %d balls\n", p.second);

            return false;
        }
        start = end+1;
        end = s.find(",", start);
    }
    //cout << s.substr(start) << endl;
    
    string gameStr = s.substr(start, end-start);
    pair<int, int> p = map(gameStr); // count, color
        outOfBag[p.second] += p.first;
        if(outOfBag[p.second] > m[p.second]){
            //printf("too many %d balls\n", p.second);
            return false;
        }

    return true;
}

int main(){
    ifstream iFile("../input.txt");
    //ifstream iFile("test01.in");
    
    const int max[] = {12, 13, 14};
    string line;
    int gameId = 1;
    int sum = 0;
    
    while ( getline(iFile, line) ) {
        cout << line << endl;
        size_t start = line.find(":");
        size_t end = line.find(";", start);
        bool isValid = true;
        
        while(end != std::string::npos){
            //cout << "+" << line.substr(start, end-start) << endl;

            string gameSet = line.substr(start, end-start);
            if(!checkGame(gameSet, max)){
                start = end+1;
                end = line.find(";", start);
                printf("game %d: not-valid\n", gameId);
                isValid = false;
                break;
                
            }

            start = end+1;
            end = line.find(";", start);
        }
        //cout << line.substr(start) << endl;
       
        string gameSet = line.substr(start, end-start);
        if(isValid && checkGame(gameSet, max)){
            sum += gameId;
            printf("game %d: valid\n", gameId);
        }
        /*
        */

        gameId++;
    }
    cout << "res: " << sum << endl;
    return 0;
}   