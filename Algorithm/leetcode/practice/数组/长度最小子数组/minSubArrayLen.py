class Solution:
    def minSubArrayLen(self, nums: list[int], s: int) -> int:
        left = 0
        right = 0
        sum = 0
        minLen = len(nums) + 1
        while right < len(nums):
            sum += nums[right]
            while sum >= s:
                minLen = min(minLen, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1
        return 0 if minLen == len(nums) + 1 else minLen

if __name__=='__main__':
    print(Solution().minSubArrayLen([2,3,1,2,4,3], 7))