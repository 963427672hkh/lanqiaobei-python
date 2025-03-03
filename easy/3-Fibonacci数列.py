import os
import sys

# 请在此输入您的代码
n =int(input())
if n<=2:
    print(1)
else: 
    nums = i = 1
    while(n-2 != 0):
        t = nums
        nums += i
        i = t
        n-=1
    print(nums)