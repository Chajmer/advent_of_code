#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// NOT GENERAL SOLUTION - solution are custum for each input
// 
// custom dfs for my day 17 part 2 FINAL input - based on program to say
vector<long long>  dfs(long long A, vector<int> output, int out_ptr) {

    if (out_ptr == -1) return vector<long long > {A};

    vector<long long> result;

    for (int i = 0; i < 8; ++i) {

        long long shift_A = (A << 3) + i;

        // custom operation for my input
        if (output[out_ptr] == (i ^ ((shift_A >> (i^7)) % 8))) {
        
            // add results from deeper dfs
            for (auto d : dfs(shift_A, output, out_ptr - 1)) {
                result.push_back(d);
            }
        }
    }
    return result;
}

int main() {
    // FINAL input of day 17 part 2 - named output cuz assigment
    vector<int> output = {2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0};

    vector<long long> result = dfs(0, output, output.size() - 1);

    cout << "Final input part 2:" << endl;
    cout << *min_element(result.begin(), result.end()) << endl;

    return 0;
}