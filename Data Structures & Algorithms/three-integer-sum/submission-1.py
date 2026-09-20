class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)-2):
            if (i-1) >= 0 and nums[i-1] == nums[i]:
                continue
            
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left]+nums[right] == -nums[i]:
                    result.append([nums[i],nums[left],nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums [right-1]:
                        right -=1

                    left += 1
                    right -= 1
                elif nums[left]+nums[right] > -nums[i]:
                    right -=1
                else:
                    left +=1

        return result

            

        