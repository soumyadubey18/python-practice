# One-Page Python Revision

## Basics
- `=` assignment
- `==` value comparison
- `is` identity comparison
- `type(x)` -> type
- `id(x)` -> identity

## Input
`input()` returns a string.

Use:
`int(input(...))`
for integer input.

## Conditions
```python
if condition:
    ...
elif condition:
    ...
else:
    ...
```

## Loops
```python
for i in range(start, stop):
    ...
```
Stop is excluded.

```python
while condition:
    ...
```

## String
- index: `text[0]`
- slice: `text[1:4]`
- reverse: `text[::-1]`
- `upper`, `lower`, `title`
- `split`, `join`, `strip`
- `find`, `replace`
- `isalpha`, `isdigit`, `isalnum`, `isspace`

## List
- `append`
- `insert`
- `extend`
- `remove`
- `pop`
- `sort`
- `reverse`
- `count`
- `len`

## Set
- unique values
- `add`, `remove`
- union `|`
- intersection `&`
- difference `-`
- symmetric difference `^`

## Dictionary
`key -> value`

Useful:
- `keys()`
- `values()`
- `items()`
- `get()`
- `update()`

## Function
```python
def name(parameters):
    return result
```

Arguments:
- positional
- keyword
- default
- `*args`
- `**kwargs`

## Module
```python
import module
import module as alias
from module import function
```

## AWS connection
Python logic -> Boto3 -> AWS APIs -> automation.
