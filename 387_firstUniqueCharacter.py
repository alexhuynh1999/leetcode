class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = set(s)
        freq = dict.fromkeys(chars, 0)
        
        for char in s:
            freq[char] += 1
        
        for i, char in enumerate(s):
            if freq[char] == 1: return i
        return -1
