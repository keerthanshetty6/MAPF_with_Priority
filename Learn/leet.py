class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dist=[[nums[0],abs(nums[0])]]
        for i in nums:  
            if abs(i)<=dist[0][1]:
                if abs(i)<dist[0][1]:
                    dist[0][0] =i
                    dist[0][1]=abs(i)
                else:
                    dist[0][0]=max(i,dist[0][0])
        return dist[0][0]

nums=[-4,-2,1,4,8]
sol=Solution()
print(sol.findClosestNumber(nums))

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data,columns=["a","b"])
    