"""
栈：先进后出

"""
# 用列表模拟栈结构
stack = []

# 压栈（向栈里存数据）
stack.append("A")
print(stack)
stack.append("B")
print(stack)
stack.append("C")
print(stack)
print("===============")

# 出栈（在栈里取数据）
res = stack.pop()
print("res = ", res)
print(stack)
res = stack.pop()
print("res = ", res)
print(stack)
res = stack.pop()
print("res = ", res)
print(stack)
