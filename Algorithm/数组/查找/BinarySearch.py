class Solution:
    def binarySearch(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1

    def binarySearch2(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1

if __name__=="__main__":
    nums = [-1,0,3,5,9,12]
    target = 3
    print(Solution().binarySearch(nums, target))
    print(Solution().binarySearch2(nums, target))