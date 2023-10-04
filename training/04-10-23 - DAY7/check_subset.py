def check(nums,target):
    def backtrack(start,sum):
        if sum==target:
            return True
        if sum>target or start==len(nums):
            return False
        if backtrack(start+1,sum+nums[start]):
            subset.append(nums[start])
            return True
        return backtrack(start+1,sum)
    subset=[]
    if backtrack(0,0):
        return True,subset
    else:
        return False,[]
nums=list(map(int,input().split()))
target=int(input())
bool,subset=check(nums,target)
if bool:
    print("A subset is present")
else:
    print("No subset is present")
    
