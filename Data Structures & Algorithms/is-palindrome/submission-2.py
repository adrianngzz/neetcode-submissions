class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleanedWord = ""

        for c in s:
            if c.isalnum():
                cleanedWord += c.lower()

        #### Did the rest yourself... Good
        l, r = 0, len(cleanedWord)-1

        while l < r:
            # if (s[l].isalnum() and s[r].isalnum()):
            if (cleanedWord[l] != cleanedWord[r]):
                return False
            l += 1
            r -= 1
        return True