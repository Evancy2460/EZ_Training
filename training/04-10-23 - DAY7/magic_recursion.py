def magic(n):
    l=[[0]*n for i in range(n)]
    def matrix(i,j,num):
        if num>n*n:
            return l
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
            return matrix(i,j,num)
        l[i][j]=num
        return matrix(i-1,j+1,num+1)
    return matrix(n//2,n-1,1)    
        
n=int(input())
k=magic(n)
for i in k:
    print(*i)
