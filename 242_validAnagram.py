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
