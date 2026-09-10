"""
Functions
=========
Run this file directly to see all output:
    python examples/basics/functions.py
"""
from collections.abc import Callable
from typing import Any


# ── BASIC DEFINITION ──────────────────────────────────────────────────────────

def add(a: int, b: int = 0) -> int:
    """Add two integers. b defaults to 0."""
    return a + b


def greet(name: str, greeting: str = "Hello") -> str:
    """Format a greeting string."""
    return f"{greeting}, {name}!"


# ── *ARGS AND **KWARGS ────────────────────────────────────────────────────────

def total(*numbers: float) -> float:
    """*args collects extra positional arguments into a tuple."""
    return sum(numbers)


def display(**options: Any) -> None:
    """**kwargs collects extra keyword arguments into a dict."""
    for key, value in options.items():
        print(f"  {key}={value!r}")


def mixed(required: int, *args: int, flag: bool = False, **kwargs: Any) -> dict:
    """Shows all parameter kinds in one signature."""
    return {"required": required, "args": args, "flag": flag, "kwargs": kwargs}


# ── POSITIONAL-ONLY (/) AND KEYWORD-ONLY (*) ─────────────────────────────────
# Parameters before / must be passed positionally — the name is not part of the API.
# Parameters after * must be passed as keyword arguments.

def strict_params(pos_only: int, /, normal: int, *, kw_only: int) -> int:
    return pos_only + normal + kw_only

# strict_params(1, 2, kw_only=3)    → 6   (correct)
# strict_params(pos_only=1, ...)    → TypeError (pos_only is positional-only)
# strict_params(1, 2, 3)            → TypeError (kw_only must be named)


# ── MULTIPLE RETURN VALUES ────────────────────────────────────────────────────
# Python returns a tuple; caller unpacks with a, b = func()

def min_max(numbers: list[float]) -> tuple[float, float]:
    """Returns (minimum, maximum) of the list."""
    return min(numbers), max(numbers)


# ── LAMBDA ───────────────────────────────────────────────────────────────────
# Anonymous single-expression functions — best for short callbacks.

# normal function for square
# def square(x):
#     return x ** 2

square    = lambda x: x ** 2
double    = lambda x: x * 2

_sorted_desc = sorted([3, 1, 4, 1, 5], key=lambda x: -x)   # [5, 4, 3, 1, 1]
_sorted_str  = sorted(["banana", "apple", "cherry"], key=len) # by length


# ── CLOSURES ──────────────────────────────────────────────────────────────────
# A closure is a function that captures variables from its enclosing scope.

def make_adder(n: int) -> Callable[[int], int]:
    """Returns a new function that always adds n to its argument."""
    def adder(x: int) -> int:
        return x + n     # 'n' is captured from make_adder's scope
    return adder

# Each call to make_adder produces an independent function with its own 'n'.
add5 = make_adder(5)
add3 = make_adder(3)
# add5(10) == 15,  add3(10) == 13


# ── RECURSION ─────────────────────────────────────────────────────────────────

def factorial(n: int) -> int:
    """Recursive factorial. Python's default call stack limit is ~1000."""
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    return 1 if n <= 1 else n * factorial(n - 1)


# ── DEMO ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(add(2, 3))
    print(greet("World"))
    print(greet("Alice", "Hi"))
    print(total(1, 2, 3, 4, 5))
    display(color="red", size=42, active=True)
    print(mixed(1, 2, 3, flag=True, x=99))
    print(min_max([3, 1, 4, 1, 5, 9]))
    print([factorial(n) for n in range(8)])
    print(add5(10), add3(10))
