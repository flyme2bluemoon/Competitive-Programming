total = 0
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operations = ['+', '*']

with open("test", "r") as f:
    for line in f:
        stack = []
        skipped_operation = 0
        line = line.strip().replace(" ", "")
        for i in range(len(line)):
            current_item = line[i]
            if current_item in numbers:
                current_item = int(current_item)
            stack.append(current_item)
            if len(stack) >= 3:
                if stack[-3] == '(' and stack[-1] == ')':
                        stack.pop()
                        inner_value = stack.pop()
                        stack.pop()
                        stack.append(inner_value)
            if len(stack) > 1:
                if stack[-2] == '+' and str(type(stack[-3])) == "<class 'int'>" and str(type(stack[-1])) == "<class 'int'>":
                    x = stack.pop()
                    sign = stack.pop()
                    y = stack.pop()
                    stack.append(x + y)
                elif stack[-2] == '*' and str(type(stack[-3])) == "<class 'int'>" and str(type(stack[-1])) == "<class 'int'>":
                    try:
                        if line[i + 1] != "+":
                            x = stack.pop()
                            sign = stack.pop()
                            y = stack.pop()
                            stack.append(x * y)
                        else:
                            skipped_operation += 1
                    except IndexError:
                        x = stack.pop()
                        sign = stack.pop()
                        y = stack.pop()
                        stack.append(x * y)
        print("".join(map(str, stack)))