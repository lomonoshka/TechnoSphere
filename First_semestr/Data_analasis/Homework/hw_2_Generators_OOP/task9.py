import copy


class FragileDict:

    def __init__(self, data=dict()):
        self._data = copy.deepcopy(data)
        self._lock = True

    def __getitem__(self, key):
        return copy.deepcopy(self._data[key]) if self._lock else self._data[key]

    def __setitem__(self, key, item):
        if self._lock:
            raise RuntimeError("Protected state")
        self._data[key] = item

    def __contains__(self, key):
        return key in self._data

    def __enter__(self):
        self.__initial_data = copy.deepcopy(self._data)
        self._lock = False
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self._data = self.__initial_data
            print("Exception has been suppressed.")
        if self._data == self.__initial_data:
            self._data = self.__initial_data
        else:
            self._data = copy.deepcopy(self._data)
        delattr(self, "_FragileDict__initial_data")
        self._lock = True
        return True
