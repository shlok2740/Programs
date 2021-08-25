s = input("enter a string")
half = int(len(s)/2)


if len(s)/2==0:
    first=s[:half]
    second=s[half:]
else :
    first=s[:half]
    second=s[half+1:]

if first==second:
    print("it\'s symmetrical")
else:
    print("it\'s not symmetrical")

if first==second[::-1]:
    print("it\'s a palindrome")
else:
    print("it\'s not a palindrome")