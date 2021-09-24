n=int(input())

a,b=0,1

if n>1:
    for i in range(2, n):
        a,b=b,a+b
    print(b)
