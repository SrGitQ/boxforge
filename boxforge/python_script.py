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
            "metadata": metadata,
        }

        self._validators = {
            "script_path": self._script_path_validation,
            "name": self._name_validation,
            "metadata": self._metadata_validation
        }

        for key in self._data:
            self._data[key] = self._validate(key=key, value=self._data[key], data=self._data)
    
    def forge(self):
        ...

    def resume(self):
        ...
    
    def _script_path_validation(self, path: str) -> str:
        assert os.path.isfile(path), f"{path} is not a valid path for a file"
        assert path.endswith(".py"), f"{path} is not a python script"

        return path
    
    @property
    def script_path(self) -> str:
        return self["script_path"]
    
    @script_path.setter
    def script_path(self, path:str) -> None:
        self._data["script_path"] = self._validate(key="script_path", value=path, data=self)


class PythonModule(ElementInterface):
    """Ignition python script, python 2.7 -- Jython 2.7"""
    def __init__(self, name:str, script_path:str) -> None:
        self._name = name
        self._script_path = script_path
    
    def forge(self):
        ...

    def resume(self):
        ...
