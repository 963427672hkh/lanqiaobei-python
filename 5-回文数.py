import os
import sys

# 请在此输入您的代码
# for i in range(1,10):
#     for j in range(0,10):
#         nums = i*1000+j*100+j*10+i
#         print(nums)

for i in range(10,100):
    i = str(i)
    num = int(i+i[::-1])
    print(num)