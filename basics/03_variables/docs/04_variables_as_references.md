# Variables as References

A variable does not store a value itself. Instead, it acts as a name that refers to an object in memory.

In Python, assignment does not copy values.
It binds a name to an existing object.

---

## Basic reference assignment

When an assignment is executed, Python first evaluates the right-hand side and produces an object.
The variable name on the left-hand side is then bound to that object.

Here, x does not contain the number 10.
It is simply a name that refers to the object representing 10.

```python
x = 10
print(x)
```
This assignment does not create a new object.
Instead, y becomes another reference to the same object that x refers to.

```python
y = x
print(y)
```

---

## Multiple references to the same value

Multiple variable names can refer to the same object at the same time.

At this point, both a and b refer to the same object.
No copying occurs during the assignment b = a.

```python
a = 5
b = a

print(a)
print(b)
```

Reassigning a does not change the original object.
It simply rebinds the name a to a different object, while b continues to refer to the original one.

```python
a = 7
print(a)
print(b)
```

---

## Looking Ahead

This reference-based behavior will become more significant in later examples involving reassignment and shared objects.

---
## Example file

* [`04_variables_as_references.py`](../examples/04_variables_as_references.py)
