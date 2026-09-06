class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = []
        for n in nums:
            if n not in unique:
                unique.append(n)
            else:
                return True;
        return False;
