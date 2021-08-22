def ars(arr,n):
    sums=1
    for i in arr:
        sums=sums*(i%n)

    return int(sums%n)




arr = [100, 10, 5, 25, 35, 14,277]
n = 11

print(ars(arr,n))