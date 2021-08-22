from math import sqrt
n=int(input('Enter the number: '))
m=0
if n>1:

  for i in range(2,int(sqrt(n))+1):
    if (n%i==0):
        m=1
        break
  if m==0:
    print(n, "is a prime number")
  else:
        print(n,'is not a prime number')

else:
    print("Error , your number is less than 1")
