# Hafersack

Hafersack is a really small library to store and retrieve metadata in any object.
Hafersack can store anything and uses strings as keys.

## Installation

```shell
$ pip install hafersack  # or use your preferred package manager
```

## How to use

Creating a singleton Hafersack instance is recommended, but not required.
As long as you use the same key, you can access the same metadata from different Hafersack instances.

```python
from hafersack import Hafersack

sack = Hafersack()

class MyClass:
    pass

obj = MyClass()

sack.set(obj, "key1", "value1")
sack.set(obj, "key2", 42)

assert sack.has(obj, "key1")
assert sack.has(obj, "key2")
assert not sack.has(obj, "key3")

assert sack.get(obj, "key1") == "value1"
assert sack.get(obj, "key2") == 42

sack.delete(obj, "key1")
assert not sack.has(obj, "key1")
assert sack.has(obj, "key2")
```
