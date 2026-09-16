# Day 2 — Python Data Structures: Quick Reference

## Lists
```python
nums = [1, 2, 3]
```
- **Mutable**, ordered, allows duplicates.
- Change in place: `nums.append(4)`, `nums[0] = 99`, `nums.remove(2)`.
- Use when: order matters *and* you need to change contents (add/remove/reorder) after creation.

## Tuples
```python
point = (1, 2, 3)
```
- **Immutable**, ordered, allows duplicates.
- `point[0] = 99` → `TypeError` (no item assignment).
- Use when: order matters, but the data shouldn't change after creation (e.g. days of the week, a fixed coordinate, a record you want to guarantee won't be mutated accidentally).

## Sets
```python
ids = {101, 102, 103}
```
- **Mutable**, unordered, **no duplicates** (duplicates are automatically dropped).
- Change with `.add()`, `.remove()`, `.discard()` — no indexing (`ids[0]` is invalid, no order to index into).
- Fast membership checks (`x in ids`) and set operations (union `|`, intersection `&`, difference `-`).
- Use when: uniqueness is the point, and order doesn't matter (e.g. deduplicating patient IDs).

## Dictionaries
```python
record = {"name": "A", "value": 1}
```
- **Mutable**, key-value pairs, keys must be unique, insertion order preserved (Python 3.7+).
- `record["name"] = "B"` reassigns the value for an existing key — allowed because dicts are mutable.
- `record["new_key"] = 2` adds a new key.
- Use when: you need to look values up by a meaningful label rather than a position.

## Nesting
```python
records = {"patient_1": [102, 98, 105]}
records["patient_1"].append(99)
```
- The dict itself doesn't change — its *value* is a mutable list, and `.append()` mutates that list object in place.
- General rule: a container is only as "immutable" as its most permissive nested type. A tuple of lists still has mutable elements inside it, even though the tuple itself can't be reassigned.

## Choosing the Right Structure — Decision Checklist

| Question | If yes → |
|---|---|
| Do I need to look things up by a label instead of position? | **dict** |
| Does uniqueness matter, and order doesn't? | **set** |
| Does order matter, and the data must never change after creation? | **tuple** |
| Does order matter, and I need to add/remove/change items? | **list** |

## Key Gotchas (from this session)
- `()` = tuple, `[]` = list — easy to mix up under time pressure.
- **Tuples allow duplicates.** Only **sets** deduplicate.
- `len()` returns a **count**, not the contents — don't confuse "print the count" with "print the structure."
- Printed dict/set string keys show with single quotes: `{'a': 1}`, not double quotes.
- Sets are mutable (`.add()`/`.remove()` work) — mutability alone doesn't distinguish tuple vs. set; the real distinguishing factors are *duplicates allowed* and *order*.
