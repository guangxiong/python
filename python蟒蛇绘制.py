import turtle

def drawsnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300, 800, 0, 0)   #启动窗体的大小
    pythonsize = 30     #轨迹宽度
    turtle.pensize(pythonsize)    #绘制轨迹
    turtle.pencolor("purple")   #轨迹颜色
    turtle.seth(-40)   #启动时方向
    drawsnake(40,80,5,pythonsize/2)  #调用绘制函数

main()
