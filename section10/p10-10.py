from turtle import *
import math

# config
color("blue")

# パラメータ
# 参考 https://www.mathartroom.com/lissajous/lissajous_n3_angels/
A = [60, 30, 15]       # A1, A2, A3
B = [60, 30, 30]        # B1, B2, B3

wx = [1, 4, 10]        # ωx1, ωx2, ωx3
wy = [1, 3, 6]        # ωy1, ωy2, ωy3

thx = [0, 0, 0]   # θx1, θx2, θx3
thy = [math.pi/2, math.pi/2, math.pi/2]   # θy1, θy2, θy3

# リサージュ
def lissajous_x(t):
    return sum(A[i] * math.sin(wx[i] * t + thx[i]) for i in range(3))

def lissajous_y(t):
    return sum(B[i] * math.sin(wy[i] * t + thy[i]) for i in range(3))

# 描画開始
T = 2000   # 分割数
tmax = 2 * math.pi * 10  # 何周描くか

penup()
for k in range(T + 1):
    t = tmax * k / T
    x = lissajous_x(t)
    y = -lissajous_y(t) # なんか上下逆だったので反転
    goto(x, y)
    pendown()

done()
