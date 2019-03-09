//
// Created by aaron on 19-3-8.
//

#include <string>

using namespace std;

class Solution {
public:
    string _intToRoman(int num, int fact, char one, char five, char ten) {
        string tmp_str = "";
        if (num >= fact) {
            int n2 = num / fact;
            if (n2 == 9) {
                tmp_str += one;
                tmp_str += ten;
            } else if (n2 == 4) {
                tmp_str += one;
                tmp_str += five;
            } else if (n2 >= 5) {
                tmp_str += five;
                for (int i = 5; i < n2; i++) {
                    tmp_str += one;
                }
            } else {
                for (int i = 0; i < n2; i++) {
                    tmp_str += one;
                }
            }
        }
        return tmp_str;
    }

    string intToRoman(int num) {
        string str = _intToRoman(num, 1000, 'M', 'M', 'M');
        num %= 1000;
        str += _intToRoman(num, 100, 'C', 'D', 'M');
        num %= 100;
        str += _intToRoman(num, 10, 'X', 'L', 'C');
        num %= 10;
        str += _intToRoman(num, 1, 'I', 'V', 'X');
        return str;
    }
};