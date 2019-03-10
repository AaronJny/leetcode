#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    /**
     * 从后向前，找到第一个比最后一个数小的数的坐标
     * @param nums
     * @return
     */
    int findFirstMinNum(vector<int> &nums, int lastPos) {
        int pos = -1;
        for (int i = lastPos - 1; i >= 0; i--) {
            if (nums[i] < nums[lastPos]) {
                pos = i;
                break;
            }
        }
        return pos;
    }


    void nextPermutation(vector<int> &nums) {
        if (nums.size() <= 1) {
            return;
        }
        int finalPos = -1;
        int finalLastPos = nums.size() - 1;
        int pos = -1;
        for (int i = nums.size() - 1; i > 0; i--) {
            pos = findFirstMinNum(nums, i);
            if (pos != -1) {
                if (pos > finalPos) {
                    finalPos = pos;
                    finalLastPos = i;
                }
            }
        }
        if (finalPos == -1) {
            sort(nums.begin(), nums.end());
        } else {
            int tmp = nums[finalPos];
            nums[finalPos] = nums[finalLastPos];
            nums[finalLastPos] = tmp;
            sort(nums.begin() + finalPos + 1, nums.end());
        }
    }
};