class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if two strings contain equal character counts.

        Example Inputs: 
            s = "rat" 
            t = "tar"

        Algorithm Tracing (s = "rat"):
            freq_map = {}
            -> c = "r" -> freq_map['r'] += 1 -> {'r': 1}
            -> c = "a" -> freq_map['a'] += 1 -> {'r': 1, 'a': 1}
            -> c = "t" -> freq_map['t'] += 1 -> {'r': 1, 'a': 1, 't': 1}
    
            We return True if the frequency maps of s and t are equal.
            -> return checkString(s) == checkString(t)
        """
        def checkString(s: str):   
            
            freq_map = {}
            for c in s:
                freq_map[c] = freq_map.get(c, 0) + 1 
            return freq_map
        
        return checkString(s) == checkString(t)
