class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=[]
        for i in s:
            if i.isalnum():
                t.append(i.upper())
        n=len(t)
        for i in range(len(t)//2):
            if t[i]!=t[n-1-i]:
                return False
        return True