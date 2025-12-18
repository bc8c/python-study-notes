# Creating Variables

In Python, a variable is created when you assign a value to a name.
There is no separate declaration step.

The assignment operator is `=`.
It binds a name on the left side to a value on the right side.

```python
x = 10
```

In this example, the name `x` now refers to the value `10`.

To see the value of a variable, you can use the built-in `print()` function.

```python
x = 10
print(x)
```

When this code is executed, the value of `x` is displayed in the console.

---

## Assigning different kinds of values

Variables can refer to different kinds of values, such as numbers or text.

```python
age = 25
name = "Alice"

print(age)
print(name)
```

Here:

* `age` refers to a number
* `name` refers to a string (text enclosed in quotes)

Python automatically determines the type of the value being assigned.

---

## Updating a variable (Reassigning)

A variable can be reassigned to a new value at any time.

```python
count = 1
print(count)

count = 2
print(count)
```

After reassignment, the variable name refers to the new value.

---

## Key points

* A variable is created by assignment
* `=` means “assign”, not “equals”
* `print()` is used to inspect values
* Variables must be assigned before they are used

---

## Example file

The code shown in this section will be collected into the following file:

* [`01_creating_variables.py`](../examples/01_creating_variables.py)
