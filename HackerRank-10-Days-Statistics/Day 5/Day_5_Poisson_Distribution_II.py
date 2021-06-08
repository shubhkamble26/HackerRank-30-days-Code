# Enter your code here. Read input from STDIN. Print output to STDOUT
lamda1,lamda2=list(map(float,input().strip().split()))

print(round(160+40*(lamda1 + lamda1**2),3))
print(round(128+40*(lamda2 + lamda2**2),3))