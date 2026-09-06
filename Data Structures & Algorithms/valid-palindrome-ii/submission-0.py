class Solution:
    def validPalindrome(self, s: str) -> bool:
        word = ""

        for ch in s:
            if ch.isalnum():
                word += ch.lower()

        # Two pointer method
        L = 0
        R = len(word) - 1

        while L < R:
            if word[L] != word[R]:
                skipL = word[L+1 : R+1]     # Start at L+1, Stop at R
                skipR = word[L : R]         # Start at L, Stop at R-1

                return (skipL == skipL[::-1] or skipR == skipR[::-1])

            L += 1
            R -= 1

        return True