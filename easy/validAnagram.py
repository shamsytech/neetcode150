class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def checkString(s: str):   
            freqMap = {}
            for c in s:
                freqMap[c] = freqMap.get(c, 0) + 1 
            return freqMap
            
        return checkString(s) == checkString(t)
