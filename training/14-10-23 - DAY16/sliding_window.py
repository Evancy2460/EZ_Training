#Sliding Window Algorithm
def sliding(l,target,n):
    def slo(i):
        k=[]
        if i>n-1:
            return None
        if l[i]==target:
            return l[i]
        k.append(l[i])
        def algo(su,j):
            if j>n-1:
                return slo(i+1)
            su+=l[j]
            k.append(l[j])
            if l[j]==target:
                return l[j]
            elif su==target:
                return k
            elif su<target:
                return algo(su,j+1)
            if su> target:
                return slo(i+1)
        return algo(l[i],i+1)
    return slo(0)
l=list(map(int,input().split()))
target=int(input())
n=len(l)
print(sliding(l,target,n))
