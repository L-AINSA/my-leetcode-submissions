class Solution(object):
    def gcdOfStrings(self, str1, str2):
        largestString = ""

        if(len(str1) > len(str2)):
            longerWord = str1
            shorterWord = str2
        else:
            longerWord = str2
            shorterWord = str1 

        for i in range(min(len(str1), len(str2))):
            splitArrShort = shorterWord.split(shorterWord[:i+1])
            splitArrLong = longerWord.split(shorterWord[:i+1])

            splitArrShortWord = "".join(splitArrShort)
            splitArrLongWord = "".join(splitArrLong)
            
            if splitArrShortWord == "" and splitArrLongWord == "":
                largestString = shorterWord[:i+1]
                
        return largestString     
