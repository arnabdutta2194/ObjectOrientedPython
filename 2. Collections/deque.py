from collections import deque

dequeTest = deque(["Jan","Feb","Mar"])
# print(type(dequeTest)

dequeTest.append("Apr")
print(dequeTest)

dequeTest.appendleft("Dec")
print(dequeTest)

dequeTest.reverse()
print(dequeTest)

dequeTest.pop()
print(dequeTest)

dequeTest.popleft()
print(dequeTest)

print(dequeTest.index("Jan"))

print(dequeTest[2])