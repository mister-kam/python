# Day 1 — Python Mental Model

## Lesson Focus

- Python's object and reference model
- Assignment vs. mutation
- Reassignment
- Mutable vs. immutable objects
- Basic Python types
- `None`
- Object identity with `id()` and `is`
- Value equality with `==`
- Lists, indexing, and slicing
- Basic Python syntax and execution
- Output prediction

---

## 1. Python Variables Are Names Bound to Objects

A Python variable is better understood as a **name bound to an object** rather than a box containing a value.

```python
x = 10
y = x
```

After these statements, both `x` and `y` refer to the same object.

```text
x ──┐
    ├──> 10
y ──┘
```

Assignment does not necessarily create a copy.

### Important

```python
y = x
```

means:

> Bind the name `y` to the same object that `x` currently refers to.

It does **not** mean:

> Make a copy of `x`.

---

## 2. Reassignment vs. Mutation

### Reassignment

**Reassignment = a name is bound to a different object; the original object is not changed.**

Example:

```python
x = 10
y = x

x = 20
```

`x` is now bound to `20`, while `y` remains bound to `10`.

```text
Before:

x ──┐
    ├──> 10
y ──┘


After x = 20:

x ───> 20

y ───> 10
```

### Mutation

**Mutation = the existing object is changed; the name remains bound to that object.**

Example:

```python
x = [1, 2, 3]
y = x

x.append(4)
```

The list object itself changes.

Both names still refer to that same list:

```text
x ──┐
    ├──> [1, 2, 3, 4]
y ──┘
```

Therefore:

```python
print(x)
# [1, 2, 3, 4]

print(y)
# [1, 2, 3, 4]
```

### Mental Model

> Reassignment changes what a name refers to.

> Mutation changes the object itself.

---

## 3. Mutable vs. Immutable Objects

### Mutable

A mutable object can be changed after it is created.

Examples encountered:

- `list`

Example:

```python
x = [10]
y = x

x.append(20)
```

The existing list is modified.

### Immutable

An immutable object cannot be changed after it is created.

Examples encountered:

- `int`
- `float`
- `str`
- `bool`
- `NoneType`

When an operation appears to "change" an immutable object, Python instead produces/binds to another object.

Example:

```python
x = 10
y = x

x += 1
```

Conceptually:

```text
Initially:

x ──┐
    ├──> 10
y ──┘


After x += 1:

x ───> 11
y ───> 10
```

The integer `10` was not mutated.

---

## 4. `+=` and Mutability

`+=` requires particular attention because its behavior depends on the object's type.

### Immutable example

```python
x = 10
y = x

x += 1
```

The integer cannot be mutated, so `x` becomes bound to `11`.

`y` remains `10`.

### Mutable example

```python
x = [10]
y = x

x += [1]
```

The list is mutable, so the existing list can be modified.

Both names continue to refer to the same list:

```python
x
# [10, 1]

y
# [10, 1]
```

This is an important distinction to understand rather than memorizing individual cases.

---

## 5. Object Identity: `id()` and `is`

Python provides `id()` to identify an object during its lifetime.

Example:

```python
x = [1, 2]
y = x

print(id(x))
print(id(y))
```

The IDs will be the same because `x` and `y` refer to the same object.

### `is`

`is` asks:

> Are these two names referring to the exact same object?

Example:

```python
x = [1, 2]
y = x

x is y
# True
```

### `==`

`==` asks:

> Do these objects have equal values?

Example:

```python
x = [1, 2]
y = [1, 2]

x == y
# True
```

But:

```python
x is y
# False
```

because these are two separately created list objects.

### Key distinction

```text
is  → object identity
==  → value equality
```

Do not use `is` as a general replacement for `==`.

---

## 6. Basic Python Types

Types encountered:

```python
type(42)
# int

type(42.0)
# float

type("42")
# str

type(True)
# bool

type(None)
# NoneType

type([1, 2, 3])
# list
```

Python's Boolean type is named `bool`, not "Boolean".

---

## 7. `None`

`None` represents the absence of a value.

```python
x = None
```

Its type is:

```python
type(x)
# NoneType
```

`None` is not the same as:

- `0`
- `False`
- `""`
- `[]`

A useful initial mental model is:

> `None` means there is no value here.

It does **not** necessarily mean that the value is unknown.

For example, a function may intentionally return `None` to indicate that it has no meaningful value to return.

---

## 8. Lists, Indexing, and Slicing

Python uses **zero-based indexing**.

```python
x = [10, 20, 30, 40]
```

Positions:

```text
index:   0   1   2   3
value:  10  20  30  40
```

Examples:

```python
x[0]
# 10

x[2]
# 30

x[-1]
# 40
```

### Slicing

Python slicing uses:

```python
[start:stop]
```

The `stop` position is **excluded**.

Example:

```python
x[1:3]
```

returns:

```python
[20, 30]
```

The slice starts at index `1` and stops before index `3`.

---

## 9. `len()`

`len()` returns the length/number of elements of an object when the object supports it.

Example:

```python
x = [10, 20, 30]

len(x)
# 3
```

Strings also support `len()`:

```python
name = "Jon"

len(name)
# 3
```

---

## 10. `print()` and `type()`

Two basic tools for inspecting Python objects.

### `print()`

Displays a value:

```python
x = 42
print(x)
```

### `type()`

Reports the object's type:

```python
x = 42
print(type(x))
```

Output:

```text
<class 'int'>
```

---

## 11. Basic Python Syntax

Python uses indentation and punctuation as part of its syntax.

For example:

```python
if age >= 40:
    print("40 or older")
```

The `:` is required after the condition.

An `else` clause is optional.

```python
if age >= 40:
    print("40 or older")
```

is valid Python.

### Important syntax differences from R

R commonly uses:

```r
x <- 10
```

Python uses:

```python
x = 10
```

Python relies heavily on indentation to define code blocks.

```python
if condition:
    do_something()
```

---

## 12. Iteration Terminology

In a loop such as:

```python
for x in values:
    print(x)
```

`x` is the **iteration variable**.

It takes on each value from `values` in sequence.

Python's `for` loop is primarily designed to iterate over an iterable.

---

## 13. Output Prediction

An important part of Python fluency is being able to predict what code will do **before running it**.

For example:

```python
x = [1, 2]
y = x

x.append(3)
```

Before running the code, determine:

1. What object does `x` refer to?
2. What object does `y` refer to?
3. Was the object mutated or was a name reassigned?
4. What will `x` contain?
5. What will `y` contain?
6. Are `x` and `y` still the same object?

This Think → Type → Run → Debug → Review workflow is central to the course.

---

## 14. Key Lessons Learned

### Assignment

```python
y = x
```

does not automatically copy an object.

### Reassignment

```python
x = new_object
```

changes what `x` refers to.

### Mutation

```python
x.append(...)
```

can change the existing object.

### Identity

```python
x is y
```

checks whether two names refer to the same object.

### Equality

```python
x == y
```

checks whether two objects are equal in value.

### Mutability matters

The behavior of an operation can depend on whether the object is mutable or immutable.

---

## 15. Current Day 1 Mastery Notes

### Demonstrated strengths

- Predicting basic Python execution
- Basic types
- List indexing and slicing
- `len()`
- Basic iteration reasoning
- Reassignment vs. mutation after probing
- Object identity vs. value equality
- Understanding shared references to mutable objects
- Reading and executing simple Python code

### Areas still being reinforced

- Writing Python syntax from scratch
- Python punctuation and indentation
- `None` / `NoneType`
- Precise Python terminology
- Immutable-object behavior
- `+=` behavior with mutable vs. immutable objects
- Python execution/reference model
- Translating common R patterns into idiomatic Python

---

## 16. Mental Model to Remember

The most important model from this lesson so far:

> **Names refer to objects.**

Then ask:

1. What object does this name refer to?
2. Is the object mutable or immutable?
3. Did the operation mutate the object?
4. Or did it reassign the name?
5. If there are multiple names, do they refer to the same object?
6. Do I mean identity (`is`) or equality (`==`)?

---

## Next

Continue Day 1 with:

- `None` and Python's execution model
- More R → Python syntax translation
- Independent syntax-writing exercises
- Output-prediction questions
- Day 1 challenge
- Day 1 assessment
- Course progress update
