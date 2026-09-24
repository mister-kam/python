# Day 5 — NumPy Quick Reference

## What is NumPy?

NumPy provides **arrays** — efficient, vectorized collections of numbers. Arrays let you perform element-wise operations on entire collections without explicit loops, much like vectors/matrices in R.

**Key difference from lists:**
```python
# Lists: operation repeats the list
temps_list = [98.6, 99.1]
temps_list * 2  # [98.6, 99.1, 98.6, 99.1]

# Arrays: operation applies to each element
temps_arr = np.array([98.6, 99.1])
temps_arr * 2  # [197.2, 198.2]
```

---

## Array Creation

```python
import numpy as np

# From a Python list
arr = np.array([10, 20, 30, 40])

# Built-in functions
np.zeros(5)           # [0. 0. 0. 0. 0.]
np.ones(3)            # [1. 1. 1.]
np.arange(0, 10, 2)   # [0 2 4 6 8] — like range()
```

---

## Indexing & Slicing (Same as Lists)

```python
arr = np.array([10, 20, 30, 40, 50])

arr[0]        # 10
arr[-1]       # 50
arr[1:3]      # [20, 30]
arr[::2]      # [10, 30, 50] — every other element

# 2D indexing
data = np.array([[1, 2, 3], [4, 5, 6]])
data[0, 1]    # 2 (row 0, column 1)
data[1, :]    # [4, 5, 6] (row 1, all columns)
data[:, 2]    # [3, 6] (all rows, column 2)
```

---

## Vectorization: Element-wise Operations

Operations apply to every element **without a loop**.

```python
temps = np.array([98.6, 99.1, 98.9])

# Arithmetic
temps - 0.5        # [98.1, 98.6, 98.4]
temps * 2          # [197.2, 198.2, 197.8]
(temps - 32) * 5/9 # Fahrenheit to Celsius

# Comparisons
temps > 99.0       # [False True False]
temps == 98.6      # [True False False]
```

---

## Broadcasting: Operations on Different Shapes

NumPy stretches smaller arrays to match larger ones.

```python
# Scalar to array
arr = np.array([1, 2, 3])
arr - 1  # [0, 1, 2] — broadcasts 1 to [1, 1, 1]

# 1D to 2D
data = np.array([[10, 20], [30, 40], [50, 60]])    # shape (3, 2)
baseline = np.array([5, 10])                        # shape (2,)
data - baseline  # Broadcasts baseline to (3, 2); subtracts each row
# [[5, 10], [25, 30], [45, 50]]
```

---

## Boolean Filtering (Masking)

Create a mask (True/False for each element) and use it to extract matching values.

```python
systolic = np.array([120, 145, 130, 110, 155])

# Single condition
high_bp = systolic > 140
filtered = systolic[high_bp]  # [145, 155]

# Combined conditions (use & for AND, | for OR)
in_range = (systolic > 120) & (systolic < 150)
systolic[in_range]  # [145, 130]
```

**Important:** Comparisons with `NaN` always return `False`, so NaN values are automatically filtered out.

---

## Missing Values: NaN

```python
glucose = np.array([95.0, np.nan, 105.0, 100.0])

# Operations with NaN propagate NaN
np.mean(glucose)      # nan (because of missing data)
np.nanmean(glucose)   # 100.0 (ignores NaN)
np.nanstd(glucose)    # ignores NaN
np.nansum(glucose)    # ignores NaN
```

**NaN in boolean indexing:**
```python
glucose > 100  # [False, False, True, False]
               # NaN > 100 → False (not included)
```

---

## Common NumPy Functions

```python
arr = np.array([10, 20, 30, 40, 50])

# Aggregation
arr.sum()      # 150
arr.mean()     # 30.0
arr.std()      # standard deviation
arr.min()      # 10
arr.max()      # 50

# With NaN
arr_with_nan = np.array([10, np.nan, 30])
np.nanmean(arr_with_nan)   # 20.0
np.nanstd(arr_with_nan)    # ignores NaN
```

---

## Practical Pattern: Filter and Aggregate

This pattern appears constantly in data science:

```python
# Data
vitals = np.array([
    [98.6, 145, 95.0],
    [99.1, 155, 105.0],
    [98.9, 130, 100.0]
])

# 1. Create mask
high_systolic = vitals[:, 1] > 140

# 2. Filter rows
filtered = vitals[high_systolic]

# 3. Aggregate
mean_glucose = np.nanmean(filtered[:, 2])
```

---

## Key Takeaways

1. **Arrays are vectorized** — operations apply to every element without loops.
2. **Indexing extends to 2D** — use `data[row, col]` or `data[:, col_index]` for slicing.
3. **Broadcasting works automatically** — NumPy aligns shapes intelligently.
4. **Boolean filtering is powerful** — combine conditions with `&` (AND) and `|` (OR).
5. **NaN behaves predictably** — comparisons with NaN return False; use `nanmean()`, `nanstd()`, etc. for aggregation.
6. **Think in terms of whole arrays, not loops** — if you're tempted to write a `for` loop, NumPy probably has a vectorized way.

---

## Day 5 Mastery Assessment Results

**5/5 correct:**
- Q1: `np.arange(5, 15, 3)` → `[5 8 11 14]`
- Q2: Boolean filtering for even numbers → `[2 4]`
- Q3: Fahrenheit to Celsius conversion → `[37.0 37.3 37.2 37.5]`
- Q4: 2D row slicing → `[3 4]`
- Q5: Comparison with NaN → `[False False True True True]`

**Next:** Day 6 — Pandas Fundamentals (Series, DataFrames, named columns, filtering by column name).
