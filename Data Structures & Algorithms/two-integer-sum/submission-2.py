class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty hash table
        num_map = {}

        for idx, val in enumerate(nums):
            # Calculate the complement of each num 
            lookUp = target - val
            
            # Search for that complement in the hash table
            if lookUp in num_map:
                return [num_map[lookUp], idx]
            
            num_map[val] = idx # I did num_map[idx] = val
        return []