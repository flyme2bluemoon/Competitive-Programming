total = 0
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operations = ['+', '*']

with open("input", "r") as f:
    for line in f:
        stack = []
        line = line.strip().replace(" ", "")
        for i in line:
            if i in numbers:
                i = int(i)
            stack.append(i)
            if len(stack) >= 3:
                if stack[-3] == '(' and stack[-1] == ')':
                        stack.pop()
                        inner_value = stack.pop()
                        stack.pop()
                        stack.append(inner_value)
            if len(stack) > 1:
                if stack[-2] in operations and str(type(stack[-3])) == "<class 'int'>" and str(type(stack[-1])) == "<class 'int'>":
                    x = stack.pop()
                    sign = stack.pop()
                    y = stack.pop()
                    if sign == "+":
                        stack.append(x + y)
                    elif sign == "*":
                        stack.append(x * y)
        total += stack[0]

print(total)