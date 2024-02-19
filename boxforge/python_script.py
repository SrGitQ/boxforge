from typing import Union
import pathlib
import os

from boxforge.metadata import Metadata
from boxforge.util import ElementInterface


class PythonScript(ElementInterface):
    """Ignition python script, python 2.7 -- Jython 2.7"""
    def __init__(self, path:str = "", name: Union[str, None] = "", metadata: Union[dict, None] = {}, code: str = "") -> None:
        self._data = {
            "path": path,
            "name": name,
            "metadata": Metadata(metadata),
            "code": code,
            "resource": "",
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
    
    def forge(self, path: str, parent: bool = False) -> None:
        def build_parent_child_path(parent: str, child: str) -> str:
            if parent.endswith("/"):
                return parent + child
            else:
                return parent + "/" + child
        
        if parent:
            launch_path = build_parent_child_path(path, self.name)
        else:
            launch_path = path
        
        script_dirpath = pathlib.Path(launch_path)
        script_dirpath.mkdir(parents=True, exist_ok=True)

        self.metadata.forge(str(script_dirpath))

        with open(script_dirpath / "code.py", "w") as file:
            file.write(self.code)

    def resume(self) -> str:
        summary: str = f"""** Ignition Python Script **\n:::name\n{self.name}\n::: code\n{self.code}\n::: resource\n{self.resource}"""
        print(summary)
        return summary
    
    def _path_validation(self, path: str) -> str:
        if path == "":
            print("Warning: no path given")
            return path
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
        if name:
            import re
            name_regex = r"[a-zA-Z0-9\_]"
            if re.match(name_regex, name):
                pass
            else:
                raise Exception(f"{name} is not a valid name")
        elif self.path:
            script_filename = self.path.split("/")[-1]
            name = script_filename.replace(".py", "")
        else:
            print("Warning: no name given")
            pass

        return name

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

    def _code_validation(self, code: str) -> str:
        # TODO: check if file is not binary
        # TOOD: test unicode scripts
        if not code:
            with open(self.path, "r") as file_script:
                return file_script.read()
        else:
            return code
    
    @property
    def code(self) -> str:
        return self["code"]

    @code.setter
    def code(self, code:str) -> None:
        self._data["code"] = self._validate(key="code", value=code, data=self)
    
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
