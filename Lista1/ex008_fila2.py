from collections import deque
from os import system
from sys import platform as SO

if SO == "linux" or SO == "linux2":
    system("clear")
elif SO == "win32":
    system("cls")
else:
    print("Erro!!!")

queue = deque([1, 2,  3, 4, 5])
print(queue)
queue.append(6)
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
