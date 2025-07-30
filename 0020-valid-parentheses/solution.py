class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        checkStack = []
        value = str
        valid = True

        for i in range(0, len(s)):

            if s[i] == "(":
                checkStack.append(s[i])
            elif s[i] == "[":
                checkStack.append(s[i])
            elif s[i] == "{":
                checkStack.append(s[i])

            elif s[i] == ")":
                if len(checkStack) != 0:
                    value = checkStack.pop()
                    if value != "(":
                        valid = False
                        break
                else:
                    valid = False
                    break
                    
            elif s[i] == "]":
                if len(checkStack) != 0:
                    value = checkStack.pop()
                    if value != "[":
                        valid = False
                        break
                else:
                    valid = False
                    break
            elif s[i] == "}":
                if len(checkStack) != 0:
                    value = checkStack.pop()
                    if value != "{":
                        valid = False
                        break
                else:
                    valid = False
                    break
        if len(checkStack) != 0:
            valid = False

       
        return valid
