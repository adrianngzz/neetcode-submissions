class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Case 1: Not the same length... False
        if len(s) != len(t):
            return False

        # Case 2
        hashS, hashT = {}, {}

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)

        for j in hashS:
            if hashS[j] != hashT.get(j, 0):
                return False
        
        return True