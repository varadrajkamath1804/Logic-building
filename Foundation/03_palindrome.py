string = "damar"

n = len(string)
left = 0

right = n - 1
while left < right:
    if string[left] != string[right]:
        print(False)
        break
    left = left + 1
    right = right - 1
else:
    print(True)
