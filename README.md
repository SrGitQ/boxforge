# boxforge
Forge Ignition SCADA components as view, python-script and named-query

**Python Script**
```
>>> from boxforge import PythonScript
>>> script = PythonScript(name="Test", code='print "Hello, world!"')
>>> script.forge("path/to/export")
...
Ignition Python script
```
**Python Module**
```
>>> from boxforge import PythonModule
>>> python_module = PythonModule(
>>>     name="NewModule", scripts=[PythonScript(path="script_1.py"), "script_2.py"]
>>> )
>>> python_module.forge("path/to/export")
...
Ignition Python Module
```

## Changelog
v0.1.7:
- Ignition Python Module
- Python Module forge
- Python Module with multiple scripts
- Python Scripts hotfix parent forge

v0.1.0:
- Ignition Python Script
- Element resume
- Element forge (export)
- You can write your python scripts directly in code
- You can import a script and export as Ignition Python Script
