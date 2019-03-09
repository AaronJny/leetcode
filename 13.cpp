//
// Created by aaron on 19-3-8.
//

#include <string>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        int num = 0;
        for (int i = 0; i < s.length(); i++) {
            switch (s[i]) {
                case 'M':
                    num += 1000;
                    break;
                case 'D':
                    num += 500;
                    break;
                case 'C':
                    if (i + 1 < s.length() and (s[i + 1] == 'D' or s[i + 1] == 'M')) {
                        num -= 100;
                    } else {
                        num += 100;
                    }
                    break;
                case 'L':
                    num += 50;
                    break;
                case 'X':
                    if (i + 1 < s.length() and (s[i + 1] == 'L' or s[i + 1] == 'C')) {
                        num -= 10;
                    } else {
                        num += 10;
                    }
                    break;
                case 'V':
                    num += 5;
                    break;
                case 'I':
                    if (i + 1 < s.length() and (s[i + 1] == 'V' or s[i + 1] == 'X')) {
                        num -= 1;
                    } else {
                        num += 1;
                    }
                    break;
                default:
                    break;
            }
        }
        return num;
    }
};