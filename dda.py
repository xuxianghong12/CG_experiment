import matplotlib.pyplot as plt

def ROUND(a):
	return int(a + 0.5)

def DrawDDA(x1,y1,x2,y2):
    xs = []
    ys = []
    x,y = x1,y1
    xs.append(ROUND(x))
    ys.append(ROUND(y))
    dx = int(x2-x1)
    dy = int(y2-y1)
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    xInc = float(dx) / float(steps)
    yInc = float(dy) / float(steps)
    for i in range(steps):
        x += xInc
        y += yInc
        xs.append(ROUND(x))
        ys.append(ROUND(y))
    plt.show()
    plt.axvline(x=0,linewidth=1, color='k')#v x轴
    plt.axhline(y=0,linewidth=1, color='k')#h y轴
    plt.axis([-50, 50, -50, 50],'equal')
    plt.xlabel('x')
    plt.ylabel('y')
    for i in range(0,len(xs)):
        plt.scatter(xs[i],ys[i],color='k',s=1)
        plt.pause(0.1)
        plt.draw()
    plt.show()
DrawDDA(1,3,20,9)
