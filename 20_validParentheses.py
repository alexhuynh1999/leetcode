class Solution:
    def isValid(self, s: str) -> bool:
        # "([{}])"
        # all the open parenthesis are put into the stack
        # if closed parenthesis is encountered, look at top of stack
        # if the top of stack is the corresponding closed parenthesis, continue
        # otherwise, return nothing
        #
        # time:  O(n) since we visit each eleme in array once
        # space: O(n) since we store entire array on the stack
        closed = {')' : '(',
                  '}' : '{', 
                  ']' : '['}
        stack = []
        for char in s:
            if char not in closed:  # we have an open parenthesis
                stack.append(char)
            else:
                if stack:
                    back = stack.pop()
                    if back == closed[char]:
                        continue
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        return True
