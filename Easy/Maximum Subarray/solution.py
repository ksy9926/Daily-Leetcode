class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        len_nums = len(nums)
        
        if len_nums == 1:
            return nums[0]
        
        mid = len_nums//2
        
        left = self.maxSubArray(nums[:mid])
        right = self.maxSubArray(nums[mid:])
        
        left_sum = -99999
        right_sum = -99999
        
        temp = 0
        
        for i in range(mid-1, -1, -1):
            temp += nums[i]
            left_sum = max(left_sum, temp)
            
        temp = 0
        
        for j in range(mid, len_nums):
            temp += nums[j]
            right_sum = max(right_sum, temp)
            
        return max(left, right, left_sum + right_sum)



# Other Solution

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         ans=[]
#         ans.append(nums[0])
#         for i in range(1,len(nums)):
#             ans.append(max(nums[i],ans[i-1]+nums[i]))
        
#         return max(ans)


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = -100000
#         curr_sum = 0
#         for i in range(len(nums)):
#             curr_sum = max(nums[i], curr_sum + nums[i])
#             if curr_sum > max_sum:
#                 max_sum = curr_sum
#         return max_sum