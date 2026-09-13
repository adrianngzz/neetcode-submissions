class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Condition 1: If len is different
        if len(s) != len(t):
            return False

        # Condition 2
        hash1, hash2 = {}, {}

        for i in s:
            if i not in hash1:
                hash1[i] = 1
            else:
                hash1[i] += 1

        for j in t:
            if j not in hash2:
                hash2[j] = 1
            else:
                hash2[j] += 1

        if hash1 == hash2:
            return True
        return False

        