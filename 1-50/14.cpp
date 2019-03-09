//
// Created by aaron on 19-3-8.
//

#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string> &strs) {
        if (strs.size() == 0) {
            return "";
        }
        int min_length = 1 << 30;
        for (int i = 0; i < strs.size(); i++) {
            min_length = min(min_length, int(strs[i].length()));
        }
        int max_prefix_size = 0;
        for (int i = 0; i < min_length; i++) {
            bool flag = true;
            char ch = strs[0][i];
            for (int j = 1; j < strs.size(); j++) {
                if (strs[j][i] != ch) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                max_prefix_size += 1;
            } else {
                break;
            }
        }
        return strs[0].substr(0, max_prefix_size);
    }
};