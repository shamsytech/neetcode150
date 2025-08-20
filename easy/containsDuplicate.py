class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        hSet
        1, 2, 3, 3
        {1, 2, 3}    
        '''
        hSet = set()

        for num in nums:
            if num not in hSet:
                hSet.add(num)
            else:
                return True
        return False


 

         