import json
import pathlib

from boxforge.definitions import Ignition
from boxforge.util import ElementInterface

from typing import Any


class Metadata(ElementInterface):
    """Metadata ignition project resource"""

    def __init__(self, metadata: dict = {}) -> None:
        if not metadata:
            deafult_metadata = {
                "scope": "G",
                "version": 1,
                "restricted": False,
                "overridable": True,
                "files": [],
                "attributes": {},
            }

            metadata = deafult_metadata

        self._validators = {
            "scope": self._scope_validation,
            "version": self._version_validation,
            "restricted": self._restricted_validation,
            "overridable": self._overridable_validation,
            "files": self._files_validation,
            "attributes": self._attributes_validation,
        }

        self._data = {
            "scope": metadata["scope"],
            "version": metadata["version"],
            "restricted": metadata["restricted"],
            "overridable": metadata["overridable"],
            "files": metadata["files"],
            "attributes": metadata["attributes"],
        }
        for key in self._data:
            self._data[key] = self._validate(key=key, value=self._data[key], data=self._data)

    def forge(self, path: str) -> None:
        """Build resource.json given the path
        ### params
        path: str

        ### return:
        file output
        """
        current_path = pathlib.Path(path)
        current_path.mkdir(parents=True, exist_ok=True)

        metadata_path = str(current_path) + "/" + Ignition.metadata_file_name
        print(metadata_path)
        with open(metadata_path, "w+") as file:
            file.write(self.dump())

    def dump(self) -> str:
        """Return a JSON string
        ### params


        ### return:
        JSON string
        """
        return json.dumps(self.to_dict(), indent=4)

    def to_dict(self) -> dict:
        """Convert to dict"""
        return self._data

    def _scope_validation(self, scope: str) -> str:
        assert isinstance(scope, str), f"Scope is not an string object: {scope}"
        assert len(scope) == 1, f"Scope is larger or shorter than single char: {scope}"
        assert scope.isupper(), f"Scope should be upper: {scope}"
        assert hasattr(Ignition.scope, scope), f"Invalid Scope value: {scope}"

        return scope

    @property
    def scope(self) -> str:
        return self["scope"]

    @scope.setter
    def scope(self, value: str) -> None:
        self._data["scope"] = self._validate(key="scope", value=value, data=self)

    def _version_validation(self, version: int) -> int:
        assert isinstance(version, int), f"{version} is not integer value"
        assert (
            version in Ignition.versions
        ), f"Version number {version} is out of the valid range"

        return version

    @property
    def version(self) -> int:
        return self["version"]

    @version.setter
    def version(self, value: int) -> None:
        self._data["version"] = self._validate(key="version", value=value, data=self)

    def _restricted_validation(self, restricted: bool) -> bool:
        assert isinstance(
            restricted, bool
        ), f"{restricted} is not a bool object or value"

        return restricted

    @property
    def restricted(self) -> bool:
        return self["restricted"]

    @restricted.setter
    def restricted(self, value: bool) -> None:
        self._data["restricted"] = self._validate(key="restricted", value=value, data=self)

    def _overridable_validation(self, overridable: bool) -> bool:
        assert isinstance(
            overridable, bool
        ), f"{overridable} is not a bool object or value"

        return overridable

    @property
    def overridable(self) -> bool:
        return self["overridable"]

    @overridable.setter
    def overridable(self, value: bool) -> None:
        self._data["overridable"] = self._validate(key="overridable", value=value, data=self)

    def _files_validation(self, files: list) -> list:
        assert isinstance(files, list), f"{files} is not a list object"

        for file in files:
            assert isinstance(file, str), f"{file} is not a file name (str)"
            assert "." in file, f"{file} has no extension"
            extension = file.split(".")[-1]
            assert extension in Ignition.files, f"{extension} is not a valid extension"

        return files

    @property
    def files(self) -> list:
        return self["files"]

    @files.setter
    def files(self, value: list) -> None:
        self._data["files"] = self._validate(key="files", value=value, data=self)

    def _attributes_validation(self, attributes: dict) -> dict:
        # TODO: attributes must be their own constructor and tests
        assert isinstance(attributes, dict), f"{attributes} is not dict object"

        return attributes

    @property
    def attributes(self) -> dict:
        return self["attributes"]

    @attributes.setter
    def attributes(self, value) -> None:
        self._data["attributes"] = self._validate(key="attributes", value=value, data=self)
