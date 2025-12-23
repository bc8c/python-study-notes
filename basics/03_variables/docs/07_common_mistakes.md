# Common Beginner Mistakes

Variables are simple in concept but easy to misuse when first learning Python.
Many beginner mistakes come from misunderstanding assignment and naming behavior.

---

## Using an undefined variable

A variable must be assigned before it is used.

```python
x = 10
print(x)
```

Using a name that has not been defined causes an error.

```python
print(y)
```

---

## Confusing assignment with equality

The assignment operator `=` assigns a value to a variable.

```python
x = 5
```

It does not compare values.

```python
x = 5
print(x == 5)
```

---

## Overwriting built-in names

Using built-in names as variables hides their original meaning.

```python
list = 10
print(list)
```

This can cause confusion later in the code.

---

## Example file

* [`07_common_beginner_mistakes.py`](../examples/07_common_beginner_mistakes.py)
