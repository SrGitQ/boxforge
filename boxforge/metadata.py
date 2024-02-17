# TODO: refactor this
class Scope:
    A = "All"
    C = "Client"
    G = "Gateway"


VERSIONS = [1, 2, 3]


class Metadata:
    """Metadata ignition project resource"""

    __slots__ = [
        "_scope",
        "_version",
        "_restricted",
    ]

    def __init__(self, metadata: dict) -> None:
        self._scope = self._scope_validation(metadata["scope"])
        self._version = self._version_validation(metadata["version"])
        self._restricted = self._restricted_validation(metadata["restricted"])
        # self._overridable = metadata["overridable"]
        # self._files = metadata["files"]
        # self._attributes = metadata["attributes"]

    def _scope_validation(self, scope: str) -> str:
        assert isinstance(scope, str), f"Scope is not an string object: {scope}"
        assert len(scope) == 1, f"Scope is larger or shorter than single char: {scope}"
        assert scope.isupper(), f"Scope should be upper: {scope}"
        assert hasattr(Scope, scope), f"Invalid Scope value: {scope}"

        return scope

    @property
    def scope(self) -> str:
        return self._scope

    @scope.setter
    def scope(self, value: str) -> None:
        self._scope = self._scope_validation(value)

    def _version_validation(self, version: int) -> int:
        assert isinstance(version, int), f"{version} is not integer value"
        assert (
            version in VERSIONS
        ), f"Version number {version} is out of the valid range"

        return version

    @property
    def version(self) -> int:
        return self._version

    @version.setter
    def version(self, value: int) -> None:
        self._version = self._version_validation(value)

    def _restricted_validation(self, restricted: bool) -> bool:
        assert isinstance(
            restricted, bool
        ), f"{restricted} is not a bool object or value"

        return restricted

    @property
    def restricted(self) -> bool:
        return self._restricted

    @restricted.setter
    def restricted(self, value: bool) -> None:
        self._restricted = self._restricted_validation(value)


# TODO: delete this
"""
{
    "scope": "A",
    "version": 1,
    "restricted": False,
    "overridable": True,
    "files": ["code.py"],
    "attributes": {},
}
"""
