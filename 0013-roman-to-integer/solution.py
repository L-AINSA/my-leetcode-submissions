class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        reprD = {
            "I" : "1",
            "V" : "5",
            "X" : "10",
            "L" : "50",
            "C" : "100",
            "D" : "500",
            "M" : "1000"
         }
        number = 0
        i = 0

        while i < len(s):
            try:
                if s[i+1]:
                    if reprD.get(s[i]) == "1" and reprD.get(s[i+1]) == "5":
                        number += 4
                        i += 1 
                    
                    elif reprD.get(s[i]) == "1" and reprD.get(s[i+1]) == "10":
                        number += 9
                        i += 1 
                    
                    elif reprD.get(s[i]) == "10" and reprD.get(s[i+1]) == "50":
                        number += 40
                        i += 1
                    
                    elif reprD.get(s[i]) == "10" and reprD.get(s[i+1]) == "100":
                        number += 90
                        i += 1

                    elif reprD.get(s[i]) == "100" and reprD.get(s[i+1]) == "500":
                        number += 400
                        i += 1 

                    elif reprD.get(s[i]) == "100" and reprD.get(s[i+1]) == "1000":
                        number += 900
                        i += 1 
                    
                    else:
                        number += int(reprD.get(s[i]))
            except IndexError:
                number += int(reprD.get(s[i]))

            i += 1

        return number
            
            
        

            
