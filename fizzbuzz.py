class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lst=[]
        for i in range(1,n+1):

            if i%3 == 0 and i%5 == 0 :
                i="FizzBuzz"
            
            elif i%3==0:
                i="Fizz"
            elif i%5 == 0:
                i = 'Buzz'
            else:
                i = str(i)
            
            lst.append(i)
        return lst
