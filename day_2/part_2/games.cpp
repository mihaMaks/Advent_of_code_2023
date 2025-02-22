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
    string color = s.substr(start, s.size()-start);
    if(color == "red"){
        return make_pair(count, 0);
    }if(color == "green"){
        return make_pair(count, 1);
    }if(color == "blue"){
        return make_pair(count, 2);
    }
    return make_pair(-1, -1);
}

void checkGame(string s, const int* m, int* minimum){
    size_t start = 0;
    size_t end = s.find(",", start);

    //const int r = 0; const int g = 1; const int b = 2;
    int outOfBag[] = {0, 0, 0};

    while(end != std::string::npos){
        string gameStr = s.substr(start, end-start);
        pair<int, int> p = map(gameStr); // count, color
        outOfBag[p.second] += p.first;
        if(outOfBag[p.second] > minimum[p.second]){
            minimum[p.second] = outOfBag[p.second];
        }
        start = end+1;
        end = s.find(",", start);
    }
    string gameStr = s.substr(start, end-start);
    pair<int, int> p = map(gameStr); // count, color
    outOfBag[p.second] += p.first;
    if(outOfBag[p.second] > minimum[p.second]){
        minimum[p.second] = outOfBag[p.second];
    }
}

int main(){
    ifstream iFile("../input.txt");
    const int max[] = {12, 13, 14};
    string line;
    int gameId = 1;
    int sum = 0;
    long pow = 0;
    
    while ( getline(iFile, line) ) {
        cout << line << endl;
        size_t start = line.find(":");
        size_t end = line.find(";", start);
        bool isValid = true;
        int minimum[] = {0 ,0 , 0};
        while(end != std::string::npos){
            string gameSet = line.substr(start, end-start);
            checkGame(gameSet, max, minimum);
            start = end+1;
            end = line.find(";", start);
        }
       
        string gameSet = line.substr(start, end-start);
        checkGame(gameSet, max, minimum);
        pow += minimum[0] * minimum[1] * minimum[2];
        printf("game %d: %d\n", gameId, minimum[0] * minimum[1] * minimum[2]);

        gameId++;
    }
    cout << "res: " << pow << endl;
    return 0;
}   