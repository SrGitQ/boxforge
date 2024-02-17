from boxforge.definitions import FILES, VERSIONS, Scope, IgnitionReference
from typing import Any
import json
import pathlib


class Metadata:
    """Metadata ignition project resource"""

    __slots__ = [
        "_scope",
        "_version",
        "_restricted",
        "_overridable",
        "_files",
        "_attributes",
        "_data",
    ]

    def __init__(self, metadata: dict) -> None:
        self._scope = self._scope_validation(metadata["scope"])
        self._version = self._version_validation(metadata["version"])
        self._restricted = self._restricted_validation(metadata["restricted"])
        self._overridable = self._overridable_validation(metadata["overridable"])
        self._files = self._files_validation(metadata["files"])
        # TODO: attributes must be their own constructor and tests
        self._attributes = self._attributes_validation(metadata["attributes"])

        self._data = {
            "scope": self.scope,
            "version": self.version,
            "restricted": self.restricted,
            "overridable": self.overridable,
            "files": self.files,
            "attributes": self.attributes,
        }

    def forge(self, path: str) -> None:
        current_path = pathlib.Path(path)
        current_path.mkdir(parents=True, exist_ok=True)

        metadata_path = str(current_path)+"/"+IgnitionReference.MetadataFileName
        print(metadata_path)
        with open(metadata_path, "w+") as file:
            file.write(self.dump())

    def dump(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

    def __getitem__(self, key: str) -> Any:
        return self._data[key]
    
    def __setitem__(self, key, value) -> None:
        self.__setattr__(key, value)
        self._data[key] = value

    def __delitem__(self, key) -> None:
        return
    
    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)
    
    def to_dict(self) -> dict:
        return self._data

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

    def _overridable_validation(self, overridable: bool) -> bool:
        assert isinstance(
            overridable, bool
        ), f"{overridable} is not a bool object or value"

        return overridable

    @property
    def overridable(self) -> bool:
        return self._overridable

    @overridable.setter
    def overridable(self, value: bool) -> None:
        self._overridable = self._overridable_validation(value)

    def _files_validation(self, files: list) -> list:
        assert isinstance(files, list), f"{files} is not a list object"

        for file in files:
            assert isinstance(file, str), f"{file} is not a file name (str)"
            assert "." in file, f"{file} has no extension"
            extension = file.split(".")[-1]
            assert extension in FILES, f"{extension} is not a valid extension"

        return files

    @property
    def files(self) -> list:
        return self._files

    @files.setter
    def files(self, value: list) -> None:
        self._files = self._files_validation(value)

    def _attributes_validation(self, attributes: dict) -> dict:
        assert isinstance(attributes, dict), f"{attributes} is not dict object"

        return attributes

    @property
    def attributes(self) -> dict:
        return self._attributes

    @attributes.setter
    def attributes(self, value) -> None:
        self._attributes = self._attributes_validation(value)
