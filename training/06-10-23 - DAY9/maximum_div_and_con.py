def maximum(l,i,j):
    if i==j:
        return l[i]
    max1=(i+j)//2
    return max(maximum(l,i,max1),maximum(l,max1+1,j))
l=list(map(int,input().split()))
print(maximum(l,0,len(l)-1))
