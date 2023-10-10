#2141. Maximum Running Time of N Computers
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        s=sum(batteries)
        while batteries[-1]>s//n:
            s-=batteries[-1]
            batteries.pop()
            n-=1
        return s//n
      
        
