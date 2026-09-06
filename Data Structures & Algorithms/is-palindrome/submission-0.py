class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        # Extract all alphanumeric char first
        for ch in s:
            if ch.isalnum():
                word += ch.lower() #! You forgot to make it all lowercase
        
        # Two pointer method to check if valid palindrome
        head = 0
        tail = len(word) - 1

        # while head < (len(word) / 2):
        while head < tail:
            if word[head] != word[tail]:
                return False
            
            head += 1
            tail -= 1

        return True
        
