class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0
        tmp = []

        for n in nums:
            if n != val:
                k = k + 1
                tmp.append(n)

        # Copied this line from solution
        for i in range(len(tmp)):
            nums[i] = tmp[i]

        return len(tmp)