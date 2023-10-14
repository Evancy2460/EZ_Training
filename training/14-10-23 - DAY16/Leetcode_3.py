#3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        k=[]
        high=1
        for i in range(len(s)):
            c=1
            k.append(s[i])
            j=i+1
            while(j<len(s)):
                if s[j] in k:
                    k=[]
                    break
                else:
                    k.append(s[j])
                    c+=1
                    j+=1
            if (c>high):
                high=c       
        return high


'''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,c=0,0
        se=set()
        for j in range(len(s)):
            while s[j] in se:
                se.remove(s[i])
                i+=1
            se.add(s[j])
            c=max(c,(j-i+1))
        return c'''

    
