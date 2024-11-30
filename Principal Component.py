import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#reading data
df = pd.read_csv('magic04.data', delimiter= ',', index_col=False)
data = df.to_numpy()
#calculation of covariance
n,d1 = data.shape
D=data[:,:d1-1]
temp= np.copy(D)
n,d = temp.shape
mu=temp.mean(axis=0)
for i in range(d):
   temp[:,i]=temp[:,i]-mu[i]
D2=temp.astype('float64')
covD2 = np.cov(D2,rowvar=False)
#creatig y and calculation eigen-vector and eigenvalue
y=[]
x=D[0,:]
x1=np.copy(x.T)
y=np.dot(covD2,x1)
sizy=np.sqrt(np.sum((y ** 2)))
normaly=y/sizy
e=np.sqrt(np.sum(((x-y )** 2)))
while e>=0.0001 :
    x1=np.copy(normaly)
    maxx=np.max(x1)
    y=np.copy(np.dot(covD2,x1))
    sizy=np.sqrt(np.sum((y ** 2)))
    normaly=y/sizy
    maxy=np.max(y)
    e=np.sqrt(np.sum(((x1-normaly )** 2))) 
eigenvalue=maxy/maxx
print("eigenvalue = " ,eigenvalue)
print('=========')
print("eigen-vector = " ,normaly)
print('=========')
sizy=np.sqrt(np.sum((normaly ** 2)))
print("lenght-vector = " ,sizy)
print('=========')
#w,v=np.linalg.eig(covD2)
#print(w)
