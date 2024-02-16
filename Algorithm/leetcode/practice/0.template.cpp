#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        int left = 0;
        int right = nums.size() - 1;
        while (left <= right)
        {
            while (nums[left] != val && left <= right)
            {
                left++;
            }
            while (nums[right] == val && left <= right)
            {
                right--;
            }
            if (left <= right)
            {
                nums[left] = nums[right];
                right--;
                left++;
            }
        }
        return left;
    }
};

int main()
{
    Solution s;
    // vector<int> nums = {0, 0, 0, 0, 1};
    // vector<int> nums = {0, 1, 2, 2, 3, 0, 4, 2};
    vector<int> nums = {2};
    int target = 2;
    cout << s.removeElement(nums, target) << endl;
    return 0;
}