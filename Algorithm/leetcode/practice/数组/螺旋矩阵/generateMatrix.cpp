#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<vector<int>> generateMatrix(int n)
    {
        vector<vector<int>> res(n, vector<int>(n, 0));
        int left = 0, right = n - 1, top = 0, bottom = n - 1;
        int num = 1;
        while (left <= right && top <= bottom)
        {
            for (int i = left; i <= right; i++)
            {
                res[top][i] = num++;
            }
            for (int i = top + 1; i <= bottom; i++)
            {
                res[i][right] = num++;
            }
            if (left < right && top < bottom)
            {
                for (int i = right - 1; i > left; i--)
                {
                    res[bottom][i] = num++;
                }
                for (int i = bottom; i > top; i--)
                {
                    res[i][left] = num++;
                }
            }
            left++;
            right--;
            top++;
            bottom--;
        }
        return res;
    }
};

int main()
{
    int n = 3;
    vector<vector<int>> res = Solution().generateMatrix(n);
    for (int i = 0; i < res.size(); i++)
    {
        for (int j = 0; j < res[0].size(); j++)
        {
            cout << res[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}