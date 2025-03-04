import os
import sys

# 请在此输入您的代码
n = int(input())
print(sum(list(map(int,input().split()))))

# map(f,nums) 将可迭代数据nums依次代入f函数
# sum(nums) 将可迭代数据nums求和，结果为字符串
# x.split() 将按照x（默认）空格分隔