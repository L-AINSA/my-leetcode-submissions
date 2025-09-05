class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
        indexVowels = []
        charVowels = []
        sArray = []
        lenghS = len(s)
        for i in range(lenghS):  #better to write a bigger if 
            if s[i] in vowels:
                indexVowels.append(i)
                charVowels.append(s[i])
            
            sArray.append(s[i])
        
       # print("sArray: ", sArray)
       # print("indexVowels: ", indexVowels)
       # print("charVowels: ", charVowels)

        reversedVowels = charVowels[::-1]

       # print("reverse: ", reversedVowels)

        lenghIndexVowels = len(indexVowels)

        for i in range(lenghIndexVowels):
            sArray[indexVowels[i]] = reversedVowels[i]

        result = "".join(sArray)

        return result

# notes from code samples: arr = list(s)

