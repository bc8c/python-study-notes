# Variables as References

A variable does not store a value itself but holds a reference to an object in memory.
Assigning a value to a variable creates a relationship between the name and the referenced object.

---

## Basic reference assignment

When a value is assigned, the variable points to that value.

```python
x = 10
print(x)
```

The variable name can be reused to refer to the same value.

```python
y = x
print(y)
```

---

## Multiple references to the same value

More than one variable can reference the same object.

```python
a = 5
b = a

print(a)
print(b)
```

Changing one reference to point elsewhere does not affect the other.

```python
a = 7
print(a)
print(b)
```

---

## Example file

* [`04_variables_as_references.py`](../examples/04_variables_as_references.py)
