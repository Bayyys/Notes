class Solution:
    def removeElement1(self, nums: list[int], val: int):
        slowIndex = 0
        for fastIndex in range(len(nums)):
            if nums[slowIndex] != val:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
        return slowIndex
    
    def removeElement2(self, nums: list[int], val: int):
        leftIndex = 0
        rightIndex = len(nums) - 1
        while leftIndex <= rightIndex:
            while leftIndex <= rightIndex and nums[leftIndex] != val:
                leftIndex += 1
            while leftIndex <= rightIndex and nums[rightIndex] == val:
                rightIndex -= 1
            if leftIndex <= rightIndex:
                nums[leftIndex], nums[rightIndex] = nums[rightIndex], nums[leftIndex]
                leftIndex += 1
                rightIndex -= 1
        return leftIndex

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    s = Solution()
    print(s.removeElement1(nums, val))
    print(nums)
    nums = [3,2,2,3]
    print(s.removeElement2(nums, val))
    print(nums)