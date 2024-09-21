class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(t)
        m = len(s)

        j = 0 
        if s == "":
            return True 
        if n < m :
            return False    
        for i in range(n):
            if j < m and s[j]==t[i]:
                j +=1
            
        return j == m   
  
        
        