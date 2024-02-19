from typing import Union
import os

from boxforge.metadata import Metadata
from boxforge.util import ElementInterface


class PythonScript(ElementInterface):
    """Ignition python script, python 2.7 -- Jython 2.7"""
    def __init__(self, path:str, name: Union[str, None] = "", metadata: Union[dict, None] = {}) -> None:
        self._data = {
            "path": path,
            "name": name,
            "metadata": Metadata(metadata),
            "code":"",
            "resource":"",
        }
        self._validators = {
            "path": self._path_validation,
            "name": self._name_validation,
            "metadata": self._metadata_validation,
            "code": self._code_validation,
            "resource": self._resource_validation,
        }

        self.metadata["files"] = ["code.py"]

        for key in self._data:
            self._data[key] = self._validate(key=key, value=self._data[key], data=self._data)
    
    def forge(self):
        ...

    def resume(self) -> str:
        summary: str = f"""** Ignition Python Script **\n:::name\n{self.name}\n::: code\n{self.code}\n::: resource\n{self.resource}"""
        print(summary)
        return summary
    
    def _path_validation(self, path: str) -> str:
        assert isinstance(path, str), f"{path} is not a string or path object"
        assert os.path.isfile(path), f"{path} is not a valid path for a file"
        assert path.endswith(".py"), f"{path} is not a python script"

        return path
    
    @property
    def path(self) -> str:
        return self["path"]
    
    @path.setter
    def path(self, path:str) -> None:
        self._data["path"] = self._validate(key="path", value=path, data=self)
    
    def _name_validation(self, name:str) -> str:
        assert isinstance(name, str), f"{name} is not a string or path object"
        if name == "":
            script_filename = self.path.split("/")[-1]
            name = script_filename.replace(".py", "")

        import re
        name_regex = r"[a-zA-Z0-9\_]"
        if re.match(name_regex, name):
            return name
        else:
            raise TypeError

    @property
    def name(self) -> str:
        return self["name"]
    
    @name.setter
    def name(self, name: str) -> None:
        if name == "":
            script_filename = self.path.split("/")[-1]
            name = script_filename.replace(".py", "")
        self._data["name"] = self._validate(key="name", value=name, data=self)

    def _metadata_validation(self, metadata:dict) -> dict:
        assert metadata["files"] == ["code.py"], f"{metadata} is invalid for python script"
        return Metadata(metadata)
    
    @property
    def metadata(self) -> Metadata:
        return self["metadata"]
    
    @metadata.setter
    def metadata(self, metadata: dict) -> None:
        self._data["metadata"] = self._validate(key="metadata", value=metadata, data=self)

    def _code_validation(self, path: str) -> str:
        # TODO: check if file is not binary
        # TOOD: test unicode scripts
        path = self.path or path
        with open(path, "r") as file_script:
            return file_script.read()
    
    @property
    def code(self) -> str:
        return self["code"]

    @code.setter
    def code(self) -> None:
        self._data["code"] = self._validate(key="code", value=self.path, data=self)
    
    def _resource_validation(self, metadata: dict) -> str:
        return self.metadata.dump()
    
    @property
    def resource(self) -> str:
        return self["resource"]
    
    @resource.setter
    def resource(self, resource: dict) -> None:
        self._data["resource"] = self._validate(key="resource", value=resource, data=self)


class PythonModule(ElementInterface):
    """Ignition python script, python 2.7 -- Jython 2.7"""
    def __init__(self, name:str, script_path:str) -> None:
        self._name = name
        self._script_path = script_path
    
    def forge(self):
        ...

    def resume(self):
        ...

"""

** Ignition Python Script **
:::name
script
::: code
variable = 12

::: resource
{
    "scope": "G",
    "version": 1,
    "restricted": false,
    "overridable": true,
    "files": [
        "code.py"
    ],
    "attributes": {}
}
** Ignition Python Script **
:::name
script 
::: code
variable = 12

::: resource
{
    "scope": "G",
    "version": 1,
    "restricted": false,
    "overridable": true,
    "files": [
        "code.py"
    ],
    "attributes": {}
}
"""
