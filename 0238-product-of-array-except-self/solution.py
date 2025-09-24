class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = []
        storedBeforeI = []
        storedAfterI = []
        lengthNum = len(nums)
        productBefore = 1
        productAfter = 1

        for number in range(lengthNum):
            productBefore *= nums[number]
            storedBeforeI.append(productBefore) 
        
        for j in range(lengthNum-1, -1, -1):
            productAfter *= nums[j]
            storedAfterI.append(productAfter)

        index = 0
        indexBefore = 0
        indexAfter = lengthNum - 3
        while index < lengthNum:
            if index == 0:
                result.append(storedAfterI[lengthNum-2])
            elif index == lengthNum-1:
                result.append(storedBeforeI[lengthNum-2])
            else:
                result.append(storedBeforeI[indexBefore]*storedAfterI[indexAfter])
                indexBefore += 1
                indexAfter -= 1
            index += 1    
            
        return result

        

