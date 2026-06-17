nums = [2, 7, 11, 15]
target = 9
seen = set()

for i in nums:
    req = target - i
    if req in seen:
        print(f"value Found({i},{req})")
        break
    else:
        seen.add(i)
else:
    print(None)


nums = [2, 7, 11, 15]
target = 9

seen = {}

for i in nums:
    req = target - i

    if req in seen:
        print(f"Value Found ({req}, {i})")
        break
    seen[i] = True

else:
    print(None)
