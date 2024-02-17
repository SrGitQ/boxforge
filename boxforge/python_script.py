from boxforge.metadata import Metadata


# TODO: implement a interface class for Ignition elements
class PythonScript:
    """Ignition python script, python 2.7 -- Jython 2.7"""
    def __init__(self, name:str, script_path:str, metadata: Metadata) -> None:
        self._name = name
        self._script_path = script_path
        self._metadata = Metadata(metadata)
    
    def forge(self):
        ...

    def resume(self):
        ...


class PythonModule:
    """Ignition python script, python 2.7 -- Jython 2.7"""
    def __init__(self, name:str, script_path:str) -> None:
        self._name = name
        self._script_path = script_path
    
    def forge(self):
        ...

    def resume(self):
        ...
