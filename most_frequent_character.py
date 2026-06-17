s = "programming"

freq = {}
max_count = 0
for letter in s:
    freq[letter] = freq.get(letter, 0) + 1
    if freq[letter] > max_count:
        mlet, max_count = letter, freq[letter]

print(f"letter={mlet} with frequency={freq[mlet]}")
