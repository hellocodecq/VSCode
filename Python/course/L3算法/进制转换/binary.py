# 二进制与十进制的转换

def bin_to_d(num):
    num = str(num)
    size = len(num)	# 获取长度
    result = 0
    for i in range(-1, -size-1, -1):
        result += int(num[i])* 2 ** (abs(i)-1)
    return result			# 直接返回结果

def d_to_bin(num):      # 10进制数转2进制
    result = []
    while (num):
        result.insert(0,num%2)
        num //= 2
    if len(result) == 0:
        return 0
    return result

if __name__ == '__main__':
    print(d_to_bin(100))