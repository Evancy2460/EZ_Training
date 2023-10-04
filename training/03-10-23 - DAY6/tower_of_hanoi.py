def tower(n,s,a,d):
    if n>0:
        tower(n-1,s,d,a)
        print(s,"->",d)
        tower(n-1,a,s,d)
n=int(input())
tower(n,'S','A','D')

def tower(n,s,a,d):
    if n==0:
        return 0
    return tower(n-1,s,d,a)+tower(n-1,a,s,d)+1
n=int(input())
print(tower(n,'S','A','D'))


