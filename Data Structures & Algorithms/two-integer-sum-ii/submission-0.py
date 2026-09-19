class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointA = 0
        pointB = len(numbers)-1
        while pointA < pointB:
            s = numbers[pointA]+numbers[pointB]
            if s == target:
                return [pointA+1,pointB+1]
            elif s < target:
                pointA +=1
            else:
                pointB -=1

        return []
        

        