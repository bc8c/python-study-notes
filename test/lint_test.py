import sys, os  # ruff will complain about multiple imports on one line


def add(a, b):
    unused_value = 123  # should trigger F841 (local variable assigned but never used)
    return a + b
