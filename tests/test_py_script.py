import os
import shutil

from boxforge import PythonScript, PythonModule

import unittest


class TestPythonScript(unittest.TestCase):
    def setUp(self) -> None:
        self.script_path = "tmp/script.py"

    def test_python_script_resume(self):
        resume_test = """** Ignition Python Script **\n:::name\nscript\n::: code\nvariable = 12\n\n::: resource\n{\n    "scope": "G",\n    "version": 1,\n    "restricted": false,\n    "overridable": true,\n    "files": [\n        "code.py"\n    ],\n    "attributes": {}\n}"""

        script = PythonScript(path=self.script_path)
        self.assertEqual(resume_test, script.resume())

    def test_python_script_path(self):
        resume_test = """** Ignition Python Script **\n:::name\nscript\n::: code\nvariable = 12\n\n::: resource\n{\n    "scope": "G",\n    "version": 1,\n    "restricted": false,\n    "overridable": true,\n    "files": [\n        "code.py"\n    ],\n    "attributes": {}\n}"""
        script = PythonScript(path=self.script_path)

        self.assertEqual(resume_test, script.resume())

    def test_python_script_string(self):
        resume_test = """** Ignition Python Script **\n:::name\n\n::: code\nvariable = 14\n::: resource\n{\n    "scope": "G",\n    "version": 1,\n    "restricted": false,\n    "overridable": true,\n    "files": [\n        "code.py"\n    ],\n    "attributes": {}\n}"""

        code = """variable = 14"""
        script = PythonScript(code=code)

        self.assertEqual(resume_test, script.resume())

    def test_python_script_forge_path(self):
        script = PythonScript(path=self.script_path)
        script.forge("tmp/py_script/")

        code_path_validation = "tmp/py_script/code.py"
        resource_path_validation = "tmp/py_script/resource.json"
        code_validation = "variable = 12\n"
        resource_validation = """{\n    "scope": "G",\n    "version": 1,\n    "restricted": false,\n    "overridable": true,\n    "files": [\n        "code.py"\n    ],\n    "attributes": {}\n}"""
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
        script.forge("tmp/script")

        code_path_validation = "tmp/script/code.py"
        resource_path_validation = "tmp/script/resource.json"
        code_validation = "variable = 12\n"
        resource_validation = """{\n    "scope": "G",\n    "version": 1,\n    "restricted": false,\n    "overridable": true,\n    "files": [\n        "code.py"\n    ],\n    "attributes": {}\n}"""
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
                shutil.rmtree(path)


class TestPythonModule(unittest.TestCase):  # TODO
    def setUp(self) -> None:
        self.module_name = "NewModule"
        self.module_parent_path = "tmp/"

    def test_python_module_empty(self):
        python_module = PythonModule(name=self.module_name, scripts=[])

        test_resume = (
            """**Ignition Python Module**\n:::name\nNewModule\n:::content\n[]"""
        )
        self.assertEqual(python_module.resume(), test_resume)

        python_module.forge(path=self.module_parent_path)
        if not os.path.isdir("tmp/NewModule"):
            raise FileNotFoundError

    def test_python_module_path_scripts(self):
        python_module = PythonModule(name=self.module_name, scripts=["script.py", "main.py"])

        test_resume = """**Ignition Python Module**\n:::name\nNewModule\n:::content\n["script", "main"]"""
        self.assertEqual(python_module.resume(), test_resume)

        python_module.forge(path=self.module_parent_path)
        if not os.path.isdir("tmp/NewModule"):
            raise FileNotFoundError

    def test_python_module_PythonScript_objects(self):
        script_1 = PythonScript(path="tmp/main.py")
        script_2 = PythonScript(path="tmp/script.py")
        python_module = PythonModule(name=self.module_name, scripts=[script_1, script_2])

        test_resume = """**Ignition Python Module**\n:::name\nNewModule\n:::content\n["script", "main"]"""
        self.assertEqual(python_module.resume(), test_resume)

        python_module.forge(path=self.module_parent_path)
        self.assertTrue(os.path.isdir("tmp/NewModule"))
        self.assertTrue(os.path.isdir("tmp/NewModule/script"))
        self.assertTrue(os.path.isdir("tmp/NewModule/script/code.py"))
        self.assertTrue(os.path.isdir("tmp/NewModule/script/resource.json"))
        self.assertTrue(os.path.isdir("tmp/NewModule/main"))
        self.assertTrue(os.path.isdir("tmp/NewModule/main/code.py"))
        self.assertTrue(os.path.isdir("tmp/NewModule/main/resource.json"))

    def tearDown(self) -> None:
        path_to_delete = [
            "tmp/NewModule",
        ]
        for path in path_to_delete:
            if os.path.isdir(path):
                shutil.rmtree(path)
