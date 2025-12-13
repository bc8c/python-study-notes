# The following line is a comment explaining that the code above prints a message
# Comments are ignored by the Python interpreter and are used to provide
# explanations or notes in the code
# You can write comments on their own line as well
# This is a single-line comment
# Comments can also be used to temporarily disable code
# print("This line is commented out and will not execute")
# End of the comments example
# Comments can be very useful for documenting your code and making it
# easier to understand for others (or yourself in the future)
# This is another comment explaining that comments are important for code clarity
# Always strive to write clear and concise comments
# to enhance the readability of your code.


"""Comments vs Docstrings.

This module demonstrates the difference between single-line comments and
docstrings. It shows examples of when to use ``#`` comments and when to use
triple-quoted docstrings (``\"\"\"...\"\"\"`` or ``'''...'''``).

The module includes:
    - A short description of the differences between comments and docstrings.
    - An example function with a Google-style docstring.
    - An example of an unused triple-quoted string (parsed and discarded).

Notes:
    - Use ``#`` for in-line or temporary notes where the text is only for
      readers and should not be attached to any object.
    - Use docstrings for modules, classes, and functions so that the text is
      accessible via :attr:`__doc__` and tools such as ``help()`` and Sphinx.
    - PEP 257 defines docstring conventions; this module follows the general
      structure but uses Google-style for function docstrings.
"""


def example_function(a, b):
    """Return the sum of ``a`` and ``b``.

    This demonstrates a short Google-style docstring for a simple function.

    Args:
            a (int): First operand.
            b (int): Second operand.

    Returns:
            int: Sum of ``a`` and ``b``.
    """
    return a + b


if __name__ == "__main__":
    # Print the docstring stored in the function's __doc__ attribute
    print("example_function __doc__:\n")
    print(example_function.__doc__)
