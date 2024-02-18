import os
import json

from boxforge import PythonScript, PythonModule

import unittest


class TestPythonScript(unittest.TestCase):
    def setUp(self) -> None:
        self.script_path = "tmp/script.py"

    def test_python_script_resume(self):
        resume_test = """** Ignition Python Script **\n:::name\nscript\n::: code\nvariable = 12\n\n::: resource\n{\n    "scope": "G",\n    "version": 1,\n    "restricted": False,\n    "overridable": True,\n    "files": [],\n    "attributes": {},\n}"""
        print(resume_test)

        script = PythonScript(path=self.script_path)

        self.assertEqual(resume_test, script.resume())

    def test_python_script_path(self):
        resume_test = """** Ignition Python Script **\n:::name\nscript\n::: code\nvariable = 12\n\n::: resource\n{\n    "scope": "G",\n    "version": 1,\n    "restricted": False,\n    "overridable": True,\n    "files": [],\n    "attributes": {},\n}"""
        script = PythonScript(path=self.script_path)

        self.assertEqual(resume_test, script.resume())

    def test_python_script_string(self):
        resume_test = """** Ignition Python Script **\n:::name\nscript\n::: code\nvariable = 14\n\n::: resource\n{\n    "scope": "G",\n    "version": 1,\n    "restricted": False,\n    "overridable": True,\n    "files": [],\n    "attributes": {},\n}"""

        code = """variable = 14"""
        script = PythonScript(code=code)

        self.assertEqual(resume_test, script.resume())
    
    def test_python_script_forge_path(self):
        script = PythonScript(path=self.script_path)
        script.forge("tmp/py_script/")

        code_path_validation = "tmp/py_script/code.py"
        resource_path_validation = "tmp/py_script/resource.json"
        code_validation = "variable = 12\n"
        resource_validation = """{
    "scope": "G",
    "version": 1,
    "restricted": False,
    "overridable": True,
    "files": [
        "code.py"
    ],
    "attributes": {},
}"""
        if os.path.isfile(code_path_validation):
            with open(code_path_validation, "r") as file:
                self.assertEqual(file.read(), code_validation)
        else:
            raise FileNotFoundError
        
        if os.path.isfile(resource_path_validation):
            with open(resource_path_validation, "r") as file:
                self.assertEqual(file.read(), resource_validation)
        else:
            raise FileNotFoundError


    def test_python_script_forge(self):
        script = PythonScript(path=self.script_path)
        script.forge()

        code_path_validation = "tmp/script/code.py"
        resource_path_validation = "tmp/script/resource.json"
        code_validation = "variable = 12\n"
        resource_validation = """{
    "scope": "G",
    "version": 1,
    "restricted": False,
    "overridable": True,
    "files": [
        "code.py"
    ],
    "attributes": {},
}"""
        if os.path.isfile(code_path_validation):
            with open(code_path_validation, "r") as file:
                self.assertEqual(file.read(), code_validation)
        else:
            raise FileNotFoundError
        
        if os.path.isfile(resource_path_validation):
            with open(resource_path_validation, "r") as file:
                self.assertEqual(file.read(), resource_validation)
        else:
            raise FileNotFoundError

    def tearDown(self) -> None:
        path_to_delete = [
            "tmp/script",
            "tmp/py_script",
        ]
        for path in path_to_delete:
            if os.path.isdir(path):
                os.remove(path)


class TestPythonModule(unittest.TestCase):# TODO
    def setUp(self) -> None:
        self.module_path = "temp/NewModule"
        self.module_name = "NewModule"
        self.module_parent_path = "tmp/"

    def test_python_module_empty(self):
        self.python_module = PythonModule(
            name=self.module_name, path=self.module_parent_path, scripts=[]
        )

    def test_python_module_path_scripts(self):
        self.python_module = PythonModule(
            name=self.module_name,
            path=self.module_parent_path,
            scripts=["script.py", "main.py"],
        )

    def test_python_module_PythonScript_objects(self):
        self.python_module = PythonModule(
            name=self.module_name, path=self.module_parent_path, scripts=[]
        )

    def tearDown(self) -> None:
        if os.path.isdir(self.module_path):
            os.remove(self.module_path)
