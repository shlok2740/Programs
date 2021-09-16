def PairSum(arr,s):
    n= len(arr)
    q=0
    for i in arr:
        q+=i
        if q == s:
            return i

arr=[1,2,3,4,5]
a=PairSum(arr,7)
print(a)
