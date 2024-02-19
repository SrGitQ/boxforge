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

## Changelog
v0.1.0:
- Ignition Python Script
- Element resume
- Element forge (export)
- You can write your python scripts directly in code
- You can import a script and export as Ignition Python Script
