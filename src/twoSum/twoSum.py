class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        for i in range(0,len(num)):
            for j in range(i+1,len(num)):
                if num[i] + num[j] == target:
                    return (i,j);
