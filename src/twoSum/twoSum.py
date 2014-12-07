class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        letarget = len(num) -1;
        
        while num[letarget] > target:
            letarget = letarget - 1;
        
        for i in range(0,letarget):
            firstnum = num[i]
            diff = target - firstnum;
            
            secondnumlast = letarget;
            while num[secondnumlast] > diff:
                secondnumlast = secondnumlast-1;
            for j in range(i+1, secondnumlast+1):
                if num[i] + num[j] == target:
                    return (i+1,j+1);
