nums = [10, 20, 30]
for i in nums:
    if i == 20:
        break
else:
    print("done")
print(i)

words = ["cat", "elephant", "dog", "hippo"]
result = [w.upper() if len(w) > 3 else w for w in words]
print(result)

fruits = ["apple", "banana", "cherry"]
for i, f in enumerate(fruits, start=1):
    print(i, f)


names = ["Sam", "Ali", "Jon"]
scores = [85, 90, 78, 100]
for n, s in zip(names, scores):
    print(n, s)

squares = [n**2 for n in range(5) if n % 2 == 0]
print(squares)

result = []
for n in range(5):
    if n % 2 == 0:
        result.append(n**2)

# Return index position temp over 100.0
temps = [98.6, 101.2, 99.1, 103.5, 97.9]
for i, t in enumerate(temps):
    if t > 100.0:
        print(i)
temps = [98.6, 101.2, 99.1, 103.5, 97.9]
result = [i for i, t in enumerate(temps) if t > 100.0]
print(result)


i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("loop finished")

count = 3
while count > 0:
    print(count)
    count -= 1
    if count == 1:
        break
else:
    print("loop finished")
print("after loop")


wait_times = [15, 42, 8, 30, 5, 60, 22]
while wait_times.pop(0) <= 50:
    print(wait_times.values())
    if wait_times > 50:
        break

wait_times = [15, 42, 8, 30, 5, 60, 22]

while wait_times:
    wait_time = wait_times.pop(0)

    if wait_time > 50:
        break

    print(wait_time)

wait_times = [15, 42, 8, 30, 5, 60, 22]
new_times = [t for t in wait_times if t < 30]
print(new_times)

wait_times = [15, 42, 8, 30, 5, 60, 22]
new_times = [t if t < 30 else 'LONG WAIT' for t in wait_times]
print(new_times)


words = ["cat", "elephant", "dog", "hippo"]
result = [w.upper() if len(w) > 3 else w for w in words]
print(result)

codes = ["A01", "B12", "A01", "C03", "B12", "A01"]
new_codes = {c for c in codes if c[0] == "A" or c[0] == "B"}
print(new_codes)

d = {"a": 1, "b": 2, "c": 3}
result = {k: v*10 for k, v in d.items() if v % 2 == 0}
print(result)


items = ["x", "y", "z"]
counter = 0
while counter < len(items):
    print(items[counter])
    counter += 1

values = [4, 15, 8, 23, 6, 42]
new_values = {v for v in values if v > 5 and v < 30}
print(new_values)


a = [1, 2]
b = ["x", "y", "z"]
for num, letter in zip(a, b):
    print(num, letter)
