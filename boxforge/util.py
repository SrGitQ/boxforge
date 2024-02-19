from typing import Any


class ElementInterface:
    """ElementInterface is an IgnitionElement convention for boxforge elements manipulation.
    Elements can be accessed as `dict` or `object`"""

    def __init__(self) -> None:
        # Assign all the input attributes in `self._data` `dict`

        # All the attributes of the element interface cannot be deleted by the end user
        # End user cannot assign other attributes, at least the element allows the interaction
        # Element should declare how their attributes are accessed above this Interface

        # Use property methods to access to class attributes
        # Those attributes that are considered as relevant data to the user
        # Must be declared in `self._data` `dict`
        self._data = {}

        # All the entry data must be validated before assination, avoid should launch an error
        # for each validator you have to declare in `self._validators` `dict`
        self._validators = {}

        # Custom attributes should be declared after `data` and `validators`...

    def forge(self) -> None:
        """Forge must build the Element content"""
        # forge return None, but it can return `bool` for error handling
        print("This class do not have forge method declared")

    def resume(self) -> str:
        """Resume must print a short summary of the current element"""
        # Resume should return a string with the whole summary.
        # It should print the same summary build too
        print("This class do not have resume method declared")

    def _validate(self, key: str, value: Any, data: dict = {}) -> Any:
        if key not in data:
            # TODO: Improve this message
            print(f"WARNING: `{key}: {value}`, unknown property")
            return value
        return self._validators[key](value)

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self._data[key] = self._validate(key=key, value=value, data=self._data)

    def __delitem__(self, key) -> None:
        # Delete an item is not a recommended method, but you can use this if you
        # need extra functionality for `self.__delitem__()`
        return

    def __iter__(self) -> Any:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def __setattr__(self, name: str, value: Any) -> None:
        try:
            if name not in ["_validators", "_data"]:
                if name not in self._data:
                    print(f"WARNING: `{name}: {value}`, unknown property")
            
            object.__setattr__(self, name, value)
        except Exception as e:
            print("check if you are declaring your attribute above `_validators` and `_data`, see boxforge>util>ElementInterface class")
            raise(e)
