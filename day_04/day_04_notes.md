# Day 4 — Functions

## Function Definition & Return

```python
def function_name(arg1, arg2):
    """Optional docstring."""
    # body
    return result
```

- Arguments are names for inputs.
- `return` sends a value back to the caller.
- If no `return`, the function returns `None`.
- The function body is indented.

## Local vs. Global Scope

**Local scope:** Variables defined inside a function exist only inside that function.

```python
def my_func():
    local_var = 10  # Only exists inside my_func
    return local_var

print(local_var)  # NameError — doesn't exist here
```

**Global scope:** Variables defined at the module level (outside functions) are accessible everywhere, *except* if you try to assign to them inside a function without the `global` keyword.

```python
count = 0  # Global

def increment():
    global count  # Tell Python to modify the global count
    count = count + 1
    return count
```

**Key rule:** If a name is assigned *anywhere* in a function, Python treats it as local for the *entire* function — even before the assignment. This causes `UnboundLocalError` if you try to read it before assigning. Use `global` to override this.

## Default Arguments

Provide default values for parameters:

```python
def categorize_bmi(bmi_value, threshold_obese=30):
    if bmi_value > threshold_obese:
        return "obese"
    # ...

print(categorize_bmi(31))        # Uses default threshold (30)
print(categorize_bmi(28, 27))    # Overrides threshold (27)
```

- Defaults come *after* required arguments.
- If you supply a value, it overrides the default.

## `*args` — Variable Positional Arguments

Collect extra positional arguments as a tuple:

```python
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1, 2))           # args = (1, 2)
print(add_numbers(1, 2, 3, 4, 5))  # args = (1, 2, 3, 4, 5)
```

`args` is always a tuple, no matter how many arguments are passed.

## `**kwargs` — Variable Keyword Arguments

Collect extra keyword arguments as a dictionary:

```python
def summarize_vitals(pt_name, **kwargs):
    pieces = []
    for key, value in kwargs.items():
        pieces.append(f"{key}={value}")
    return f"{pt_name}: {', '.join(pieces)}"

result = summarize_vitals(pt_name="Alice", temp=98.6, hr=72)
print(result)  # Alice: temp=98.6, hr=72
```

`kwargs` is always a dict, where keys are the argument names.

## Lambdas

Anonymous one-line functions:

```python
square = lambda x: x ** 2
print(square(5))  # 25
```

Lambdas are useful with `map()`, `filter()`, and `sorted()`:

```python
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]
```

**Constraint:** Lambdas can only contain a single expression — no loops, no multiple statements.

## `sorted()` with `key=`

Use `key=` parameter to specify how to sort:

```python
patients = [("Alice", 22.8), ("Bob", 31.2), ("Casey", 18.5)]
result = sorted(patients, key=lambda p: p[1])
print(result[0][0])
```

**Walkthrough:**

```
patients
   ↓
[("Alice", 22.8), ("Bob", 31.2), ("Casey", 18.5)]
                    │
                    │ sorted by p[1] (second element, the BMI)
                    ↓
result
   ↓
[("Casey", 18.5), ("Alice", 22.8), ("Bob", 31.2)]
   │
   │ [0] — first tuple
   ↓
("Casey", 18.5)
   │
   │ [0] — first element of that tuple
   ↓
"Casey"
```

`sorted()` applies the lambda to each item, extracts the sort key, and orders by that key.

## Calling Functions from Within Functions

Once a function is defined, you can call it from inside another function:

```python
def calculate_bmi(height_cm, weight_kg):
    bmi = weight_kg / (height_cm / 100) ** 2
    return bmi

def analyze_patient(name, height_cm, weight_kg):
    bmi_value = calculate_bmi(height_cm, weight_kg)  # Call the function
    return f"{name}: BMI={bmi_value}"

print(analyze_patient("Alice", 175, 70))
```

The inner function call works just like any other — pass arguments, capture the return value, use it.

## `.join()` — Combining Strings

Combine a list of strings with a separator:

```python
pieces = ["temp=98.6", "hr=72", "bp=120"]
result = ", ".join(pieces)
print(result)  # temp=98.6, hr=72, bp=120
```

Useful when building formatted output from a list of pieces.

---

## Key Takeaways

1. Functions encapsulate logic and return values.
2. Local scope is automatic inside functions; use `global` to modify globals.
3. Defaults let you make parameters optional.
4. `*args` and `**kwargs` handle flexible argument counts.
5. Lambdas are small, nameless functions — useful with `filter()`, `map()`, `sorted()`.
6. Functions can call other functions — this is composition.
7. Always predict output before running code.
