'''1 represents the land and 0 represents the water .Now count the no.of islands'''
n=int(input())
a=[]
count=0
for i in range(n):
    a.append(list(map(int,input().split())))

def fun(a,i,j,n):
    if a[i][j]==0:
        return
    if a[i][j]==1:
        a[i][j]=0
    if j<n-1:
        fun(a,i,j+1,n)
    if j>0:
        fun(a,i,j-1,n)
    if i<n-1:
        fun(a,i+1,j,n)
    if i>0:
        fun(a,i-1,j,n)
        
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            count=count+1
            fun(a,i,j,n)

print(count)
            
