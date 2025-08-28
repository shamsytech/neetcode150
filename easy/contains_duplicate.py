class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Check if the array contains duplicate integers.
        
        Example Input: [1, 2, 3, 3]

        Algorithm Tracing
            seen:
            -> num = 1: 1 not in seen -> add 1 -> seen = {1} 
            -> num = 2: 2 not in seen -> add 2 -> seen = {1,2}
            -> num = 3: 3 not in seen -> add 3 -> seen = {1,2,3}
            -> num = 3: 3 in seen: return True 
        """
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
