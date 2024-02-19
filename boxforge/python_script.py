from typing import Union
import os

from boxforge.metadata import Metadata
from boxforge.util import ElementInterface


class PythonScript(ElementInterface):
    """Ignition python script, python 2.7 -- Jython 2.7"""
    def __init__(self, script_path:str, name: Union[str, None] = "", metadata: Union[dict, None] = {}) -> None:
        self._data = {
            "script_path": script_path,
            "name": name,
            "metadata": Metadata(metadata),
            "code":"",
            "resource":"" # TODO resource cast
        }

        self._validators = {
            "script_path": self._script_path_validation,
            "name": self._name_validation,
            "metadata": self._metadata_validation
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
    
    def _script_path_validation(self, path: str) -> str:
        assert isinstance(path, str), f"{path} is not a string or path object"
        assert os.path.isfile(path), f"{path} is not a valid path for a file"
        assert path.endswith(".py"), f"{path} is not a python script"

        return path
    
    @property
    def script_path(self) -> str:
        return self["script_path"]
    
    @script_path.setter
    def script_path(self, path:str) -> None:
        self._data["script_path"] = self._validate(key="script_path", value=path, data=self)
    
    def _name_validation(self, name:str) -> str:
        assert isinstance(name, str), f"{name} is not a string or path object"

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
            script_filename = self.script_path.split("/")[-1]
            name = script_filename.replace(".py", " ")
        self._data["name"] = self._validate(key="name", value=name, data=self)

    def _metadata_validation(self, metadata:dict) -> dict:
        assert metadata["files"] == ["code.py"], f"{metadata} is invalid for python script"
        return Metadata(metadata)
    
    @property
    def metadata(self) -> dict:
        return self["metadata"]
    
    @metadata.setter
    def metadata(self, metadata: dict) -> None:
        self._data["metadata"] = self._validate(key="metadata", value=metadata, data=self)

    def _code_validation(self, path) -> str:
        # TODO: check if file is not binary
        # TOOD: test unicode scripts
        with open(path, "r") as file_script:
            return file_script.read()
    
    @property
    def code(self) -> str:
        return self["code"]

    @code.setter
    def code(self) -> None:
        self._data["code"] = self._validate(key="code", value=self.script_path, data=self)



class PythonModule(ElementInterface):
    """Ignition python script, python 2.7 -- Jython 2.7"""
    def __init__(self, name:str, script_path:str) -> None:
        self._name = name
        self._script_path = script_path
    
    def forge(self):
        ...

    def resume(self):
        ...
