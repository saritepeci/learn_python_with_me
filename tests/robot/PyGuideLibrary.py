"""
Robot Framework keyword library.
Exposes Python Guide classes as Robot Framework keywords.
"""
import sys
import os
import math

# Ensure the project root is on sys.path so 'examples' is importable
# regardless of the working directory when Robot Framework is invoked.
_project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

from examples.oop.classes import BankAccount, Circle, Rectangle


class PyGuideLibrary:
    """Keywords that wrap Python Guide classes for acceptance testing."""

    ROBOT_LIBRARY_SCOPE = "TEST"   # fresh instance for each Robot test case

    # ── BankAccount keywords ──────────────────────────────────────────────────

    def create_bank_account(self, owner: str, initial_balance: float = 0.0) -> BankAccount:
        return BankAccount(owner, float(initial_balance))

    def deposit_to_account(self, account: BankAccount, amount: float) -> float:
        account.deposit(float(amount))
        return account.balance

    def withdraw_from_account(self, account: BankAccount, amount: float) -> float:
        account.withdraw(float(amount))
        return account.balance

    def get_balance(self, account: BankAccount) -> float:
        return account.balance

    # ── Shape keywords ────────────────────────────────────────────────────────

    def circle_area(self, radius: float) -> float:
        return Circle(float(radius)).area()

    def rectangle_area(self, width: float, height: float) -> float:
        return Rectangle(float(width), float(height)).area()

    def values_are_close(
        self,
        a: float,
        b: float,
        tolerance: float = 0.01,
    ) -> bool:
        return math.isclose(float(a), float(b), abs_tol=float(tolerance))
