#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int minSubArrayLen(vector<int> &nums, int s){
        int minLen = INT_MAX;
        int sum = 0;
        int left = 0;
        int subLength = 0;
        for (int left = 0; left < nums.size(); left++)
        {
            sum += nums[left];
            while (sum >= s)
            {
                subLength = left - left + 1;
                minLen = minLen < subLength ? minLen : subLength;
                sum -= nums[left++];
            }
        }
        return minLen == INT_MAX ? 0 : minLen;
    }
};

int main()
{
    vector<int> nums={2,3,1,2,4,3};
    int s=7;
    Solution solution;
    cout << solution.minSubArrayLen(nums, s) << endl;
    return 0;
}