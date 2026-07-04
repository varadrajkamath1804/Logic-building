# Questions:
#
# Count frequency
# First non-repeating character
# Reverse words
# Compress string
# Check anagram
# Longest substring

s = "abcabc"

# Frequency
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

# First non-repeating character
for val in s:
    if freq[val] == 1:
        print(val)
        break

else:
    print("None")
