class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l, r = 0, len(nums) - 1

        first, last = -1, -1 #sentinel = -1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                # Do something
                first = mid
                r = mid - 1
            
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                # Do something
                last = mid
                l = mid + 1
            
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1


        return [first, last]