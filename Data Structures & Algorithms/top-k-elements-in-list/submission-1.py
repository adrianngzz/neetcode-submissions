class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        result = []

        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

        # Take the top k pairs, then pull out just the numbers
        
        ## Fast python way
        # return [num for num, freq in sorted_counts[:k]]
        for num, freq in sorted_counts[:k]:
            result.append(num)
        
        return result
