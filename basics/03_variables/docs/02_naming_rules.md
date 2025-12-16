# Naming Rules and Best Practices

In Python, variable names must follow specific syntax rules and common style conventions.
These rules define which names are allowed and which forms are invalid.
Following established naming practices helps prevent errors and makes code easier to read and maintain.


---

## Valid variable names

Variable names (identifiers) may contain letters, digits and underscores. They must not start with a digit and they are case-sensitive.

```python
# valid examples
name = "Alice"
age2 = 30
_private_value = None  # leading underscore is allowed
long_name_123 = 1

print(name, age2, _private_value, long_name_123)
```

Unicode letters are permitted as well (use with care):

```python
π = 3.14159
print(π)
```

---

## Invalid variable names

Some identifiers are invalid because they break Python's syntax rules or collide with reserved keywords. Invalid examples are commented out so the examples remain executable.

```python
# invalid: cannot start with a digit
# 1st_value = 10  # SyntaxError

# invalid: hyphens are not allowed in identifiers
# my-value = 5  # SyntaxError

# invalid: reserved keywords cannot be used as variable names
# for = 3  # SyntaxError

# corrected forms
first_value = 10
my_value = 5
for_loop = 3  # append or change the name to avoid keyword collision

print(first_value, my_value, for_loop)

import keyword
print("for is keyword?", keyword.iskeyword("for"))
```

---

## Best practices for readable and maintainable names

- Use descriptive names that convey purpose (prefer nouns for variables).
- Keep names concise but clear; avoid unnecessary abbreviations.
- Use short names like `i`, `j` for simple loop counters or indexes only.
- Be consistent in naming style across the codebase.

```python
# poor: unclear
x = 0

# better: descriptive and clear
total_items = 0

# acceptable for short loops
for i in range(3):
    print(i)

users_list = ["alice", "bob"]
print(total_items, users_list)
```

---

## Syntax rules vs style conventions

- Syntax rules are enforced by the interpreter (for example, identifiers cannot start with a digit and keywords cannot be used as names).
- Style conventions are recommendations that improve readability; a common convention for variable names in Python is snake_case (lowercase words separated by underscores).

```python
# syntax rule violation (commented out):
# 2value = 5  # would raise SyntaxError

# style recommendation (snake_case):
user_id = 42
print(user_id)
```

---

## Example file
- [`02_naming_rules.py`](../examples/02_naming_rules.py)
