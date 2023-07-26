#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main()
{
    vector<int> nums = {3, 8, 20};
    priority_queue<double> pq;
    double sum = 0;
    for (int i: nums)
    {
        pq.push(i);
        sum += i;
    }
    sum /= 2.0;

    double sum_tmp = 0;
    int count = 0;
    while (sum > 0)
    {
        double tmp = pq.top() / 2.0;
        count++;
        pq.pop();
        sum -= tmp;
        pq.push(tmp);
    }
    cout << count << endl;
    return 0;
}