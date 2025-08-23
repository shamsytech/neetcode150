class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        [1, 2, 3, 3]
        seen:
        {} -> {1} --> {1,2} --> {1,2,3} --> 3 is in seen, returns True   
        '''
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
