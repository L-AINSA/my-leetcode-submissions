class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        currentWordChar = []
        currentWord = []
        wordsInReverse = []
        length = len(s)


        for i in range(length):
            if s[i] == " ":
                continue
                
            if s[i] != " ":
                currentWordChar.append(s[i])
                if i+1 <= length-1 and s[i+1] == " ":
                    currentWord.append("".join(currentWordChar))
                    currentWordChar = []
                    wordsInReverse.insert(0,currentWord.pop())
                elif i == length-1:
                    currentWord.append("".join(currentWordChar))
                    currentWordChar = []
                    wordsInReverse.insert(0,currentWord.pop())
        
        
        result = " ".join(wordsInReverse)
        return result

        
