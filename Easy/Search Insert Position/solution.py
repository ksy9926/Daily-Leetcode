class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for item in nums:
                if item > target:
                    return nums.index(item)
            return len(nums)