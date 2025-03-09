#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// NOT GENERAL SOLUTION - solution are custum for each input
// 
// custom operation for my day 17 part 2 EXAMPLE input - based on program to say
long long example_program(vector<int> output) {

    long long A = 0;

    for (int i = output.size() -1 ; i >=  0; --i) {
        A = (A << 3) + output[i];
    }
    return A << 3;
}

int main() {
    // EXAMPLE input of day 17 part 2 - named output cuz assigment
    vector<int> output = {0,3,5,4,3,0};

    long long result = example_program(output);

    cout << "EXAMPLE input part 2:" << endl;
    cout << result << endl;

    return 0;
}