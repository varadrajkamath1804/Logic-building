nums = [10, 20, 30, 40]

# Read a list
print(nums[1])

# Update the list by index
nums[2] = 99
print(nums)

# Append the element at the end of the list
nums.append(50)
print(nums)

# Remove last element from a list
nums.pop()
print(nums)

# insert element at the front of the list
nums.insert(0, 1)
print(nums)

# Replace element in the list
nums[0] = 2
print(nums)

# Search the value in the list
if 990 in nums:
    print(True)
else:
    print(False)

# Slice the elements in the list
print(nums[0:4])

# Sort the elements in the list (changes happens to nums)
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

# nums is not chnaged - New sorted list will be created
result = sorted(nums)
print(result)

# extend the elements
nums.extend([110, 120])
print(nums)

# appends as one  elements
nums.append([110, 120])
print(nums)


# nums.extend(130)  causes error - should extend using array - not single element

# Reverses the element
nums.reverse()
print(nums)

# Index gives the position of the element in array
print(nums.index(20))

# Tells how much time the given element is present in the array
print(nums.count(20))

# length of nums
print(len(nums))

# Delete first element
del nums[0]
print(nums)

# Sum of nums - only possible if all numbers present
print(sum(nums))

# Minimum of nums
print(min(nums))


# Maximum of nums
print(max(nums))


# To create new list
numbers = 1, 2, 3, 4, 5, 6
print(list(numbers))

# To create new reversed list
print(list(reversed(numbers)))

# Index-value pairs
print(list(enumerate(nums)))

nums.clear()
print(nums)
