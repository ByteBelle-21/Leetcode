# Leetcode problem  - https://leetcode.com/problems/count-and-say/description/

class Solution:
    def countAndSay(self, n: int) -> str:
        
        def helper_count_and_say(i):
            output = ""
            if i== 1:
                return "1"
            
            temp_result = helper_count_and_say(i-1)
            count = 1
            curr_index = 0
            result  = ""
            while curr_index < len(temp_result) - 1:
                if temp_result[curr_index] == temp_result[curr_index + 1]:
                    count += 1
                    curr_index += 1
                else:
                    result = result + str(count) + temp_result[curr_index]
                    curr_index += 1
                    count = 1
                   
            result = result + str(count) + temp_result[curr_index]
            return result 

        return helper_count_and_say(n)
