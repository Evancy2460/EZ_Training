def substring(self, str1,substr):
    res=[]
    def backtrack(i,curstr):
        if len(curstr)==len(digits):
            res.append(curstr)
            return
        for c in d[digits[i]]:
            backtrack(i+1,curstr+c)
    if digits:
        backtrack(0,'')
    return res
str1=input()
substr=input()
print(substring(str1,substr))
        















