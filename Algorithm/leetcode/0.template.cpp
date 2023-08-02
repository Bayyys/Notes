#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    bool isPerfectSquare(int num)
    {
        if (1 == num)
        {
            return true;
        }
        int left = 1, right = num / 2;
        while (left <= right)
        {
            long long res = left + (right - left) / 2;
            if (res * res < num)
            {
                left = res + 1;
            }
            else if (res * res > num)
            {
                right = res - 1;
            }
            else
            {
                return true;
            }
        }
        return false;
    }
};

int main()
{
    Solution s;
    // vector<int> nums = {};
    int target = 10;
    // vector<int> res = s.searchRange(nums, target);
    // for (int i = 0; i < res.size(); i++)
    // {
    //     cout << res[i] << endl;
    // }
    vector<int> nums = {};
    for (int i = 1; i < 37; i++)
    {
        if (s.isPerfectSquare(i))
        {
            cout << i << "True" << endl;
        }
    }
    return 0;
}