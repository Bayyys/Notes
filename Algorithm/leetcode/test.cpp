#include <cassert>
#include <cstring>
#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int totalFruit(vector<int> &fruits)
    {
        int left = 0, right = 1;
        int count = 1;
        int num1 = fruits[0], num2 = INT32_MIN;
        int tmp = INT32_MIN;
        while (right <= fruits.size() - 1)
        {
            if (fruits[right] != num1 && fruits[right] != num2)
            {
                if (num2 == INT32_MIN)
                {
                    num2 = fruits[right];
                }
                else
                {
                    int c = right - 2;
                    while (fruits[right - 1] == fruits[c])
                    {
                        c--;
                    }
                    left = c + 1;
                    num1 = fruits[left];
                    num2 = fruits[right];
                }
            }
            count = max(count, right - left + 1);
            right++;
        }
        return count;
    }
};

int main()
{
    Solution s;
    vector<int> nums = {1, 0, 1, 4, 1, 4, 1, 2, 3};
    cout << s.totalFruit(nums) << endl;
    return 0;
}