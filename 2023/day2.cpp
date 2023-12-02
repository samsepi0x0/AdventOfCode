#include <bits/stdc++.h>

using namespace std;

void part1(){
    string line;
    ifstream inputFile("input2.txt");
    int line_number = 0;
    int sum = 0;

    int max_red = 12, max_blue = 14, max_green = 13;

    while(getline(inputFile, line)){
        line_number += 1;
        bool good_game = true;

        vector<string> tokens;
        stringstream check1(line);
        string temp;
        while(getline(check1, temp, ' ')){
            tokens.push_back(temp);
        }

        for(int i = 2; i < tokens.size(); i+=2){
            // cout << tokens[i] << "\t"; 
            int val = stoi(tokens[i]);
            string color = tokens[i+1];

            if (color.rfind("red", 0) == 0){
                if (val > max_red)
                    good_game = false;
            } else if (color.rfind("blue", 0) == 0){
                if (val > max_blue)
                    good_game = false;
            } else {
                if (val > max_green)
                    good_game = false;
            }
        }
        if(good_game){
            sum += line_number;
        }
    }
    cout << "Sum: " << sum << endl;
}

void part2(){
    string line;
    ifstream inputFile("input2.txt");
    int sum = 0;

    while(getline(inputFile, line)){
        int max_red = 0, max_blue = 0, max_green = 0;
        
        vector<string> tokens;
        stringstream check1(line);
        string temp;
        while(getline(check1, temp, ' ')){
            tokens.push_back(temp);
        }

        for(int i = 2; i < tokens.size(); i+=2){
            // cout << tokens[i] << "\t"; 
            int val = stoi(tokens[i]);
            string color = tokens[i+1];

            if (color.rfind("red", 0) == 0){
                if (val > max_red)
                    max_red = val;
            } else if (color.rfind("blue", 0) == 0){
                if (val > max_blue)
                    max_blue = val;
            } else {
                if (val > max_green)
                    max_green = val;
            }
        }
        sum += (max_red*max_blue*max_green);
    }
    cout << "Sum: " << sum << endl;
}

int main(){
    part1();
    part2();
    return 0;
}