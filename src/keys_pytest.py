import pytest
import sys
import importlib

@pytest.fixture
def keys_pytest():
    if "keys_pytest" in sys.modules:
        importlib.reload(sys.modules["keys_pytest"])
    else:
        importlib.import_module("keys_pytest")

class KeysPytest:
    def __init__(self):
        self.message = "Check Pytest!"

    def __str__(self):
        return self.message

    def __eq__(self, other):
        return self.message == other
    
    def get_info(self):
        return f"KeysPytest: {self.message}"
    
##multiplexer:

def mux(e1, e2, e3, a0, a1, a2):
    outputs = ["H"] * 8

    # Enable kontrolü
    if e1 == 0 and e2 == 0 and e3 == 1:
        index = (a2 << 2) | (a1 << 1) | a0
        outputs[index] = "L"

    return outputs