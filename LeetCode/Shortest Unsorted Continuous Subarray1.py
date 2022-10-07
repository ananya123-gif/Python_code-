# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, 
# then the whole array will be sorted in ascending order.
# Return the shortest such subarray and output its length.

# Example 1:
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 0

# Example 3:
# Input: nums = [1]
# Output: 0
 
# Constraints:
# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        l,r = n,0

        cur_max = float('-inf')
        cur_min = float('inf')

        for i in range(n):
            if cur_max > nums[i]:
                r=i
            if nums[n-i-1]>cur_min:
                l=n-i-1
            cur_max = max(cur_max,nums[i])
            cur_min = min(cur_min,nums[n-i-1])

        return max(0,r-l+1)
        
