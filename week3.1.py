# 初始化奇數和
odd_sum = 0

# 遍歷範圍 1 到 100，步長為2，以確保只有奇數
for i in range(1, 101, 2):
    odd_sum += i

print("1 到 100 中所有奇數的和為:", odd_sum)
