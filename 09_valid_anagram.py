s1 = "listen"
s2 = "silent"

s1 = "".join(sorted(s1))
s2 = "".join(sorted(s2))
print(s1)
print(s2)
if s1 == s2:
    print("true")
else:
    print("False")


freq = {}

for ch in s1:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s2:
    freq[ch] = freq.get(ch, 0) - 1

print(freq)
if all(val == 0 for val in freq.values()):
    print(True)

else:
    print(False)
