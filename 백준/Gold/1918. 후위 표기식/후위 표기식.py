from collections import deque
infix = list(input())

postfix = ''
stack = []
priority ={'(':0, '-':1, '+':1,'*':2,'/':2, ')':3}
op = set(['+', '-', '*', '/', '(', ')'])
for i in range(len(infix)):
    token = infix[i]
    if token in op:

        if token =='(':
            stack.append(token)
        elif token ==')':
            while True:
                tmp = stack.pop()
                if tmp=='(':
                    break
                postfix += tmp
        else:
            if not stack:
                stack.append(token)
            else:
                while True:
                    if not stack:
                        stack.append(token)
                        break
                    if priority[stack[-1]] >= priority[token]:
                        postfix += stack.pop()
                    else:
                        stack.append(token)
                        break

    else:
        postfix += token

postfix = postfix + ''.join(stack[::-1])
print(postfix)
