import matplotlib.pyplot as plt

def DrawBre(x1,y1,x2,y2):
    steep = 0
    dx = abs(x2 - x1)
    if (x2 - x1) > 0: sx = 1
    else: sx = -1
    dy = abs(y2 - y1)
    if (y2 - y1) > 0: sy = 1
    else: sy = -1
    if dy > dx:# k > 1
        steep = 1
        x1,y1 = y1,x1
        dx,dy = dy,dx
        sx,sy = sy,sx
    d = (2 * dy) - dx
    xs =[]
    ys=[]
    x = x1; y = y1
    for i in range(0,dx):
        if steep: 
            xs.append(y)
            ys.append(x)
        else:
            xs.append(x)
            ys.append(y)
        while d >= 0:
            y = y + sy
            d = d - (2 * dx)
        x = x + sx
        d = d + (2 * dy)
    xs.append(x2)
    ys.append(y2)
    plt.show()
    plt.axvline(x=0,linewidth=1, color='k')#v x轴
    plt.axhline(y=0,linewidth=1, color='k')#h y轴
    plt.axis([-50, 50, -50, 50],'equal')
    plt.xlabel('x')
    plt.ylabel('y')
    for i in range(len(xs)):
        plt.scatter(xs[i],ys[i],color='k',s=1)
        plt.pause(0.1)
        plt.draw()
    plt.show()

DrawBre(1,3,20,9)
