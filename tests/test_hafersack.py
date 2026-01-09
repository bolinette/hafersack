import pytest

from hafersack import Hafersack


class Dummy:
    pass


def test_has_get_set_basic() -> None:
    h = Hafersack("meta")
    obj = Dummy()

    assert not h.has(obj, "a")
    with pytest.raises(KeyError):
        h.get(obj, "a")

    h.set(obj, "a", 1)

    assert h.has(obj, "a")
    assert h.get(obj, "a") == 1


def test_overwrite_value() -> None:
    h = Hafersack("meta")
    obj = Dummy()

    h.set(obj, "a", "first")
    h.set(obj, "a", "second")

    assert h.get(obj, "a") == "second"


def test_containers_are_isolated_between_keys() -> None:
    h1 = Hafersack("k1")
    h2 = Hafersack("k2")
    obj = Dummy()

    h1.set(obj, "x", "a")
    assert not h2.has(obj, "x")

    h2.set(obj, "x", "b")

    assert h1.get(obj, "x") == "a"
    assert h2.get(obj, "x") == "b"


def test_set_on_non_assignable_object_raises() -> None:
    h = Hafersack("meta")
    with pytest.raises(AttributeError):
        h.set(42, "a", 1)


def test_multiple_objects_independent() -> None:
    h = Hafersack("meta")
    a = Dummy()
    b = Dummy()

    h.set(a, "v", 1)
    assert h.has(a, "v")
    assert not h.has(b, "v")

    h.set(b, "v", 2)
    assert h.get(a, "v") == 1
    assert h.get(b, "v") == 2


def test_delete_key() -> None:
    h = Hafersack("meta")
    obj = Dummy()

    h.set(obj, "a", 1)
    h.set(obj, "b", 2)

    assert h.has(obj, "a")
    assert h.has(obj, "b")

    h.delete(obj, "a")

    assert not h.has(obj, "a")
    assert h.has(obj, "b")

    h.delete(obj, "b")

    assert not h.has(obj, "b")


def test_delete_absent_key() -> None:
    h = Hafersack("meta")
    obj = Dummy()

    h.delete(obj, "b")


def test_add_then_delete_all() -> None:
    h1 = Hafersack("meta1")
    h2 = Hafersack("meta2")

    obj = Dummy()

    h1.set(obj, "a", 1)
    h2.set(obj, "b", 2)

    assert h1.has(obj, "a")
    assert h2.has(obj, "b")

    h1.delete(obj, "a")
    h2.delete(obj, "b")

    assert not h1.has(obj, "a")
    assert not h2.has(obj, "b")
