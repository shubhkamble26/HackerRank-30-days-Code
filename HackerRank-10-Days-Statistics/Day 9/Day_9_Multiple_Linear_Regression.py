# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
import sys
a=sys.stdin.readlines()
col, n_train=list(map(int ,a[0].strip().split()))

x_train=[]
x_test=[]

for i in range(1,n_train+ 1):
    x_train.append(list(map(float,a[i].strip().split())))
    
n_test=int(a[n_train+1])
for j in range(n_train+2,n_train+2+n_test):
    x_test.append(list(map(float,a[j].strip().split())))
    
for k in range(n_test):
    x_test[k].insert(0,1.0)
    
x_test=np.array(x_test)
    

for i in range(n_train):
    x_train[i].insert(0,1.0)
       
x_train=np.array(x_train)
y_train=x_train[:,-1]
x_t=x_train[:,:-1]

xT=np.transpose(x_t)
B=np.array(np.dot(np.linalg.inv(np.dot(xT,x_t)),np.dot(xT,y_train)))

y_test=np.dot(B, np.transpose(x_test))
for i in y_test:
    print(round(i,2))
    
