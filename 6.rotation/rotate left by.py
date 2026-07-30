def left_rotate(arr, k):
    n = len(arr)

    k = k % n

    temp = [0] * n

    for i in range(n - k):
        temp[i] = arr[i + k]

    for i in range(n - k, n):
        temp[i] = arr[i - (n - k)]

    for i in range(n):
        arr[i] = temp[i]


arr = [1, 2, 3, 4, 5, 6]
left_rotate(arr, 2)
print(arr)