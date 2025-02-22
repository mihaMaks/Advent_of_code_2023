#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;

void checkPrevVec_nums(vector<pair<int, pair<int, int>>> &p, int i, vector<pair<int, vector<int>>> &g){
    vector<int> b;
    for(auto &e: p){
        printf("number%d:[%d, %d] : %d-index\n", e.first, e.second.first, e.second.second, i);
        if(e.second.first <= i && i <= e.second.second){
            b.push_back(e.first);
            //e.first = 0;
            //cout << "+: " << e.first << endl;
        }
    }
    g.push_back(make_pair(i, b));
    return;
}

void checkPrevVec_gears(pair<int, pair<int, int>> &p, vector<pair<int, vector<int>>> &g){
    for(auto &e: g){
        printf("num: %d [%d-%d]\n",p.first, p.second.first, p.second.second);
        if(p.second.first <= e.first && e.first <= p.second.second){
            e.second.push_back(p.first);
            //e.first = 0;
            printf("++g[%d]: %d\n", e.first, p.first);
        }
    }
    //g.push_back(make_pair(i, b));
    return;
}

int sum_prev_gears(vector<pair<int, vector<int>>> &g){
    int sum = 0;
    for(auto &gear: g){
        if(gear.second.size() == 2){
            sum += gear.second[0] * gear.second[1];
        }
    }
    return sum;
}

int main(){
    ifstream iFile("../input.txt");
    //ifstream iFile("test01.in");
    string line;
    int sum = 0;
    // gear index, <gear number 1, gear number 2>
    vector<pair<int, pair<int, int>>> pr_nums;
    vector<pair<int, vector<int>>> pr_gears;

    string pr;
    while ( getline(iFile, line) ) {
        cout << "prev: " << pr << endl;
        cout << "curr: " << line << endl;
        vector<pair<int, vector<int>>> gears;
        vector<pair<int, pair<int, int>>> nums;

        for(int i=0; i < line.size(); i++){
            //cout << "-------------------------" << line[i] << endl;
            
            // if we come across gear check prev line for numbers and store it
            if(line[i] == '*'){
                //check if number before gear
                int start = 0;
                int k = i;
                int pred =0; int po = 0;
                if(k > 0 && isdigit(line[k-1])){
                    int j = k-1;
                    int end = k;
                    while(isdigit(line[j])){
                        j--;
                    }
                    int d = stoi(&line[j+1]);
                    start = j;
                    pr_nums.push_back(make_pair(d, make_pair(start, end)));
                    pred =1;
                    k = end;
                }
                //check if nuber after gear
                if(k+1 < line.size() && isdigit(line[k+1])){
                    
                    int d = stoi(&line[k+1]);
                    start = k;
                    for(int j = 0; pow(10, j) <= d; j++){
                        k++;
                    }
                    int end = k+1;
                    //nums.push_back(make_pair(d, make_pair(start, end)));
                    pr_nums.push_back(make_pair(d, make_pair(start, end)));
                    po =1;
                }
                
                checkPrevVec_nums(pr_nums, i, gears);
                if(pred) pr_nums.pop_back();
                if(po) pr_nums.pop_back();
            
            }
            
            //if we come across number check prev line for gears and store it
            if(isdigit(line[i])){
                int d = stoi(&line[i]);
                int start = i-1;
                for(int j = 0; pow(10, j) <= d; j++){
                    i++;
                }
                int end = i;
                nums.push_back(make_pair(d, make_pair(start, end)));
                
                auto p = nums.back();
                checkPrevVec_gears(nums.back(), pr_gears);
                i--;
            }
        
        }
        //izpis
        
        } 
        //check all prev_gears and sum up ones with exactly 2 numbers
        sum += sum_prev_gears(pr_gears);
        pr_gears = gears;
        pr_nums = nums;
        pr = line;
        
        
    }
    sum += sum_prev_gears(pr_gears);
    cout << "res: " << sum << endl;
    return 0;
}   