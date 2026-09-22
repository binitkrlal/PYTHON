x=int(input())
p=input()
for i in range(x):
    for j in range(i,x-1):
        print(" ",end='')
    for j in range(i+1):
        print(p,end='')
    print()
for i in range(x):
    for j in range(x):
        print(" ",end='')
    for j in range(x,i,-1):
        print(p,end='')
    print()
for j in range(x*2):
    print("_",end='')
print()
for i in range(x):
    for j in range(x):
        print(" ",end='')
    for j in range(i,x-1):
        print(" ",end='')
    for j in range(i+1):
        print(p,end='')
    print()
for i in range(x):
    for j in range(x,i,-1):
        print(p,end='')
    print()