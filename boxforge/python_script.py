from boxforge.metadata import Metadata
from boxforge.util import ElementInterface


class PythonScript(ElementInterface):
    """Ignition python script, python 2.7 -- Jython 2.7"""
    def __init__(self, name:str, script_path:str, metadata: Metadata = {}) -> None:
        self._name = name
        self._script_path = script_path
        self._metadata = Metadata(metadata)
    
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
