Numbers = [-1,-1,-1,-1,-1,-1,-1]
Find = 60
low = 0
mid = ""
high = len(Numbers) - 1
while low <= high:
    mid = (low + high) // 2
    if Numbers[mid] > Find:
        high = mid - 1
    elif Numbers[mid] < Find:
        low = mid + 1
    else:
        break

print(mid)
