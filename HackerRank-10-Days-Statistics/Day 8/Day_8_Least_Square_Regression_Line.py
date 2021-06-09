# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
S1,S2,S3,S4,S5=sys.stdin.readlines()
n=5

S1=list(map(int,S1.strip().split()))
S2=list(map(int,S2.strip().split()))
S3=list(map(int,S3.strip().split()))
S4=list(map(int,S4.strip().split()))
S5=list(map(int,S5.strip().split()))

x=[S1[0],S2[0],S3[0],S4[0],S5[0]]
y=[S1[1],S2[1],S3[1],S4[1],S5[1]]

S_X=sum(x)
S_Y=sum(y)
x_y=[x[i]*y[i] for i in range(n)]
S_XY=sum(x_y)
x_2=[x[i]**2 for i in range(n)]
S_X2=sum(x_2)

b=(n*S_XY - (S_X*S_Y))/(n*S_X2-S_X**2)

x_mean = S_X/n
y_mean=sum(y)/n

a=y_mean-b*x_mean

x=80

print(round(a+b*x,3))
