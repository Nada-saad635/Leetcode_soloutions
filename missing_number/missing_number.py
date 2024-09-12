class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = min(nums)
        max_val = max(nums)
        full_set = set(range(min_val,max_val+1))
        sum_full_set = sum(full_set)
        sum_nums = sum(nums)
        return sum_full_set - sum_nums
    
sol = Solution()
nums = [2, 1, 5, 4, 6, 9, 7, 8, 10 ]  
missingNumber = sol.missingNumber(nums)  
print(missingNumber)
