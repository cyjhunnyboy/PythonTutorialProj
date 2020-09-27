"""
队列：先进先出

"""
import collections

# 创建一个队列
queue = collections.deque()
print(queue)

# 进队
queue.append("A")
print(queue)
queue.append("B")
print(queue)
queue.append("C")
print(queue)
print("==============")


# 出队
res = queue.popleft()
print("res = ", res)
print(queue)
res = queue.popleft()
print("res = ", res)
print(queue)
res = queue.popleft()
print("res = ", res)
print(queue)
