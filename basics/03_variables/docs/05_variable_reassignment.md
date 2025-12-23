# Variable Reassignment

A variable can be reassigned to reference a different value at any time.
Reassignment changes which object the variable name refers to.

---

## Reassigning a variable

A variable can be given a new value after its initial assignment.

```python
x = 10
print(x)

x = 20
print(x)
```

The previous value is no longer referenced by the variable.

---

## Reassignment with expressions

Reassignment can use the variable’s current value.

```python
count = 3
count = count + 1

print(count)
```

This pattern is common in calculations and updates.

---

## Example file

* [`05_variable_reassignment.py`](../examples/05_variable_reassignment.py)
