class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_symo = { "I" :1 , "V" :5 , "X":10 ,"L" :50 , "C":100 , "D":500 , "M":1000}
        count = 0 
        n = len(s)
        for i in range(n):
            if i < n-1 and roman_symo[s[i]] < roman_symo[s[i+1]]:
                count -= roman_symo[s[i]]
                i +=1
            else :
                count += roman_symo[s[i]]
                i += 1
        return count        


   