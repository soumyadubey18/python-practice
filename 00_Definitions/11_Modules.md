# Modules
A module is a Python `.py` file containing reusable code.

Think: **module = toolbox; function = tool inside it.**

```python
# calculator.py
def add(a, b):
    return a + b
```

```python
import calculator
print(calculator.add(10, 20))
```

Other forms: `import math as m`, `from math import sqrt`.

**Mock:** What is a module? Why use modules? What is an alias?
