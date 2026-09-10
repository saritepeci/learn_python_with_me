"""
Control Flow
============
Run this file directly to see all output:
    python examples/basics/control_flow.py
"""


# ── IF / ELIF / ELSE ──────────────────────────────────────────────────────────

x = 42
if x > 100:
    label = "big"
elif x > 10:
    label = "medium"
else:
    label = "small"

# Ternary (inline if-else)
sign = "positive" if x > 0 else "non-positive"


# ── FOR LOOPS ─────────────────────────────────────────────────────────────────

# range(start, stop, step) — stop is exclusive
_range_basic = list(range(5))         # [0, 1, 2, 3, 4]
_range_step  = list(range(1, 10, 2))  # [1, 3, 5, 7, 9]

# enumerate gives (index, value) pairs; start= shifts the counter
colors = ["red", "green", "blue"]
_indexed = [(i, c) for i, c in enumerate(colors, start=1)]
# [(1, 'red'), (2, 'green'), (3, 'blue')]

# zip pairs two iterables — stops at the shorter one
names  = ["Alice", "Bob", "Carol"]
scores = [95, 87, 72]
_paired = list(zip(names, scores))
# [('Alice', 95), ('Bob', 87), ('Carol', 72)]

# Loop else: the else block runs only when the loop exits WITHOUT hitting break.
# Used here as a classic primality check.
def find_primes(limit: int) -> list[int]:
    primes = []
    for n in range(2, limit):
        for divisor in range(2, n):
            if n % divisor == 0:
                break
        else:
            primes.append(n)  # only appended when inner loop never broke
    return primes


# ── WHILE LOOPS ───────────────────────────────────────────────────────────────

def count_up(limit: int) -> list[int]:
    """Demonstrates while with break and continue."""
    result = []
    i = 0
    while True:
        if i >= limit:
            break        # exits the loop entirely
        if i % 2 == 0:
            i += 1
            continue     # skips to the next iteration (even numbers skipped)
        result.append(i)
        i += 1
    return result
# count_up(10) → [1, 3, 5, 7, 9]


# ── MATCH / CASE (Python 3.10+) ───────────────────────────────────────────────
# Structural pattern matching — richer than a switch statement.
# Patterns are matched top-down; the first match wins.

def describe_point(point: tuple) -> str:
    match point:
        case (0, 0):
            return "origin"
        case (x, 0):
            return f"on x-axis at {x}"
        case (0, y):
            return f"on y-axis at {y}"
        case (x, y):
            return f"at ({x}, {y})"
        case _:
            return "not a valid point"


def http_status(code: int) -> str:
    match code:
        case 200 | 201 | 204:
            return "success"
        case 400:
            return "bad request"
        case 401 | 403:
            return "auth error"
        case 404:
            return "not found"
        case 500:
            return "server error"
        case _:
            return "unknown"


# ── EXPORTED FUNCTIONS (used by tests) ────────────────────────────────────────

def fizzbuzz(n: int) -> str:
    """Classic FizzBuzz — returns 'Fizz', 'Buzz', 'FizzBuzz', or str(n)."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def describe_number(n: int) -> str:
    """Classifies a number using match/case."""
    match n:
        case 0:
            return "zero"
        case n if n > 0:
            return "positive"
        case _:
            return "negative"


# ── DEMO ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print([fizzbuzz(i) for i in range(1, 16)])
    print(find_primes(20))
    print(count_up(10))

    for p in [(0, 0), (3, 0), (0, 4), (3, 4)]:
        print(describe_point(p))

    for code in [200, 404, 500, 418]:
        print(f"HTTP {code}: {http_status(code)}")
