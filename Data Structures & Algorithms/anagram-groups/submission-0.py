class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}

        for s in strs:
            # Create array of len 26 to hold a-z chars
            charCount = [0] * 26
            
            for c in s:
                charCount[ord(c) - ord("a")] += 1   #increment correct idx

            ## Lost here
            key = tuple(charCount)

            if key not in result:
                result[key] = []
            result[key].append(s)
        
        return list(result.values())
            