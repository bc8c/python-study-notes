# Data Types (Overview)

A variable is a name that refers to a value.
Every value in Python has a data type, which defines what kind of value it is and how it behaves when used in code.

---

## Integers

An integer represents a whole number without a decimal point.

```python
count = 10
year = 2025

print(count)
print(year)
```

Integers are commonly used in arithmetic expressions.

```python
a = 7
b = 3

result = a - b
print(result)
```

---

## Floating-point numbers

A floating-point number represents a number with a decimal point.

```python
price = 19.99
temperature = -3.5

print(price)
print(temperature)
```

Division between numbers may produce a floating-point result.

```python
x = 10
y = 4

print(x / y)
```

---

## Strings

A string represents a sequence of characters used to store text.

```python
name = "Alice"
message = "Hello, Python"

print(name)
print(message)
```

Strings can be combined using the `+` operator.

```python
first = "Hello"
second = "World"

combined = first + " " + second
print(combined)
```

---

## Booleans

A boolean represents a truth value.

```python
is_active = True
is_admin = False

print(is_active)
print(is_admin)
```

Comparison expressions evaluate to boolean values.

```python
x = 5
y = 10

print(x < y)
```

---

## Checking a value’s type

The `type()` function returns the data type of a value.

```python
value = 42
print(type(value))

value = 3.14
print(type(value))

value = "text"
print(type(value))
```

---

## Example file

* [`03_data_types_overview.py`](../examples/03_data_types_overview.py)
