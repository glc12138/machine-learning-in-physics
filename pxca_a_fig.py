import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


y1=np.loadtxt('fig(3-d)-160-10-100')
y2=np.loadtxt('fig(3-d)-320-10-100')
y3=np.loadtxt('fig(3-d)-320-20-25')
y4=np.loadtxt('fig(3-d)-640-20-25')


for i in range(3):
    max1=np.amax(y1[i,:])
    min1=np.amin(y1[i,:])
    max2=np.amax(y2[i,:])
    min2=np.amin(y2[i,:])
    max3=np.amax(y3[i,:])
    min3=np.amin(y3[i,:])
    max4=np.amax(y4[i,:])
    min4=np.amin(y4[i,:])
    y1[i,:]=(y1[i,:]-min1)/(max1-min1)
    y2[i,:]=(y2[i,:]-min2)/(max2-min2)
    y3[i,:]=(y3[i,:]-min3)/(max3-min3)
    y4[i,:]=(y4[i,:]-min4)/(max4-min4)
#    y1[i,:]=y1[i,:]/max1
#    y2[i,:]=y2[i,:]/max2

x1=np.linspace(0.55,0.65,10)
plt.xlabel("possible")
plt.ylabel("principal component")
#plt.scatter(x1,y1[1,:],c="green")
#plt.scatter(x1,y2[1,:],c="red")
x2=np.linspace(0.5,0.7,20)
#plt.scatter(x2,y3,c="black")
#plt.scatter(x2,y4,c="blue")


x1=np.linspace(0.55,0.65,10)
plt.xlabel("possible")
plt.ylabel("principal component")
#legend((line1, line2, line3),('1','2','3'))
plt.plot(x1,y1[1,:],c="green")
plt.plot(x1,y2[1,:],c="red")
x2=np.linspace(0.5,0.7,20)
#plt.plot(x2,y3[1,:],c="black")
#plt.plot(x2,y4[1,:],c="blue")





plt.show()
