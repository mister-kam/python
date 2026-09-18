# Day 3 — Control Flow: Quick Reference

## `for` / `while` with `else`
- `else` on a loop runs only if the loop finishes **without** hitting `break`.
- `break` skips the loop's `else` entirely and jumps to the code right after the loop.

```python
for i in nums:
    if condition:
        break
else:
    print("didn't break")
```

Same rule applies to `while`/`else`.

## List Comprehensions
Shorthand for a `for` loop that builds a list.

```python
[expr for item in iterable if condition]
```
Equivalent to:
```python
result = []
for item in iterable:
    if condition:
        result.append(expr)
```

**Conditional expression form** (value depends on a condition, not a filter):
```python
[expr_if if condition else expr_else for item in iterable]
```
Note the difference: filtering `if` comes *after* `for`; the conditional-expression `if/else` comes *before* `for`.

## Dict Comprehensions
Same idea, built with `{}` and `key: value`:
```python
{k: v for k, v in pairs if condition}
```
`dict.items()` yields `(key, value)` pairs for iteration — needed to unpack both in a loop/comprehension.

## Set Comprehensions
Same idea, built with `{}` but no `:` — just the value:
```python
{expr for item in iterable if condition}
```
Duplicates automatically collapse (it's a set).

## `enumerate()`
Wraps an iterable to yield `(index, value)` pairs. Only use it when you actually need the index — otherwise iterate directly.
```python
for i, val in enumerate(items, start=1):  # start shifts the counter
```

## `zip()`
Pairs up multiple iterables **elementwise**. Stops at the **shortest** one — silently drops leftovers from longer iterables.
```python
for a, b in zip(list1, list2):
```
If you need to keep the leftovers, use `itertools.zip_longest(list1, list2, fillvalue=None)`.

## `and` / `or`
- `and` → `True` only if **both** sides are `True`.
- `or` → `True` if **at least one** side is `True`.
- Common bug: writing `x == a or b` (always truthy) instead of `x == a or x == b`.

## `print()` vs. container display (quoting)
- `print("x")` → `x` (no quotes — printing a string directly shows raw content)
- `print(["x"])` or `print({"x": 1})` → `['x']` / `{'x': 1}` (quotes appear — Python shows the *repr* of items inside containers)
- This is a recurring gotcha — watch for it when predicting output involving dicts/lists of strings.

## `.pop(0)` (introduced ahead of schedule during a queue-processing exercise)
- `.pop()` removes and returns the **last** item of a list.
- `.pop(0)` removes and returns the **first** item — useful for front-of-queue processing in a `while` loop.

---

## Demonstrated Competencies (Day 3)
- `for`/`while` with `break`/`else` interaction — solid, including a self-corrected grading dispute (learner was right, instructor initially mis-graded).
- List comprehensions: filtering and conditional-expression forms — both independently correct.
- Dict comprehensions — correct once `.items()` was properly taught (this was initially introduced without being taught first; corrected under new course rule, see below).
- Set comprehensions — correct after fixing an `or` logic bug (`x == a or b` → `x == a or x == b`); note `or`/`and` were also initially used before being explicitly taught, then properly taught and re-verified.
- `enumerate()` — correct, including recognizing when it's unnecessary overhead.
- `zip()` — correct, including correctly predicting silent truncation on mismatched lengths, and independently asking about `zip_longest()`.
- `.pop(0)` for front-of-queue processing — correct after being taught (also initially introduced without being taught first; corrected under new course rule).

## Areas to Watch (minor, carried forward)
- `print()` vs. container-display quoting — recurring theme since Day 2. Missed on the mastery assessment (Q5). Worth a short deliberate check-in early in Day 4, not a full drill.
- Exact requirement-following (carried forward from Day 1/Day 2) — no new instance this session; thread appears resolved for now.

## Mastery Assessment Results
- Q1 (list comprehension filter): Correct
- Q2 (dict comprehension + `.items()`): Partially correct (right value, incomplete dict-format answer) — not counted against learner, since `.items()` was untaught at time of asking
- Q3 (`while` loop): Correct
- Q4 (set comprehension, `and`): Correct
- Q5 (`zip()` + print-quoting): Incorrect — quoted strings in plain `print()` output

**Result: 3/5 fully correct, 1/5 partial (instructor error), 1/5 incorrect (quoting rule).**

## New Standing Course Rule (established this session)
Claude must never require or introduce Python syntax/concepts not already explicitly taught when setting an exercise or expecting a code answer. Any new syntax must be taught first, with practice reps, before being used in an exercise. (Applied retroactively this session to `.items()`, `and`/`or`, and `.pop()`, each of which was introduced without being taught first and then properly corrected.)
