class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for i in range (1, n+1):
            if i%5==0 and i%3==0:
                #print(FizzBuzz)
                answer.append("FizzBuzz")
            elif i%3==0:
                #print("Fizz")
                answer.append("Fizz")
            elif i%5==0:
                #print("Buzz")
                answer.append("Buzz")
            else:
                #print(i)
                answer.append(str(i))
        return answer
