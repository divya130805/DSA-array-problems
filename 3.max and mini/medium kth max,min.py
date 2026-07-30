def func(arr,k):
        arr.sort()
        return (arr[k-1])
print(func([1,2,3,4,5,6,7,8],4))

def func1(arr,k):
        arr.sort(reverse=True)
        return(arr[k-1])
print(func1([1,2,3,4,5,6,7,8],2))
