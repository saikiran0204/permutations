from sys import setrecursionlimit

setrecursionlimit(10 ** 4)


def permutations(data, length):
    global stack
    if length == len(data):
        stack.append(list(data))
        return
    for i in range(length, len(data)):
        data[length], data[i] = data[i], data[length]
        permutations(data, length + 1)
        data[length], data[i] = data[i], data[length]


stack = []
data = [str(i) for i in input("Enter your data:")]
permutations(data, 0)
print(stack, data)
