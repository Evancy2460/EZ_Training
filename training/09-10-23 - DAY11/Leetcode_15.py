#15. 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        m=[]
        tar=0
        n=len(nums)
        nums.sort()
        for i in range(n):
            left=i+1
            right=n-1
            while(left<right):
                if (nums[i]+nums[left]+nums[right])==tar and ([nums[i],nums[left],nums[right]]) not in m:
                    m.append([nums[i],nums[left],nums[right]])
                if(nums[i]+nums[left]+nums[right])<tar:
                    left+=1
                else:
                    right-=1     
        return m     
