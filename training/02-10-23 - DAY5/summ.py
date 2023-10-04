n2=int(input())
def sumofdigits(n2):
    if(n2<=0):
        return 0
    return ((n2%10)+sumofdigits(n2//10))
print(sumofdigits(n2))
