# Reassignment = a name is bound to a different object; the original object is not changed.
# Mutation = the existing object is changed; the name remains bound to that object.
# None = absence of a value, not necessarily an unknown value.

name = "Jon"
age = 40

print(name, age)
print(type(age))

x = [5]
y = x

y.append(10)
print(x)
print(y)

#################################################
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a == c)

b.append(4)
print(a)
print(b)
print(c)
#################################################

name = "Jon"
age = 40
scores = [80, 90, 100]
scores_copy = scores
scores.append(95)
print(name)
print(age)
print(scores)
print(scores_copy)
print(scores is scores_copy)

################################################

scores = [80, 90, 100]
scores_copy = scores

scores = scores + [95]

print(scores)
print(scores_copy)
print(scores is scores_copy)
