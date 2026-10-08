# Day 6 — Pandas Fundamentals Quick Reference

## DataFrames and Series

A **DataFrame** is a table. Each column is a **Series**. The left-hand column of row labels is the **index**; Pandas adds 0, 1, 2... automatically.

```python
import pandas as pd

df = pd.DataFrame({
    "patient": ["Ana", "Ben", "Cy"],
    "age": [54, 61, 47],
})
print(df)
```

```
  patient  age
0     Ana   54
1     Ben   61
2      Cy   47
```

---

## Selecting a Column

```python
df["age"]
```

```
0    54
1    61
2    47
Name: age, dtype: int64
```

A single column is a Series: it keeps its index, its `Name:`, and a `dtype:` line.

Operations apply to the whole column, with no loop needed:

```python
df["age"] * 2     # 108, 122, 94 — still a Series, still "Name: age, dtype: int64"
```

---

## Boolean Masks (Filtering Rows)

```python
mask = df["age"] > 50        # Series of True/False
df[mask]                     # keeps only the True rows
df[df["age"] < 55]           # mask written inline
```

- Whole rows are kept.
- **Original index labels are kept** (so gaps can appear, e.g. labels 0 and 2).

---

## `.loc` vs `.iloc` (the key distinction)

| | Selects by | Row argument | Column argument |
|---|---|---|---|
| `.loc[row, col]` | **labels / names** | index label | column **name** |
| `.iloc[row, col]` | **positions** (count from 0) | row position | column position |

```python
filtered = df[df["age"] < 55]
```

```
              col position →   0         1
 row    row label                patient   age
 pos ↓     ↓
  0        0                     Ana       54
  1        2                     Cy        47
```

```python
filtered.loc[2, "patient"]   # Cy   (label 2, column name)
filtered.iloc[1, 0]          # Cy   (row position 1, column position 0)
filtered.iloc[0, 1]          # 54
```

Errors to recognize:

```python
filtered.loc[1, "age"]       # KeyError   — no row labeled 1
filtered.iloc[2, 0]          # IndexError — only 2 rows (positions 0, 1)
filtered.iloc[1, 2]          # IndexError — only 2 columns (positions 0, 1)
```

**The trap:** after filtering, labels and positions no longer match. Label 2 can be position 1.

**Rule:** `.loc` = names for rows AND columns. `.iloc` = counting numbers for rows AND columns.

---

## Creating and Replacing Columns

Assign to a new name to add a column; assign to an existing name to replace it.

```python
df["age_next_year"] = df["age"] + 1      # new numeric column
df["over_50"] = df["age"] > 50           # new True/False column
df["age"] = df["age"] - 10               # replaces existing column
```

---

## Output-Format Reminders

- Booleans print as **`True` / `False`** (capitalized), never `true` / `false`.
- Plain `print("x")` shows no quotes; strings inside containers (`['x']`, `{'a': 'x'}`) show quotes.
- A Series result ends with `Name: <column>, dtype: <type>` (`int64`, `bool`, ...).
- Grading convention: content only (headers, index, values, capitalization). Column spacing and alignment are decided by Pandas at run time and are not graded.

---

## Practical Pattern: Build, Derive, Filter, Look Up

```python
df = pd.DataFrame({
    "patient": ["Ana", "Ben", "Cy", "Dee"],
    "systolic": [128, 152, 141, 119],
})
df["systolic_minus_120"] = df["systolic"] - 120   # derive a column
print(df[df["systolic"] > 140])                   # filter rows (Ben, Cy; labels 1, 2)
print(df.loc[3, "systolic"])                      # label-based lookup -> 119
```

---

## Key Takeaways

1. A DataFrame is a table of Series; column selection returns a Series.
2. Column arithmetic and comparisons are vectorized, as in NumPy.
3. Boolean masks filter rows and keep their original index labels.
4. `.loc` uses names/labels; `.iloc` uses positions. Check which one the task asks for.
5. After filtering, label and position diverge. Verify which you mean.
6. New columns come from assigning to a new name.

---

## Day 6 Mastery Assessment Results

**5/5 correct:**
- Q1: column arithmetic Series output (`Name: hr, dtype: int64`)
- Q2: filtered DataFrame keeps labels 1 and 2
- Q3: `sub.loc[2, "patient"]` → `Cy`
- Q4: `sub.iloc[0, 0]` → `Ben`
- Q5: boolean column Series (`Name: high, dtype: bool`)

**Next:** Day 7 — Grouping & Aggregation (`groupby()`, `agg()`, `transform()`, `apply()`).
