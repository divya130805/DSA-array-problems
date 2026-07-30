def func(arr1,arr2):
    for i in range(min(len(arr1),len(arr2))):
        if arr1[i]==arr2[i]:
            return True
    return False

print(func([1,2,3,4,5,6],[6,7,77,7]))