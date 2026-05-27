import math

d = float(input())
w = float(input())
n = int(input())

table_circumference = math.pi * d
required_space = n * w

if table_circumference >= required_space:
    print("YES")
else:
    print("NO")
