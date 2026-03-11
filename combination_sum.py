# Leetcode problem - https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []

        def backtrack_sum(i, sum, temp_result):
            if sum == target:
                result.append(temp_result.copy())
                return 

            elif sum > target or i >= len(candidates):
                return 

            temp_result.append(candidates[i])
            backtrack_sum(i, sum + candidates[i], temp_result)

            temp_result.pop()
            backtrack_sum(i+1, sum, temp_result)

        backtrack_sum(0, 0, [])

        return result
