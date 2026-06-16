s = "aabbcdde"
freq = {}

for i in s:
    freq[i] = freq.get(i, 0) + 1

for i in freq:
    if freq[i] == 1:
        print(i)
        break
else:
    print(None)
