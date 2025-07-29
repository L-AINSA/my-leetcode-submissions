class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        indexOuter = 0
        answerArray = [0]*2

        for i in nums:
            for j in range(indexOuter+1, len(nums)):
                 if nums[indexOuter]+nums[j] == target:
                    answerArray[0]=indexOuter
                    answerArray[1]=j
                    return answerArray
            indexOuter += 1
        return answerArray







        
