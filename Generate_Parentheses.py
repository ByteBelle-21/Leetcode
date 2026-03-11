# Leetcode Question  -  https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result  = []

        def backtrack_generate(s, open_p, close_p):
            if len(s) == (2*n):
                result.append(s)
                return
            
            if open_p < n:
                backtrack_generate((s+"("), open_p+1, close_p)

            if open_p > close_p:
                backtrack_generate((s+")"), open_p, close_p+1)
        
        backtrack_generate("", 0, 0)
        return result
 
