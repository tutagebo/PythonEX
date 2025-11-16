from turtle import *
# ex2と同様に正7角形の星型は3.5、正9角形の星型は4.5角形
n = 9/2
sx, sy = pos()
while True:
    forward(100)
    left(360/n)
    x, y = pos()
    # いちおう誤差吸収
    if abs(x - sx) < 1e-6 and abs(y - sy) < 1e-6:break
done()
