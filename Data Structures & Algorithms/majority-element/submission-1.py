class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Create variables
        count = {}
        result, maxCount = 0, 0

        for num in nums:
            count[num] = 1 + count.get(num, 0)

            # Check if result needs to be updated
            if count[num] > maxCount:
                result = num

            # Update maxCount if needed
            maxCount = max(count[num], maxCount)
        return result