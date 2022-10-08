import math

dx = 0.001
f0 = math.exp(1 - 0.001) * math.cos(1 - 0.001)
f1 = math.exp(1 - 0.0005) * math.cos(1 - 0.0005)
f2 = math.exp(1) * math.cos(1)
f3 = math.exp(1 + 0.0005) * math.cos(1 + 0.0005)
f4 = math.exp(1 + 0.001) * math.cos(1 + 0.001)

#前進差分商
print(f'前進差分商：{(f4 - f2) / dx}')

#後退差分商
print(f'後退差分商：{(f2 - f0) / dx}')

#中心差分商
print(f'中心差分商：{(f3 - f1) / dx}')