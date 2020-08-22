import glob
import importlib
import os

from onkyrimote.backend import Backend

SUPPORTED_DEVICES = set()


class DeviceMeta(type):
    def __new__(cls, *args, **kwargs):
        new_class = super().__new__(cls, *args, **kwargs)
        if new_class.ID:
            SUPPORTED_DEVICES.add(new_class)
        return new_class


class Device(metaclass=DeviceMeta):
    ID = None
    NAME = None

    def __init__(self, backend: Backend):
        self.backend = backend

    @classmethod
    def sender(cls, *args, **kwargs):
        def func(self: cls):
            return self.backend.send_commands(*args, **kwargs)

        return func


for file in glob.glob(os.path.join(os.path.dirname(__file__), "[a-z]*.py")):
    module_name, ext = os.path.splitext(os.path.basename(file))
    importlib.import_module("." + module_name, package=__package__)
SUPPORTED_DEVICES = frozenset(SUPPORTED_DEVICES)
