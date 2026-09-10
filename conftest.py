"""
conftest.py is auto-loaded by pytest before any test run.
Fixtures defined here are available to every test file without an explicit import.
"""
import pytest


@pytest.fixture
def sample_text() -> str:
    """Reusable sentence used by string and collection tests."""
    return "the quick brown fox jumps over the lazy dog"


@pytest.fixture
def bank_account():
    """A BankAccount with 100.0 balance, shared across OOP tests."""
    from examples.oop.classes import BankAccount
    return BankAccount("Alice", 100.0)
