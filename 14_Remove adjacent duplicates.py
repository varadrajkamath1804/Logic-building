s = "abbaca"

stack = []
top = ""

for ch in s:
    print("Character", ch)
    print("Stack", stack)

    if ch == top:
        popped_element = stack.pop()
        print("Popped", popped_element)
        print("Stack after pop", stack)
        if len(stack) > 0:
            top = stack[-1]
        else:
            top = ""
        print("Top", top)
        continue
    else:
        stack.append(ch)
        print("Stack after append", stack)
        top = stack[-1]
        print("Top", top)

else:
    print(stack)


s = "abbaca"

stack = []

for ch in s:
    if stack and stack[-1] == ch:
        stack.pop()
    else:
        stack.append(ch)

result = "".join(stack)

print(result)
