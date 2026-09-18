# Hafersack

Hafersack is a really small library to store and retrieve metadata in any object.
Hafersack can store anything and uses strings as keys.

Hafersack is used by the [Bolinette project](https://github.com/bolinette) to tag classes and functions with the information its decorators collect.

```python
from hafersack import Hafersack

sack = Hafersack("my_unique_key")


class MyClass:
    pass


obj = MyClass()
sack.set(obj, "role", "admin")

assert sack.has(obj, "role")
assert sack.get(obj, "role") == "admin"
```

## Installation

```shell
$ pip install hafersack  # or use your preferred package manager
```

## Requirements

Hafersack requires Python 3.13 (or newer) and no other dependencies.

## How to use

Creating a singleton Hafersack instance is recommended, but not required.
As long as you use the same key, you can access the same metadata from different Hafersack instances.

Make sure to use distinct keys to avoid collisions with other libraries using Hafersack.
Storing your keys in one place is a good idea to avoid typos and collisions within your own code.

```python
from hafersack import Hafersack

sack = Hafersack("my_unique_key")


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

The metadata is kept in a `__hafersack__` attribute set on the object itself, so Hafersack works on anything that accepts a new attribute, and not on builtins or classes using `__slots__`.
That attribute is removed again once the last key is deleted, which leaves the object as it was found.

## Reference

| Method                 | Behaviour                                                      |
| ---------------------- | -------------------------------------------------------------- |
| `Hafersack(key)`       | Opens a container, shared by every instance using the same key |
| `set(obj, key, value)` | Stores a value, creating the container on first use            |
| `get(obj, key)`        | Reads a value, raises `KeyError` when there is none            |
| `has(obj, key)`        | Tells whether a value is stored, without raising               |
| `delete(obj, key)`     | Removes a value, and the container once it is empty            |

## License

Hafersack is released under the MIT license, see [LICENSE.txt](LICENSE.txt).
