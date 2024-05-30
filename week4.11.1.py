def power(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

# 測試函式
x = 2
n = 3
print("2 的 3 次方為:", power(x, n))  # 輸出: 8

