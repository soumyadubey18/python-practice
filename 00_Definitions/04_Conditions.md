# Conditions
Conditions let a program make decisions.

```python
cpu = 90
if cpu >= 90:
    print("Critical")
elif cpu >= 70:
    print("Warning")
else:
    print("Normal")
```

Mental model: **IF this is true -> do this; ELIF -> check another; ELSE -> otherwise.**

**Mock:** Why indentation? When is `else` executed?
