mec=input()
x=input()
A=[x]
a=1
y=0
for i in range(len(mec)):
    if A[a]==5:
        y=y+1                            
        a=a+1
    else:
        a=a+1
    print(y)
print(len(mec))
