def targetsum(arr,n,target):
    if target==0:
        return True
    if n==0:
        return False
    if arr[n-1]>target:
        return targetsum(arr,n-1,target)
    return targetsum(arr,n-1,target-arr[n-1]) or targetsum(arr,n-1,target)  
arr=list(map(int,input().split(" ")))
target=int(input())
n=len(arr)

print(targetsum(arr,n,target))

