n = int(input())
lst = []

for i in range(n):
    lst.append(input())


def perblockcheck(current_block):
    stack = []
    for char in current_block:
        if char in ["(", "["]:
            stack.append(char)
        else:

            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    if stack:
        return False
    return True


for i in range(len(lst)):
    if perblockcheck(lst[i]):
        print("YES")
    else:
        print("NO")
