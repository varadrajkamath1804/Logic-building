s = "abcaed"

freq = {}
for letter in s:
    if freq.get(letter, 0) > 0:
        print(letter)
        break
    freq[letter] = freq.get(letter, 0) + 1


# else

seen = set()
for ch in s:
    if ch in seen:
        print(ch)
        break
    seen.add(ch)
else:
    print(None)
