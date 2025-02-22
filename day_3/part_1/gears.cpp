#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <random>
#include <string>
#include <fstream>

using namespace std;

void checkPrevVec(vector<pair<int, pair<int, int>>> &p, int i, int &sum){
    for(auto &e: p){
        printf("++%d:[%d, %d] : %d\n", e.first, e.second.first, e.second.second, i);
        if(e.second.first <= i && i <= e.second.second){
            cout << "dodano++" << endl;
            sum += e.first;
            e.first = 0;
            //cout << "+: " << e.first << endl;
        }
    }
}

int main(){
    ifstream iFile("../input.txt");
    //ifstream iFile("test02.in");
    string line;
    int sum = 0;
    vector<pair<int, pair<int, int>>> p;
    string pr;
    while ( getline(iFile, line) ) {
        cout << "prev: " << pr << endl;
        cout << "curr: " << line << endl;
        vector<pair<int, pair<int, int>>> v;
        for(int i=0; i < line.size(); i++){
            // check prev vector if simbol encountered
            if(line[i] != '.' && !isdigit(line[i])){
                checkPrevVec(p, i, sum);
            }
            // read line and note every number occurance
            int d = 0;
            if(isdigit(line[i])){
                d = stoi(&line[i]);
                //if simbol before the number
                if(i != 0 && line[i-1] != '.' && !isdigit(line[i-1])){
                    cout << "1same line+: " << d << endl;
                    sum += d;
                    // take i to end of number
                    for(int j = 0; pow(10, j) <= d; j++){
                        i++;
                    }
                    // check prev vec if simbol again
                    if(line[i] != '.' && i < line.size()){
                        checkPrevVec(p, i, sum);
                    }
                }else{

                    int start = i-1;
                    // take i to end of number
                    for(int j = 0; pow(10, j) <= d; j++){
                        i++;
                    }
                    //if simbol behing the number
                    if(line[i] != '.' && i < line.size()){
                        cout << "l[i]: " << line[i] << " 2ame line+: " << d << endl;
                        sum += d;
                        checkPrevVec(p, i, sum);
                        continue;
                    }else{
                        int end = i;
                        //if number not used store it
                        v.push_back(make_pair(d, make_pair(start, end)));
                        printf("start: %d, end: %d\n", start, end);
                        if(start < 0) start = 0;
                        if(end > pr.size()) end = pr.size();
                        if(start < end){
                            string range = pr.substr(start, end-start+1);
                            // check if prev line has relavant simbols to use number
                            for(int j=0; j<range.size(); j++){
                                if(range[j] != '.' && !isdigit(range[j])){
                                    sum += d;
                                    cout << "+: " << d << endl;
                                    v.pop_back();
                                    break;
                                }
                            }
                            cout << "range: " << range << endl;
                        }
                        printf("%d:[%d, %d]\n", d, start, end);
                    }
                }
            }
        }

        p = v;
        pr = line;
        cout << "----------------" << endl;
        // sum up relevant numbers based on previous line
        
        // current line = previous line
        /*
        for(auto x: v){
            cout << x.first << "index: " << x.second << endl;
        }
        */
        
    }
    cout << "res: " << sum << endl;
    return 0;
}   