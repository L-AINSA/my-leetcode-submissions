class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        length = len(flowerbed)
        plantedTotal = sum(flowerbed)

        previousValue = int
        nextValue = int
        count = 0

        for i in range(0, length):
            if n == 0:
                return True
            elif length == 1:
                if n > 0:
                    if not flowerbed[i]:
                        return True
                    else:
                        return False
                else:
                    return True
            elif i == 0:
                if not flowerbed[i] and not flowerbed[i+1]:
                    flowerbed[i] = 1
                    count +=1
            elif i == length-1:
                if not flowerbed[i] and not flowerbed[i-1]:
                    flowerbed[i] = 1
                    count +=1
            elif not flowerbed[i] and not flowerbed[i-1] and not flowerbed[i+1]:
                flowerbed[i] = 1
                count += 1
            if  count == n:
                return True

        return False

            
        # 100001 count would be 2 but the answer is 1; 10000001 count would be 4 but the answer is 2
        # 1000000001 count = 6   answer= 3
        # needs to be a 0 and to have 0s on both sides 

        
