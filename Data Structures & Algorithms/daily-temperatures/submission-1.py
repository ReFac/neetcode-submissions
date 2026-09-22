class Solution:

  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    res = [0] * n
    stack = [] 

    for i, cur_temp in enumerate(temperatures):
      while stack and cur_temp > temperatures[stack[-1]]:
        prev_idx = stack.pop()
        res[prev_idx] = i - prev_idx

      stack.append(i)

    return res
