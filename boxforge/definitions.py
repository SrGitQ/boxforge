class Scope:
    A = "All"
    C = "Client"
    G = "Gateway"


class Ignition:
    metadata_file_name = "resource.json"
    versions = [1, 2, 3]
    scope = Scope
    files = {"py": ".py", "sql": ".sql", "png": ".png", "json": ".json", "bin": ".bin"}
