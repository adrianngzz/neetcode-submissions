class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            # countS[s[i]] = 1 + countS[s[i]]
            countS[s[i]] = 1 + countS.get(s[i], 0) # the .get(,) function returns default value 0 if s[i] does not exist
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for j in countS:
            if countS[j] != countT.get(j, 0):
                return False
        
        return True



# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False