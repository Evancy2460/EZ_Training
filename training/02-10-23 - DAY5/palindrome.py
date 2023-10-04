def palindrome(str,i,j):
    if(str[i]!=str[j]):
        print("Not a palindrome")
        return
    elif(i>j):
        print("Paindrome")
        return
    else:
        palindrome(str,i+1,j-1)
str=input()
i=0
j=len(str)-1
palindrome(str,i,j)
