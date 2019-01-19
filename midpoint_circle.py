import matplotlib.pyplot as plt

def Drawcircle(x_off, y_off, r):
    xs =[]
    ys =[]
    x = 0
    y = r
    p = 5/4.0 - r # 决策
    xs.append(x)
    ys.append(y)
    while x < y:
        if p < 0:
            x += 1
            p += 2*x + 1
        else:
            x += 1
            y -= 1
            p += 2*(x-y) + 1
        xs.append(x)
        ys.append(y)
    plt.show()
    plt.axis('equal')
    plt.axvline(x=0,linewidth=1, color='k')#v x轴
    plt.axhline(y=0,linewidth=1, color='k')#h y轴
    plt.axis([-50, 50, -50, 50])
    plt.xlabel('x')
    plt.ylabel('y')
    for i in range(0,len(xs)):
        if i == 0:
            plt.scatter(xs[i]+x_off,ys[i]+y_off,color='k',s=1)
            plt.scatter(xs[i]+x_off,-ys[i]+y_off,color='k',s=1)
            plt.scatter(ys[i]+x_off,xs[i]+y_off,color='k',s=1)
            plt.scatter(ys[i]+x_off,-xs[i]+y_off,color='k',s=1)
            plt.pause(0.1)
        else:
            plt.scatter(xs[i]+x_off,ys[i]+y_off,color='k',s=1)
            plt.scatter(-xs[i]+x_off,ys[i]+y_off,color='k',s=1)
            plt.scatter(xs[i]+x_off,-ys[i]+y_off,color='k',s=1)
            plt.scatter(-xs[i]+x_off,-ys[i]+y_off,color='k',s=1)
            plt.scatter(ys[i]+x_off,xs[i]+y_off,color='k',s=1)
            plt.scatter(-ys[i]+x_off,xs[i]+y_off,color='k',s=1)
            plt.scatter(ys[i]+x_off,-xs[i]+y_off,color='k',s=1)
            plt.scatter(-ys[i]+x_off,-xs[i]+y_off,color='k',s=1)
            plt.pause(0.1)
            plt.draw()
    plt.show()


Drawcircle(2,8,10)
