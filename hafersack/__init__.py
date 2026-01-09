from typing import Any, ClassVar


class Hafersack:
    _ROOT_KEY: ClassVar[str] = "__hafersack__"

    def __init__(self, key: str) -> None:
        self._key = key

    @classmethod
    def _has_root_container(cls, obj: object) -> bool:
        return hasattr(obj, cls._ROOT_KEY)

    @classmethod
    def _init_root_container(cls, obj: object) -> None:
        setattr(obj, cls._ROOT_KEY, {})

    @classmethod
    def _get_root_container(cls, obj: object) -> dict[str, dict[str, Any]]:
        return getattr(obj, cls._ROOT_KEY)

    def _has_container(self, obj: object) -> bool:
        return self._has_root_container(obj) and self._key in self._get_root_container(obj)

    def _init_container(self, obj: object) -> None:
        if not self._has_root_container(obj):
            self._init_root_container(obj)
        root = self._get_root_container(obj)
        root[self._key] = {}

    def _get_container(self, obj: object) -> dict[str, Any]:
        return self._get_root_container(obj)[self._key]

    def has(self, obj: object, key: str) -> bool:
        return self._has_container(obj) and key in self._get_root_container(obj)[self._key]

    def get(self, obj: object, key: str) -> Any:
        if not self.has(obj, key):
            raise KeyError(f"Object {obj} has no metadata '{key}' in container '{self._key}'.")
        return self._get_root_container(obj)[self._key][key]

    def set(self, obj: object, key: str, value: Any) -> None:
        if not self._has_container(obj):
            self._init_container(obj)
        self._get_container(obj)[key] = value

    def delete(self, obj: object, key: str) -> None:
        if not self._has_container(obj):
            self._init_container(obj)
        container = self._get_container(obj)
        if self.has(obj, key):
            del container[key]
        if len(container) == 0:
            root = self._get_root_container(obj)
            del root[self._key]
            if len(root) == 0:
                delattr(obj, self._ROOT_KEY)
