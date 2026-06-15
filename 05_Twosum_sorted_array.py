nums = [2, 5, 6, 7]
target = 8

left = 0
right = len(nums) - 1

while left < right:
    print(
        f"left={left} ({nums[left]}), "
        f"right={right} ({nums[right]}), "
        f"sum={nums[left] + nums[right]}"
    )
    if nums[left] + nums[right] == target:
        print(True)
        break
    elif nums[left] + nums[right] > target:
        right = right - 1
    elif nums[left] + nums[right] < target:
        left = left + 1
else:
    print(None)
