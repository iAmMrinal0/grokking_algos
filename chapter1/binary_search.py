def binary_search(arr, num):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == num:
            return mid
        if guess < num:
            low = mid + 1
        else:
            high = mid - 1
    return None


def rec_search(arr, num, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    if arr[mid] == num:
        return mid
    if arr[mid] > num:
        return rec_search(arr, num, low, mid - 1)
    if arr[mid] < num:
        return rec_search(arr, num, mid + 1, high)
    return None


a = [10, 12, 23, 34, 55, 76, 87, 98, 109, 110]
print(binary_search(a, 2))
print(rec_search(a, 2, 0, len(a) - 1))

print(binary_search(a, 109))
print(rec_search(a, 109, 0, len(a) - 1))
