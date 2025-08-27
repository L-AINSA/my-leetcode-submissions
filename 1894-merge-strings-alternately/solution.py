class Solution(object):

    def mergeAlternately(self, word1, word2):

        merged = ""

        if len(word1) == len(word2):
            for i in range(len(word1)):
                merged = merged + word1[i] + word2[i]
                
        elif len(word1) < len(word2):
            for i in range(len(word1)):
                merged = merged + word1[i] + word2[i]
                
            merged = merged + word2[len(word1):]
    
        elif len(word1) > len(word2):
            for i in range(len(word2)):
                merged = merged + word1[i] + word2[i]
                
            merged = merged + word1[len(word2):]
        return merged


            
