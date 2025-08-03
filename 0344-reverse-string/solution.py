class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        back_i = -1
        hold = str

        while i < int(len(s)/2):
            hold = s[i]
            s[i] = s[back_i]
            s[back_i] = hold
            i+=1
            back_i-=1
 
