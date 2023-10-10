pt=list(map(int,input().split()))
wt=list(map(int,input().split()))
sack=int(input())
'''ppw=[]
for i in range(len(wt)):
    ppw.append(pt[i]/wt[i])'''
l=list(zip(wt,pt))
l.sort(key=lambda x:x[1]/x[0],reverse=True)
maxpr=0
for w,p in l:
    if w<=sack:
        maxpr+=p
        sack-=w
    else:
        maxpr+=sack*(p/w)
        break
print(maxpr)
    
    

    
    
