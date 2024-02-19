from typing import Union

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


class PythonModule(ElementInterface):
    """Ignition python script, python 2.7 -- Jython 2.7"""
    def __init__(self, name:str, script_path:str) -> None:
        self._name = name
        self._script_path = script_path
    
    def forge(self):
        ...

    def resume(self):
        ...
