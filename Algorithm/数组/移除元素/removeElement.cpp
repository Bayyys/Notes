#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        int slowIndex, fastIndex = 0;
        for (int fastIndex = 0; fastIndex < nums.size(); fastIndex++)
        {
            if (nums[fastIndex] != val)
            {
                nums[slowIndex] = nums[fastIndex];
                slowIndex++;
            }
        }
        return slowIndex;
    }
    int removeElement2(vector<int> &nums, int vla)
    {
        int leftIndex = 0;
        int rightIndex = nums.size() - 1;
        while (leftIndex <= rightIndex)
        {
            while (leftIndex <= rightIndex && nums[leftIndex] != vla)
            {
                leftIndex++;
            }
            while (leftIndex <= rightIndex && nums[rightIndex] == vla)
            {
                rightIndex--;
            }
            if (leftIndex <= rightIndex)
            {
                nums[leftIndex++] = nums[rightIndex--];
            }
        }
        return leftIndex;
    };
};

int main()
{
    vector<int> nums = {1, 2, 3, 2, 4, 5, 2, 6};
    int val = 2;
    Solution s;
    int res = s.removeElement2(nums, val);
    cout << res << endl;
    return 0;
}