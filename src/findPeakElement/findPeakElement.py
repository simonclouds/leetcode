class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        numlen = len(num)
        if numlen == 1:
            return 0
        else:
            for i in range(0,numlen-1):
                if num[i] > num[i+1]:
                    return i;
            return numlen-1;
    
