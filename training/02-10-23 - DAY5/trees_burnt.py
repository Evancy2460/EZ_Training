'''Calculate the no. of trees burnt wher 1 represents trees and 0 represents land '''
n=int(input())
a=[]
count=0
c1=0
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
            fun(a,i,j,n)
print(c1)

            
