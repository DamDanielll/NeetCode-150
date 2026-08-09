class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ns = {}
        for i,num in enumerate(nums):
          res = target - num
          if res in ns:
            return [ns[res],i]
          else:
            ns[num] = i
