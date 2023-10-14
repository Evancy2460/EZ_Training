#Prime algorithm - Sieve of erasthones
'''def prime(l,n):
    while(i<n):
        while(i*j<n):
            j=i+1
            if i=="F":
                j+=1
            if i==i*j:
                l[i]="F"
                j+=1
n=int(input())
l=["T"]*(n+1)
print(prime(l,n))'''


def prime(l,n):
    p=2
    while(p*p<=n):
        if l[p]:
            for i in range(p*p,n+1,p):
                l[i]=False
        p+=1
    for p in range(2,n+1):
        if l[p]:
            print(p)

n=int(input())
l=[True]*(n+1)
prime(l,n)
