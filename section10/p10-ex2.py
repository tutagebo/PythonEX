from turtle import *
# 昔なんかの動画で星型は正2.5角形と言えると聞いたことがあった
n = 5/2
sx, sy = pos()
while True:
    forward(100)
    left(360/n)
    x, y = pos()
    if abs(x - sx) < 1e-6 and abs(y - sy) < 1e-6:break
done()
