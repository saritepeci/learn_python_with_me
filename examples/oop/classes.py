"""
Object-Oriented Programming
============================
Run this file directly to see all output:
    python examples/oop/classes.py
"""
from __future__ import annotations   # enables forward references in annotations

import math
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


# ── BASIC CLASS ───────────────────────────────────────────────────────────────

class InsuranceAccount:
    """
    Demonstrates: instance vars, class vars, @property, @classmethod,
    @staticmethod, and the main dunder (magic) methods.
    """

    interest_rate: float = 0.05     # class variable — shared by all instances
    _total_accounts: int = 0        # tracks how many accounts have been created

    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.owner = owner
        self._balance = initial_balance   # _ prefix = 'protected' by convention
        InsuranceAccount._total_accounts += 1

    # ── property: turns a method into a read-only attribute ──────────────────

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    # ── public methods ───────────────────────────────────────────────────────

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError(
                f"Insufficient funds: balance={self._balance:.2f}, "
                f"requested={amount:.2f}"
            )
        self._balance -= amount

    def apply_interest(self) -> float:
        """Mutates balance in-place; returns the interest amount added."""
        interest = self._balance * self.interest_rate
        self._balance += interest
        return interest

    # ── classmethod: receives the class object, not an instance ──────────────

    @classmethod
    def total_accounts(cls) -> int:
        return cls._total_accounts

    # ── staticmethod: no access to class or instance — pure utility ──────────

    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        return isinstance(amount, (int, float)) and amount > 0

    # ── dunder (magic) methods ───────────────────────────────────────────────

    def __repr__(self) -> str:
        # repr should ideally be eval-able to recreate the object
        return f"InsuranceAccount(owner={self.owner!r}, balance={self._balance:.2f})"

    def __str__(self) -> str:
        # str is the human-friendly version
        return f"{self.owner}'s account: ${self._balance:.2f}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, InsuranceAccount):
            return NotImplemented   # lets Python try the other operand's __eq__
        return self.owner == other.owner and self._balance == other._balance


# ── ABSTRACT BASE CLASS + INHERITANCE ─────────────────────────────────────────

class Shape(ABC):
    """Abstract class — cannot be instantiated; subclasses must implement area/perimeter."""

    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:
        return f"{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


# ── DATACLASS ─────────────────────────────────────────────────────────────────
# @dataclass auto-generates __init__, __repr__, and __eq__ from field annotations.

@dataclass
class Point:
    x: float
    y: float

    def distance_to(self, other: Point) -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)


@dataclass
class Student:
    name: str
    grade: int
    # Mutable defaults MUST use field(default_factory=...) — never use [] directly.
    # Using a bare [] as a default would share one list across all instances.
    subjects: list[str] = field(default_factory=list)

    def add_subject(self, subject: str) -> None:
        self.subjects.append(subject)


# ── DEMO ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    acc = InsuranceAccount("Alice", 1000.0)
    acc.deposit(200.0)
    acc.withdraw(50.0)
    print(acc)
    print(repr(acc))
    print(f"Interest: {acc.apply_interest():.2f}")
    print(f"Total accounts created: {InsuranceAccount.total_accounts()}")

    for shape in [Circle(5.0), Rectangle(4.0, 6.0)]:
        print(shape.describe())

    p1 = Point(0.0, 0.0)
    p2 = Point(3.0, 4.0)
    print(f"Distance: {p1.distance_to(p2)}")
    print(f"Sum: {p1 + p2}")

    s = Student("Eve", 10)
    s.add_subject("Math")
    s.add_subject("Science")
    print(s)
