#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
	int binary_search1(vector<int> &nums, int target)
	{
		int left = 0;
		int right = nums.size() - 1;
		while (left <= right)
		{
			int middle = left + (right - left) / 2;
			if (nums[middle] == target)
			{
				return middle;
			}
			else if (nums[middle] < target)
			{
				left = middle + 1;
			}
			else if (nums[middle] > target)
			{
				right = middle - 1;
			}
		}
		return -1;
	};
	int binary_search2(vector<int> &nums, int target)
	{
		int left = 0;
		int right = nums.size();
		while (left < right)
		{
			int middle = left + (right - left) / 2;
			if (nums[middle] == target)
			{
				return middle;
			}
			else if (nums[middle] < target)
			{
				left = middle + 1;
			}
			else if (nums[middle] > target)
			{
				right = middle;
			}
		}
		return -1;
	};
};

int main()
{
	vector<int> nums = {1, 2, 3, 4, 5, 6};
	int target = 3;
	Solution s;
	int res = s.binary_search2(nums, target);
	cout << res << endl;
	return 0;
}