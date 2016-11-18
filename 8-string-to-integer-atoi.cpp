// Implement atoi to convert a string to an integer.

#include <iostream>
#include <limits>
using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        int i = 0;
        bool positive = true;
        long r = 0;
        int imax = numeric_limits<int>::max();
        int imin = numeric_limits<int>::min();
        while (str[i] == ' ') { i++;}
        if (str[i] == '+') { positive = true;i++;}
        else if (str[i] == '-') { positive = false;i++;}
        if (!isdigit(str[i])) { return 0;}
        while (isdigit(str[i])) {
            r = r * 10 + long(str[i] - '0');
            if (positive && r > imax) { return imax;}
            if (!positive && -r < imin) { return imin;} 
            i++;
        }
        int rr = r;
        if (positive) { return rr;}
        else { return -rr;}
    }
};
void Test(string str) {
    Solution solution;
    cout << "Input string is: " << str << endl;
    cout << "Output number is: " << solution.myAtoi(str) << endl;
}
int main() {
    Test("+100");
    Test("-100");
    Test("  10035");
    Test("");
    Test("avd");
    Test("1024abc");
    Test("1000000000000000000000000000000000000");
    Test("+-5");
    Test("-+5");
    return 0;
}

