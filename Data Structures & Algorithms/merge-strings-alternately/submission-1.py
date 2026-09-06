class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1Idx, ptr2Idx = 0,0
        res = ""

        while ptr1Idx < len(word1) and ptr2Idx < len(word2):
            res += word1[ptr1Idx]
            res += word2[ptr2Idx]

            ptr1Idx += 1
            ptr2Idx += 1

        if ptr1Idx >= len(word1) and ptr2Idx < len(word2):
            for i in range(ptr2Idx, len(word2), 1):
                res += word2[i]
        elif ptr1Idx < len(word1) and ptr2Idx >= len(word2):
            for j in range(ptr1Idx, len(word1), 1):
                res += word1[j]

        return res