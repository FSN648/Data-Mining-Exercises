import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#calculation of covariance
df = pd.read_csv('magic04.data', delimiter= ',', index_col=False)
data = df.to_numpy()
n,d1 = data.shape
D=data[:,:d1-1]
temp= np.copy(D)
n,d = temp.shape
mu=temp.mean(axis=0)
for i in range(d):
   temp[:,i]=temp[:,i]-mu[i]
D2=temp.astype('float64')
covD2 = np.cov(D2,rowvar=False)
#creatig s,r and calculation of a,b
s=np.array([[1,2],[4,4],[1,6],[4,5],[5,2],[5,1],[2,4],[2,5],[4,1],[6,4]])
s0=s[:,0]
s1=s[:,1]
sizs0=np.sqrt(np.sum((s0 ** 2)))
sizs1=np.sqrt(np.sum((s1 ** 2)))
normals0=s0/sizs0
normals1=s1/sizs1
new_s=np.zeros([10,2])
new_s[:,0]=normals0
new_s[:,1]=normals1
r=np.dot(covD2,new_s)
a=r[:,0]
b=r[:,1]
b=b-((np.dot(b.T,a)/np.dot(a.T,a))*a)
siza=np.sqrt(np.sum((a ** 2)))
sizb=np.sqrt(np.sum((b ** 2)))
normala=a/siza
normalb=b/sizb
r[:,0]=normala
r[:,1]=normalb
sigma=np.sqrt(np.sum(((r-new_s )** 2)))
while sigma>=0.001:
   s=np.copy(r)
   r=np.dot(covD2,s)
   a=r[:,0]
   b=r[:,1]
   b=b-((np.dot(b.T,a)/np.dot(a.T,a))*a)
   siza=np.sqrt(np.sum((a ** 2)))
   sizb=np.sqrt(np.sum((b ** 2)))
   normala=a/siza
   normalb=b/sizb
   r[:,0]=normala
   r[:,1]=normalb
   sigma=np.sqrt(np.sum(((r-s )** 2)))
#creatig u
u=np.zeros([10,2])
u[:,0]=normala
u[:,1]=normalb
print('u=',u)
print('=========')
#projection of points in new basis
new_D=np.dot(u.T,D.T)
print('new_D=', new_D)
#drawing chart
x=new_D[0,:]
y=new_D[1,:]
fig = plt.figure()
plt.scatter(x, y, alpha=0.5)
plt.title('Scatter for 2D')
plt.xlabel('Attribute1')
plt.ylabel('Attribute2')
plt.show()

