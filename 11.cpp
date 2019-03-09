//
// Created by aaron on 19-3-8.
//
#include <vector>

using namespace std;


class Solution {
public:

    int maxArea(vector<int> &height) {
        int maxarea = 0;
        int lpos = 0, rpos = height.size() - 1;
        while (lpos < rpos) {
            int lheight = height[lpos];
            int rheight = height[rpos];
            maxarea = max(maxarea, min(lheight, rheight) * (rpos - lpos));
            if (lheight < rheight) {
                lpos++;
            } else {
                rpos--;
            }
        }
        return maxarea;
    }
};