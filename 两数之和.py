#!/bin/env python3
# -*- coding: utf-8 -*-
#Author zhangkaiyue1@cmcm.com

'''
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

nums = [2, 15, 11, 7]
target = 9

# 我的答案
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             print(i,j)


# 标答
def twoSum(nums,target):
    dict = {}
    for i,num in enumerate(nums):
        if num in dict:
            return [dict[num],i]
        else:
            dict[target - num] = i

result = twoSum(nums,target)

print(result)



