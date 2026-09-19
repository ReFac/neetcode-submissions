class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_index = 0
        for num in nums_set:
            if (num-1) not in nums_set:
                current_num = num
                current_streak = 1
                while ( current_num +1 in nums_set):
                    current_streak +=1
                    
                    current_num += 1
                longest_index = max(current_streak,longest_index)

        return longest_index





        
        
        