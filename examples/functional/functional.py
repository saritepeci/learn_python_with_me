"""
Functional Programming Patterns
================================
Run this file directly to see all output:
    python examples/functional/functional.py
"""
from collections.abc import Callable, Generator
from functools import lru_cache, partial, reduce
from itertools import islice
from typing import TypeVar

T = TypeVar("T")


# ── COMPREHENSIONS ────────────────────────────────────────────────────────────

# List comprehension — most readable option when you want a list
squares    = [x ** 2 for x in range(10)]
evens      = [x for x in range(20) if x % 2 == 0]
flat       = [x for row in [[1, 2], [3, 4]] for x in row]  # nested loop

# Dict comprehension
freq       = {ch: "hello".count(ch) for ch in set("hello")}

# Set comprehension — unique values only
word_lens  = {len(w) for w in "one two three four".split()}

# Generator expression — uses () instead of []
# Key difference: values are computed one at a time (lazy), no list in memory.
gen_sq = (x ** 2 for x in range(1_000_000))  # holds no values yet
_first_5 = [next(gen_sq) for _ in range(5)]   # computes only 5


# ── GENERATOR FUNCTIONS ───────────────────────────────────────────────────────
# 'yield' suspends execution and hands the value to the caller.
# Execution resumes on the next call to next().

def countdown(start: int) -> Generator[int, None, None]:
    while start >= 0:
        yield start
        start -= 1


def fibonacci() -> Generator[int, None, None]:
    """Infinite sequence — consume with islice or a for-break."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def read_in_chunks(data: bytes, size: int = 4) -> Generator[bytes, None, None]:
    """Streaming reader — avoids loading all data into memory at once."""
    for i in range(0, len(data), size):
        yield data[i:i + size]


# yield from delegates iteration to a sub-generator
def chain_iters(*iterables) -> Generator:
    for it in iterables:
        yield from it


# ── MAP, FILTER, REDUCE ───────────────────────────────────────────────────────
# These return iterators; wrap in list() to materialise.

nums = [1, 2, 3, 4, 5, 6]
doubled  = list(map(lambda x: x * 2, nums))    # [2, 4, 6, 8, 10, 12]
filtered = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4, 6]
product  = reduce(lambda acc, x: acc * x, nums)       # 720

# In modern Python, list/dict comprehensions are usually preferred over map/filter.
# Use map/filter when working with existing callables:
_strs    = list(map(str, nums))    # ['1', '2', '3', ...]


# ── FUNCTOOLS ─────────────────────────────────────────────────────────────────

# partial: pre-fill some arguments of a function
def power(base: float, exp: float) -> float:
    return base ** exp

square = partial(power, exp=2)
cube   = partial(power, exp=3)
# square(5) == 25,  cube(3) == 27

# lru_cache: memoize return values — ideal for pure recursive functions.
# Caches up to maxsize call results; None means unlimited.
@lru_cache(maxsize=None)
def memoized_fib(n: int) -> int:
    """Fibonacci with memoization — O(n) instead of O(2^n)."""
    if n < 2:
        return n
    return memoized_fib(n - 1) + memoized_fib(n - 2)


# sorted with a key function
words     = ["banana", "apple", "cherry", "date"]
by_len    = sorted(words, key=len)
by_last   = sorted(words, key=lambda w: w[-1])


# ── HIGHER-ORDER FUNCTIONS ────────────────────────────────────────────────────

def compose(*funcs: Callable) -> Callable:
    """Apply functions right-to-left: compose(f, g)(x) == f(g(x))."""
    def composed(value):
        for f in reversed(funcs):
            value = f(value)
        return value
    return composed


add1   = lambda x: x + 1
times2 = lambda x: x * 2
add1_then_double = compose(times2, add1)   # (x+1)*2


# ── DEMO ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(list(countdown(5)))
    print(list(islice(fibonacci(), 10)))
    print(f"memoized_fib(35) = {memoized_fib(35)}")
    print(f"product of [1..6] = {product}")
    print(f"compose: add1_then_double(3) = {add1_then_double(3)}")
    print(f"by_len: {by_len}")
    print(list(chain_iters([1, 2], [3, 4], [5])))
    chunks = list(read_in_chunks(b"Hello World", size=4))
    print(chunks)
