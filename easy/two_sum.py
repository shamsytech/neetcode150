class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Return indices of the two elements that add up to target. 

        Example Input: [3,4,5,6], target = 7
        
        Algorithm Tracing:
            seen = {}
            
            -> i = 0, n = 3, diff = 4 -> 4 not in seen -> seen[3] = 0
            -> i = 1, n = 4, diff = 3 -> 3 in seen -> return [seen[3], 1] -> [0,1]   
        """
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
  