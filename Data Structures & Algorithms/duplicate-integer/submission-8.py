class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i, num in enumerate(nums):
            if i != len(nums) - 1 and num == nums[i + 1]:
                return True;
        return False;