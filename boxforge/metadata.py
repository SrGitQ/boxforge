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
    ]

    def __init__(self, metadata):
        self._scope = self._scope_validation(metadata["scope"])
        self._version = self._version_validation(metadata["version"])
        # self._restricted = metadata["restricted"]
        # self._overridable = metadata["overridable"]
        # self._files = metadata["files"]
        # self._attributes = metadata["attributes"]
    
    def _scope_validation(self, scope: str):
        assert isinstance(scope, str), f"Scope is not an string object: {scope}"
        assert len(scope) == 1, f"Scope is larger or shorter than single char: {scope}"
        assert scope.isupper(), f"Scope should be upper: {scope}"
        assert hasattr(Scope, scope), f"Invalid Scope value: {scope}"
        return scope
    
    @property
    def scope(self):
        return self._scope
    
    @scope.setter
    def scope(self, value):
        self._scope = self._scope_validation(value)
    
    def _version_validation(self, version: int):
        assert isinstance(version, int), f"{version} is not integer value"
        assert version in VERSIONS, f"Version number {version} is out of the valid range"

    @property
    def version(self):
        return self.version
    
    @version.setter
    def version(self, value):
        self._version = self._version_validation(value)


    
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
