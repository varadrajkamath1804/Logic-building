# Problem 1: First Non-Repeating Element

arr = [4, 5, 1, 2, 0, 4, 5]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for num in arr:
    if freq[num] == 1:
        print(num)
        break
