string = "A man, a plan, a canal: Panama"
string = string.lower()

left = 0
right = len(string) - 1

while left < right:
    print("\n--------------------")
    print(f"left index  = {left}")
    print(f"right index = {right}")
    print(f"left char   = '{string[left]}'")
    print(f"right char  = '{string[right]}'")

    if not string[left].isalnum():
        print(f"Skipping left character '{string[left]}'")
        left += 1
        continue

    if not string[right].isalnum():
        print(f"Skipping right character '{string[right]}'")
        right -= 1
        continue

    print(f"Comparing '{string[left]}' and '{string[right]}'")

    if string[left] != string[right]:
        print("Mismatch found")
        print(False)
        break

    print("Match found")
    left += 1
    right -= 1

    print(f"Move left -> {left}")
    print(f"Move right -> {right}")

else:
    print("\nPointers crossed. Palindrome confirmed.")
    print(True)
