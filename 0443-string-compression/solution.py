class Solution:
    def compress(self, chars: List[str]) -> int:
        length  = len(chars)
        count = 1
        currentChar = chars[0]
        s = []
        loopCount = 1
        for i in range(1, length):
            print(f"****This is loop #{loopCount}****")

            print(f"current char is {currentChar}")
            print(f"loop char is {chars[i]}")
            print(f"count is {count}")
            if chars[i] == currentChar:
                print("comprarision:")
                print(f"chars[i]  {chars[i]}  == {chars[i] == currentChar} currentChar {currentChar}  ")
                count += 1
                currentChar = chars[i]
                print(f"count is {count}")
                print(f"currentChar is {currentChar}")

            else:
                if count == 1:
                    s.append(currentChar)
                    count = 1
                    currentChar = chars[i]
                elif count < 10:
                    s.append(currentChar)
                    s.append(str(count))
                    count = 1
                    currentChar = chars[i]
                else:
                    s.append(currentChar)
                    countStr = str(count)
                    for j in countStr:
                        s.append(j)
                    count = 1
                    currentChar = chars[i]
            loopCount +=1
        
        print(f"count is {count}")
        if count == 1:
            s.append(currentChar)

        elif count < 10:
            s.append(currentChar)
            s.append(str(count))
                
        else:
            s.append(currentChar)
            countStr = str(count)
            for i in countStr:
                s.append(i)       

        print(s)

        lengthS = len(s)
        chars[0:6] = s
        return lengthS
