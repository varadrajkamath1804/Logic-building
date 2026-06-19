s = "([])"

stack = []
for ch in s:
    if ch in "({[":
        stack.append(ch)
    else:
        if len(stack) == 0:
            print(False)
            break

        top = stack.pop()
        print(f"POP {top} -> {stack}")

        if ch == ")" and top != "(":
            print(False)
            break
        if ch == "}" and top != "{":
            print(False)
            break
        if ch == "]" and top != "[":
            print(False)
            break

else:
    if len(stack) == 0:
        print(True)
    else:
        print(False)
