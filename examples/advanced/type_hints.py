"""
Type Hints  (PEP 484 / 526 / 604 / 673)
=========================================
Type hints are checked by mypy / pyright at development time — not enforced at runtime.

Run this file directly to see all output:
    python examples/advanced/type_hints.py
"""
from __future__ import annotations  # makes all annotations lazy strings; required for forward refs

from collections.abc import Callable, Sequence
from typing import (
    Any,
    ClassVar,
    Final,
    Literal,
    Optional,
    Protocol,
    TypedDict,
    TypeVar,
    overload,
    TYPE_CHECKING,
)

# TYPE_CHECKING is False at runtime but True for type checkers.
# Use it to avoid circular imports that only exist for annotations.
if TYPE_CHECKING:
    pass  # e.g.: from some_module import HeavyType


# ── BASIC HINTS ───────────────────────────────────────────────────────────────

def add(a: int, b: int) -> int:
    return a + b

# Python 3.9+: use lowercase built-in names directly — no need to import List, Dict…
def first(items: list[int]) -> int | None:   # | is Union since Python 3.10
    return items[0] if items else None

def map_keys(d: dict[str, int], offset: int) -> dict[str, int]:
    return {k: v + offset for k, v in d.items()}


# ── OPTIONAL AND UNION ────────────────────────────────────────────────────────

# Optional[T] is exactly T | None — the | syntax is preferred in new code.
def find(items: list[str], target: str) -> int | None:
    try:
        return items.index(target)
    except ValueError:
        return None

# Union with unrelated types
def stringify(value: int | float | str) -> str:
    return str(value)


# ── TYPEVAR ───────────────────────────────────────────────────────────────────
# TypeVar lets a function stay generic: the return type mirrors the input type.

T = TypeVar("T")

def identity(x: T) -> T:
    """Returns x; the type checker knows the output type matches the input."""
    return x

def first_item(seq: Sequence[T]) -> T:
    return seq[0]


# ── TYPEDDICT ─────────────────────────────────────────────────────────────────
# Gives structure to dicts. Type checker validates key names and value types.

class Movie(TypedDict):
    title: str
    year: int
    rating: float

def display_movie(m: Movie) -> str:
    return f"{m['title']} ({m['year']}) — {m['rating']:.1f}"

the_matrix: Movie = {"title": "The Matrix", "year": 1999, "rating": 8.7}


# ── PROTOCOL ──────────────────────────────────────────────────────────────────
# Structural subtyping — "duck typing" with compile-time checks.
# Any class that implements the required methods satisfies the Protocol,
# even without inheriting from it.

class Drawable(Protocol):
    def draw(self) -> None: ...
    def area(self) -> float: ...

class Canvas:
    def render(self, shape: Drawable) -> None:
        print(f"Drawing shape with area {shape.area():.2f}")
        shape.draw()


# ── LITERAL ───────────────────────────────────────────────────────────────────
# Restricts a parameter to a fixed set of values.

Direction = Literal["north", "south", "east", "west"]

def move(direction: Direction, steps: int) -> str:
    return f"Moving {direction} by {steps} steps"


# ── FINAL AND CLASSVAR ────────────────────────────────────────────────────────

class Config:
    MAX_RETRIES: ClassVar[int]  = 3                           # class-level, no instance copy
    BASE_URL:    Final[str]     = "https://api.example.com"   # cannot be reassigned


# ── CALLABLE ──────────────────────────────────────────────────────────────────

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

_doubled = apply(lambda x: x * 2, 5)   # 10


# ── OVERLOAD ──────────────────────────────────────────────────────────────────
# Declare multiple signatures; only the last (implementation) body actually runs.

@overload
def process(x: int) -> int: ...
@overload
def process(x: str) -> str: ...

def process(x: int | str) -> int | str:
    if isinstance(x, int):
        return x * 2
    return x.upper()


# ── DEMO ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(display_movie(the_matrix))
    print(move("north", 3))
    print(process(10))
    print(process("hello"))
    print(find(["a", "b", "c"], "b"))
    print(first_item([10, 20, 30]))
