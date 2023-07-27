#include <iostream>
#include <vector>
using namespace std;


class solution {
 public:
  int binaySearch(int arr[], int length, int target) {
    int left = 0;
    int right = length - 1;
    while (left < right) {
      int mid = left + (right - left) / 2;
      if (arr[mid] > target) {
        right = mid;
      } else if (arr[mid] < target) {
        left = mid + 1;
      } else {
        return mid;
      }
    }
    return -1;
  }
};

int main() {
  int nums[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int length = sizeof(nums) / sizeof(nums[0]);
  int target = 9;
  solution s;
  int find = s.binaySearch(nums, length, target);
  cout << find << endl;
  return 0;
}