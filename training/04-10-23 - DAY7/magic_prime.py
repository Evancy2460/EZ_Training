n=int(input())
l=[[0]*n for i in range(n)]
num=1
i=n//2
j=n-1
while num<=(n*n):
    if i<0 and j==n:
        i=0
        j=n-2
    else: 
        if j==n:
            j=0
        if i<0:
            i=n-1
        if l[i][j]:
            i=i+1
            j=j-2
            continue
        l[i][j]=num
        i=i-1
        j=j+1
        num+=1
for i in l:
    print(*i)
