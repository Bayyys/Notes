#include <iostream>
#include <vector>
#include <cassert>
#include <cstring>

using namespace std;

class Solution
{
public:
    int totalFruit(vector<int> &fruits)
    {
    }
};

int main()
{
    Solution s;
    vector<int> nums = {1, 1, 1, 1, 1, 1, 1, 1};
    int target = 11;
    int result = 0;
    assert(s.minSubArrayLen(target, nums) == result);
    cout << "Pass!" << endl;
    return 0;
}