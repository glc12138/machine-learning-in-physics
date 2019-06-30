import pycuda.autoinit
import pycuda.gpuarray as gpuarray
import numpy as np
#import skcuda.linalg as linalg
#from skcuda.linalg import PCA as cuPCA
import matplotlib.pyplot as plt
#from sklearn.decomposition import PCA
import pca_lc as PCA
#import sklearn as sk
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans


size = 10
lenth = 640
sample = 25
lenth = lenth * lenth

f1 = open("perco.txt","r")
f2 = open("result.txt","r")
x1 = f1.read()
x2 = f2.read()
f1.close()
f2.close()


y1 = x1.split()
y2 = x2.split()
y1 = np.array(y1,dtype="float32")
#k1 = [float(m) for m in y1]
k2 = [int(n) for n in y2]
k1 = np.reshape(y1, (size*sample, lenth))
k2 = np.reshape(k2, (size, sample))
##for pr in range(1,10):
  ##  k1[pr*sample,:] = k1[pr*sample,:]*100.0/(pr+55)

k1 = PCA.pca_lca(k1)
#k1 = sk.preprocessing.normalize(k1)
#pca.fit(k1)
#k1 = pca.transform(k1)
print(k1[:,:3])


y=np.zeros(size)
z=np.zeros(size)
q=np.zeros(size)
y[0]=k1[0,2]
z[0]=k1[0,1]
q[0]=k1[0,0]

m=np.zeros(size)
m=k1[:,:3]
kmeans = KMeans(n_clusters=2, random_state=0).fit_predict(m)
plt.scatter(m[:,0],m[:,1],c=kmeans)
plt.figure()
#y[0,0]=k1[0,0]
#y[0,1]=k1[0,1]
#y[0,2]=k1[0,2]
k1[:,1] = np.absolute(k1[:,1])
k1[:,0] = np.absolute(k1[:,0])
k1[:,2] = np.absolute(k1[:,2])
for i in range(0,size):
    for j in range(0,sample):
        y[i]=y[i]+k1[(i+1)*j,2]
        z[i]=z[i]+k1[(i+1)*j,1]
        q[i]=q[i]+k1[(i+1)*j,0]

x=np.linspace(0.55,0.64,10)
plt.title("k1[:,1]")
plt.scatter(x,y)
plt.figure()
np.savetxt('fig(3-d)-640-10-25',(y,z,q))


plt.title("x-y is 1-2")
plt.scatter(k1[:,1],k1[:,2],c=k1[:,0])
plt.figure()
plt.title("x-y is 0-1")
plt.scatter(k1[:,0],k1[:,1],c=k1[:,0])
plt.figure()
plt.title("x-y is 0-2")
plt.scatter(k1[:,0],k1[:,2],c=k1[:,0])
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

ax.scatter(k1[:,0],k1[:,1],k1[:,2])
plt.show()


#X_gpu = gpuarray.GPUArray((lenth,size*100), np.float64, order='F')
#k1 = np.transpose(k1)
#X_gpu.set(k1)
#print(len(X_gpu[:,0]))
#print(len(X_gpu[:,1]))



#pca = cuPCA()
#T_gpu = pca.fit_transform(X_gpu)
#print(T_gpu[:,0])
#print(T_gpu[:,1])
#print("\n")
#linalg.dot(T_gpu[:,0], T_gpu[:,1])
#print(T_gpu[:,0])
#print(T_gpu[:,1])
