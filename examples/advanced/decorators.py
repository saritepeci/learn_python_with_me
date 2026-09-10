"""
Decorators
==========
A decorator is a callable that takes a function and returns a (usually) enhanced version.

Run this file directly to see all output:
    python examples/advanced/decorators.py
"""
import functools
import time
from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


# ── BASIC DECORATOR ───────────────────────────────────────────────────────────

def uppercase_result(func: F) -> F:
    """Wraps return value in .upper() — for functions that return str."""
    @functools.wraps(func)   # copies __name__, __doc__, __module__ from func
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper  # type: ignore[return-value]


@uppercase_result
def say_hello(name: str) -> str:
    return f"hello, {name}"

# say_hello("world")     → "HELLO, WORLD"
# say_hello.__name__     → "say_hello"  (not "wrapper", thanks to functools.wraps)


# ── DECORATOR FACTORY (decorator that takes arguments) ───────────────────────
# Add a wrapper layer: the outer function receives config and returns the decorator.

def repeat(times: int) -> Callable[[F], F]:
    """Calls the decorated function 'times' times; returns the last result."""
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper  # type: ignore[return-value]
    return decorator


@repeat(3)
def knock() -> str:
    print("knock")
    return "knock"


# ── TIMER ─────────────────────────────────────────────────────────────────────

def timer(func: F) -> F:
    """Logs wall-clock time for each call."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start   = time.perf_counter()
        result  = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.6f}s")
        return result
    return wrapper  # type: ignore[return-value]


# ── RETRY ─────────────────────────────────────────────────────────────────────

def retry(
    max_attempts: int = 3,
    exceptions: tuple[type[Exception], ...] = (Exception,),
) -> Callable[[F], F]:
    """Re-calls the function on failure, up to max_attempts total attempts."""
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc: Exception | None = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    last_exc = exc
                    print(f"Attempt {attempt}/{max_attempts} failed: {exc}")
            raise last_exc  # type: ignore[misc]
        return wrapper  # type: ignore[return-value]
    return decorator


# ── STACKING DECORATORS ───────────────────────────────────────────────────────
# Decorators are applied bottom-up: @timer runs first, then @repeat wraps it.

@repeat(2)
@timer
def slow_op(label: str = "work") -> str:
    """timer wraps slow_op; then repeat wraps the timed version."""
    time.sleep(0.01)
    return label


# ── CLASS-BASED DECORATOR ─────────────────────────────────────────────────────

class memoize:
    """Caches results keyed by positional args — class-based decorator."""

    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)  # makes instance look like func
        self._func  = func
        self._cache: dict = {}

    def __call__(self, *args):
        if args not in self._cache:
            self._cache[args] = self._func(*args)
        return self._cache[args]

    def cache_info(self) -> dict:
        return {"size": len(self._cache), "keys": list(self._cache.keys())}


@memoize
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)


# ── DEMO ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(say_hello("world"))
    knock()
    slow_op("task")
    print(f"fib(30) = {fib(30)}")
    print(f"cache: {fib.cache_info()}")
