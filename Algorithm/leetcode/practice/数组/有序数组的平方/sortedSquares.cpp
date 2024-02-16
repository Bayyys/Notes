#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        vector<int> sortedSquares(vector<int>& A) {
            vector<int> res(A.size(), 0);
            int i = 0, j = A.size() - 1, pos = A.size() - 1;
            while (i <= j) {
                if (abs(A[i]) > abs(A[j])) {
                    res[pos] = A[i] * A[i];
                    i++;
                } else {
                    res[pos] = A[j] * A[j];
                    j--;
                }
                pos--;
            }
            return res;
        }
};

int main() {
    vector<int> A = {-4, -1, 0, 3, 10};
    Solution s;
    vector<int> res = s.sortedSquares(A);
    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << endl;
    }
    return 0;
}