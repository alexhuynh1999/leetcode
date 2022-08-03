import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # put every letter into an array
        # loop through every letter backwards
        # create new string that is flipped
        #
        # time:  O(n) -> where n is length of the string
        # space: O(n) 
        
        # instead, go through each letter
        # compare first, to last
        # compare second to second to last
        # compare n to length - n
        #
        # time:  O(n / 2) -> O(n)        
        # space: O(1)
        """"        
        cleanStr = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        reverse = ""   
        for i in range(len(cleanStr) - 1, -1, -1):
            reverse = reverse + cleanStr[i]
        return reverse == cleanStr
        """
        
        cleanStr = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        for i in range(len(cleanStr) // 2):
            oppositeIdx = len(cleanStr) - 1 - i
            if cleanStr[i] != cleanStr[oppositeIdx]:
                print(f'{cleanStr} is not a palindrome.')
                return False
        print(f'{cleanStr} is a palindrome.')
        return True
            
            
        
     
