import os
import sys

# 请在此输入您的代码

# bin(n)将n转化为二进制字符串表示
# n = 10
# n = bin(n)
# print(type(n))
# print(n)

# <class 'str'>
# 0b1010

# enumerate为枚举，列举。
# enumerate的作用就是对可迭代的数据进行标号并将其里面的数据和标号一并打印出来
# >>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# >>> list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
# >>> list(enumerate(seasons, start=1))       # 下标从 1 开始
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
num = int(input())

def transform(num):
    bin_num = bin(num)[2:][::-1]
    # [::-1]翻转字符串
    result = []
    
    for idx, para in enumerate(bin_num):
        if para == '1':
            if idx == 0:
                result.append('2(0)')
            elif idx == 1:
                result.append('2')
            else:
                result.append(f"2({transform(idx)})")
    result = result[::-1]
    return '+'.join(result)
    # str.join(n) 以字符串str分隔可迭代n,输出为字符串

print(transform(num))