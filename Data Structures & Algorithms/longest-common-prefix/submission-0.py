class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxPrefix = ""

        # First for loop defines the length of indexes we want to check
        # However, this does not necessarily mean that the first string is the shortest one.
        # So a better way would be to find the shortest string first.  
        shortestIdx = 0
        
        for s in range(1, len(strs)):
            if len(strs[s]) < len(strs[s-1]):
                shortestIdx = s

        # Now we can move on to the main logic
        for i in range(len(strs[shortestIdx])):
            for s in strs:
                # If index is larger than the length of string, forget it
                if i == len(s) or s[i] != strs[shortestIdx][i]:
                    return maxPrefix
                
            maxPrefix += strs[shortestIdx][i]
        
        return maxPrefix
