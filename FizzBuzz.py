class Solution(object):
    def fizzBuzz(self, n):
        responses = []

        for i in range(1, n + 1):
            if i % 3 == 0:
                if i % 5 == 0:
                    responses.append("FizzBuzz")
                else:
                    responses.append("Fizz")
            elif i % 5 == 0:
                responses.append("Buzz")
            else:
                responses.append(str(i))

        return responses
# 5 2