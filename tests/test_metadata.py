import os
import json

from boxforge import Metadata

import unittest


class TestMetadata(unittest.TestCase):
    def setUp(self) -> None:
        metadata = {
            "scope": "A",
            "version": 1,
            "restricted": False,
            "overridable": True,
            "files": ["code.py"],
            "attributes": {},
        }

        metadata_test = {
            "scope": "A",
            "version": 1,
            "restricted": False,
            "overridable": True,
            "files": ["code.py"],
            "attributes": {},
        }

        self.metadata = Metadata(metadata)
        self.metadata_test = metadata_test

        self.path = "tmp/metadata.json"

    def test_metadata(self):
        self.assertDictEqual(self.metadata, self.metadata_test)

    def test_metadata_json(self):
        self.assertEqual(self.metadata.dump(), json.dumps(self.metadata_test))

    def test_metadata_file(self):
        self.metadata.forge(self.path)

        self.assertTrue(os.path.isfile(self.path))

        with open(self.path, "r") as file:
            data = json.load(file)
            self.assertEqual(data, json.dumps(self.metadata_test))

    def test_metadata_dtype_scope_all(self):
        self.metadata.scope = "A"

    def test_metadata_dtype_scope_client(self):
        self.metadata.scope = "C"

    def test_metadata_dtype_scope_gateway(self):
        self.metadata.scope = "G"

    def test_metadata_dtype_scope_broken(self):
        wrong_values = [
            "a",
            "c",
            "g",
            "Q",
            "W",
            "E",
            "R",
            "T",
            "TAWD",
            "TAWDS",
            1
        ]
        for case in wrong_values:
            try:
                self.metadata.scope = case
                raise ValueError
            except Exception as e:
                if not isinstance(e, AssertionError):
                    raise Exception("This case should be avoided: "+str(e))
                continue

    def test_metadata_dtype_version_valid(self):
        versions = [1, 2, 3]
        for version in versions:
            self.metadata.version = version

    def test_metadata_dtype_version_invalid(self):
        versions = [-1, 0, 4, 5, 6, 7]
        for version in versions:
            try:
                self.metadata.version = version
                raise ValueError
            except Exception as e:
                if not isinstance(e, AssertionError):
                    raise Exception("This case should be avoided")
                continue

    def test_metadata_dtype_restricted(self):
        self.metadata.restricted = True
        self.metadata.restricted = False

        wrong_values = [1, 1.0, "false", "true", [], {}]
        for fault in wrong_values:
            try:
                self.metadata.restricted = fault
                raise ValueError
            except Exception as e:
                if not isinstance(e, AssertionError):
                    raise Exception("This case should be avoided")
                continue

    def test_metadata_dtype_overridable(self):
        self.metadata.overridable = True
        self.metadata.overridable = False

        wrong_values = [1, 1.0, "false", "true", [], {}]
        for fault in wrong_values:
            try:
                self.metadata.overridable = fault
                raise ValueError
            except Exception as e:
                if not isinstance(e, AssertionError):
                    raise Exception("This case should be avoided")
                continue

    def test_metadata_dtype_files_invalid(self):
        wrong_values = [1, 1.0, {}, [1], True, False]

        self.assertIsInstance(self.metadata.files, list)
        for fault in wrong_values:
            try:
                self.metadata.files = fault
                raise ValueError
            except Exception as e:
                if not isinstance(e, AssertionError):
                    raise Exception("This case should be avoided")
                continue

    def test_metadata_dtype_attributes(self):
        # TODO: add data validations for attributes and methods
        # for data manipulation
        attritbutes = {
            "lastModification": {
                "actor":"admin",
                "timestamp": "2024-01-30T12:07:04Z"
            },
            "lastModificationSignature": "c4a1d2e9350072aa27ed65f9bb254bba28d48c1c5365a9fb6130cc8595e934a1"
        }
        self.metadata.attributes = attritbutes
        self.assertDictEqual(self.metadata.attributes, attritbutes)

    def tearDown(self) -> None:
        if os.path.isfile(self.path):
            os.remove(self.path)


class TestAttributes(unittest.TestCase):
    def test_attributes_last_modification(self):
        raise Exception("No tests yet")
