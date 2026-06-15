nums = [2, 1, 5, 1, 3, 2]
k = 3

n = len(nums)

# First window
window_sum = sum(nums[:k])
max_sum = window_sum

print(f"Initial Window: {nums[:k]}")
print(f"Initial Sum: {window_sum}")

for left in range(n - k):
    outgoing = nums[left]
    incoming = nums[left + k]

    print("\n------------------")
    print(f"Removing: {outgoing}")
    print(f"Adding: {incoming}")

    window_sum = window_sum - outgoing + incoming

    print(f"New Window Sum: {window_sum}")

    if window_sum > max_sum:
        max_sum = window_sum
        print(f"New Max Sum: {max_sum}")

print("\nFinal Answer")
print(max_sum)
