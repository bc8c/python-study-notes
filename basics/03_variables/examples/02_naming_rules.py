import keyword

# --------------------------------------------------------
# Valid variable names
# --------------------------------------------------------
name = "Alice"
age2 = 30
_private_value = None  # leading underscore is allowed
long_name_123 = 1

print(name, age2, _private_value, long_name_123)

# Unicode letters are permitted as well (use with care):
π = 3.14159
print(π)

# --------------------------------------------------------
# Invalid variable names
# --------------------------------------------------------

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


print("for is keyword?", keyword.iskeyword("for"))

# --------------------------------------------------------
# Best practices for readable and maintainable names
# --------------------------------------------------------

# poor: unclear
x = 0

# better: descriptive and clear
total_items = 0

# acceptable for short loops
for i in range(3):
    print(i)

users_list = ["alice", "bob"]
print(total_items, users_list)

# --------------------------------------------------------
# Syntax rules vs style conventions
# --------------------------------------------------------

# syntax rule violation (commented out):
# 2value = 5  # would raise SyntaxError

# style recommendation (snake_case):
user_id = 42
print(user_id)
