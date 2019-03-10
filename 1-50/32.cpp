//
// Created by aaron on 19-3-10.
//

#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    void findStartPos(vector<int> &startPos, string s) {
        for (int i = 0; i < s.length() - 1;) {
            if (s[i] == '(' and s[i + 1] == ')') {
                startPos.push_back(i);
                i += 2;
            } else {
                i++;
            }
        }
    }

    void fill_zero(int *a, int n) {
        for (int i = 0; i < n; i++) {
            a[i] = 0;
        }
    }

    int longestValidParentheses(string s) {
        if (s.length() < 2) {
            return 0;
        }

        vector<int> startPos;
        findStartPos(startPos, s);
        if (startPos.size() == 0) {
            return 0;
        }
        int slen = s.length();
        int a[slen + 2];
        fill_zero(a, slen + 2);
        for (int i = 0; i < startPos.size(); i++) {
            int leftPos = startPos[i];
            int rightPos = leftPos + 1;
            while (leftPos >= 0 and rightPos < slen) {
                if (a[leftPos] == 1) {
                    leftPos--;
                    continue;
                }
                if (a[rightPos] == 1) {
                    rightPos++;
                    continue;
                }
                if (s[leftPos] == '(' && s[rightPos] == ')') {
                    a[leftPos] = 1;
                    a[rightPos] = 1;
                    leftPos--;
                    rightPos++;
                } else {
                    break;
                }
            }
        }
        int maxLength = 0;
        int cnt = 0;
        for (int i = 0; i < slen; i++) {
            if (a[i]) {
                cnt++;
            } else {
                maxLength = max(maxLength, cnt);
                cnt = 0;
            }
        }
        maxLength = max(maxLength, cnt);
        return maxLength;
    }
};