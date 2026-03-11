# Leetcode question - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        def find_first(num_list):
            left =  0
            right=  len(num_list) -1
            start = -1
            while left <= right:
                mid =  (left+right)//2
                if (num_list[mid] == target):
                    start =  mid
                    right = mid - 1
                elif num_list[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return start
        
        def find_last(num_list):
            left =  0
            right=  len(num_list) -1
            end = -1
            while left <= right:
                mid =  (left + right) // 2
                if (num_list[mid] == target):
                    end  = mid
                    left = mid + 1
                elif num_list[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return end

        return([find_first(nums), find_last(nums)])
            
        
