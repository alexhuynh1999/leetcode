class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        left = 0
        longest = 0
        
        for right, char in enumerate(s):
            while char in visited:
                visited.remove(s[left])
                left += 1
            visited.add(char)
            longest = max(longest, right - left + 1)
        return longest
