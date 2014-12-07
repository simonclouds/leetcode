class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        m = {}
        firstIndex = 1;
        secondeIndex = 1;
        
        for i in range(0,len(num)):
            if(m.get(num[i]) == None):
                m[target - num[i]] = i;
            else:
                firstIndex = m.get(num[i]) + 1
                secondIndex = i + 1
                return (firstIndex,secondIndex);
