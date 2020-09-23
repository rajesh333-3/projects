# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 17:42:05 2020

@author: VenkataDurgaRajesh
"""

l=list("1,2,3,4,5,6".split(','))
print(l[0])

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(nums[i]+nums[j] == target and i != j):
                return [i,j]
                break
ans=twoSum([3,3],6)
print(ans)

# just adding to learn git commit+ one  more trail
