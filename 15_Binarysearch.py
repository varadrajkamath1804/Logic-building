nums = [1, 3, 5, 7, 9, 11, 13]
target = 9

first = 0
last = len(nums) - 1

while first <= last:
    mid = (first + last) // 2

    print(f"first={first}, last={last}, mid={mid}")

    if nums[mid] == target:
        print(f"Target found at {mid}")
        break

    elif target < nums[mid]:
        last = mid - 1

    else:
        first = mid + 1

else:
    print(None)
