n=int(input())
def printi(n):
    if(n==0):
        return
    print(n)
    printi(n-1)
printi(n)

n1=int(input())
def printi(n1):
    if(n1==0):
        return
    printi(n1-1)
    print(n1)
printi(n1)


    
