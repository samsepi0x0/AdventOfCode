#include <bits/stdc++.h>

using namespace std;

void part1(){
    string line;
    ifstream inputFile("input1.txt");
    vector<int> values;

    while(getline(inputFile, line)){
        int size = line.length();
        string val;
        for(int i = 0; i < size; i++){
            if (isdigit(line[i])){
                val += line[i];
                break;
            }
        }
        for(int i = size - 1; i >= 0; i--){
            if (isdigit(line[i])){
                val += line[i];
                break;
            }
        }
        values.push_back(stoi(val));
    }
    int sum = accumulate(values.begin(), values.end(), 0);
    cout << "Sum: " << sum << endl;
    inputFile.close();
}

void part2(){
    // in python
}

int main(){
    part1(); 
    return 0;
}
