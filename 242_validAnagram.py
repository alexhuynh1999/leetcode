class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = set(s)
        freq_s = dict.fromkeys(chars, 0)
        freq_t = dict.fromkeys(chars, 0)
        
        for char in s:
            freq_s[char] += 1
        
        for char in t:
            if char not in freq_t: return False
            freq_t[char] += 1
                
        return freq_s == freq_t

 class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # counter method: 
        #   initialize a counter object of all the alphabet (a...z)
        #   increment counter by 1 for each character seen
        #   do this for s and t
        #   check if counter objects are equivalent
        #   
        #   time:  O(max(s,t))
        #   space: O(1) because only 26 characters. unicode would be the same; just a 255 char object
        
        if len(s) != len(t): return False
        
        alphabet = list(map(chr, range(97, 123)))
        counterC = dict.fromkeys(alphabet, 0)
        counterT = dict.fromkeys(alphabet, 0)
        
        for char in s:
            counterC[char] += 1
        for char in t:
            counterT[char] += 1
            
        return counterC == counterT
