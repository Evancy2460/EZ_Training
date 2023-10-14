def ver_graph(l):
    print("Vertical graph")
    max1=max(l)
    n=len(l)
    k=[0]*n
    for i in range(n):
        k[i]=(max1-l[i])
    for j in range(max1):
        for i in range(n):
            if k[i]==0:
                print("*",end=' ')
            else:
                print(" ",end=' ')
                k[i]-=1
        print()
    '''for i in range(max1,0,-1):
        print(f"{i:2d} |",end=" ")
        for j in l:
            if j>=i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()'''
def hor_graph(l):
    print("Horizontal graph")
    n=len(l)
    for i in l:
        print("*"*i)
l=list(map(int,input().split()))
ver_graph(l)
print()
hor_graph(l)
