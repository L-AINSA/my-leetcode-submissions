class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        for i in candies:
            iExtra = i + extraCandies
            if iExtra >= max(candies):
                result.append(True)
            else:
                result.append(False)

        return result
        


      
        
