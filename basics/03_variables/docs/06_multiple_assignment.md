# Multiple Assignment

Python allows assigning values to multiple variables in a single statement.
This feature makes code more concise while remaining explicit.

---

## Assigning multiple variables

Multiple variables can be assigned at once using commas.

```python
a, b = 1, 2

print(a)
print(b)
```

Each variable receives the value in the corresponding position.

---

## Swapping values

Multiple assignment can be used to swap values without a temporary variable.

```python
x = 5
y = 10

x, y = y, x

print(x)
print(y)
```

---

## Example file

* [`06_multiple_assignment.py`](../examples/06_multiple_assignment.py)
