class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {} # idx:nums

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in hashMap:
                return [hashMap[complement], idx]
            # hashMap.update({idx, num})
            hashMap[num] = idx