"""
Variables & Data Types
======================
Run this file directly to see all output:
    python examples/basics/variables_and_types.py
"""
import math


# ── ASSIGNMENT ────────────────────────────────────────────────────────────────

x = 10
a, b, c = 1, 2, 3               # tuple unpacking — left-to-right
first, *rest = [10, 20, 30, 40]  # starred: first=10, rest=[20, 30, 40]
a, b = b, a                      # swap without a temporary variable

# Walrus (:=) — assigns and returns the value inside expressions
data = "hello world"
if (length := len(data)) > 5:
    pass  # 'length' is now in scope here too

# Augmented assignment
n = 10
n += 5    # 15
n -= 3    # 12
n *= 2    # 24
n //= 5   # 4   (floor division — result is always int)
n **= 3   # 64  (exponentiation)


# ── NUMERIC TYPES ─────────────────────────────────────────────────────────────

i: int     = 42
f: float   = 3.14
cx: complex = 2 + 3j     # complex number; j is the imaginary unit
b_: bool   = True        # bool is a subclass of int: True==1, False==0

# Underscores in numeric literals are ignored by the parser — pure readability
million = 1_000_000
pi      = 3.141_592_653

# Integer bases
binary  = 0b1010   # 10
octal   = 0o17     # 15
hex_val = 0xFF     # 255

# Division — the only operator that changes the result type
_float_div = 7 / 2    # 3.5  — always float, even when result is whole
_floor_div = 7 // 2   # 3    — always int (floors toward -∞)
_modulo    = 7 % 2    # 1    — remainder
_power     = 2 ** 8   # 256  — exponentiation

# Float comparison — never use == for floats (binary representation error)
assert math.isclose(0.1 + 0.2, 0.3)    # correct: uses relative tolerance
# assert 0.1 + 0.2 == 0.3              # False — 0.30000000000000004


# ── STRINGS ───────────────────────────────────────────────────────────────────

name      = "Alice"
greeting  = f"Hello, {name}!"                    # f-string — preferred since 3.6
aligned   = f"{'left':<10}|{'right':>10}"        # format spec: left/right align
decimal   = f"{3.14159:.2f}"                     # "3.14"
thousands = f"{1_000_000:,}"                     # "1,000,000"
raw_path  = r"C:\Users\name"                     # raw string — backslashes literal
multiline = """line one
line two"""

# Strings are immutable — all methods return a new string
s = "  Hello, World!  "
_stripped  = s.strip()                     # "Hello, World!"
_lower     = s.lower()                     # "  hello, world!  "
_split     = "a,b,c".split(",")            # ['a', 'b', 'c']
_joined    = ",".join(["a", "b", "c"])     # "a,b,c"
_replaced  = s.replace("World", "Python")
_starts    = "hello".startswith("he")      # True
_count     = "hello world".count("l")      # 3

# Slicing: [start : stop : step] — stop is exclusive, negative index = from end
t = "Python"
_first   = t[0]    # 'P'
_last    = t[-1]   # 'n'
_middle  = t[1:4]  # 'yth'
_reverse = t[::-1] # 'nohtyP' — negative step reverses


# ── BOOL AND NONE ─────────────────────────────────────────────────────────────

# Every object has a boolean value. All of these are falsy:
falsy_values = [False, None, 0, 0.0, "", [], {}, set()]
assert all(not v for v in falsy_values)

# None is the null sentinel — always compare with 'is', not '=='
value = None
assert value is None
assert value is not None or True  # shows the pattern


# ── TYPE CHECKING AND CONVERSION ──────────────────────────────────────────────

x = 42
_type_of_x = type(x)                      # <class 'int'>
_is_int    = isinstance(x, int)            # True
_is_num    = isinstance(x, (int, float))   # True — tuple of types accepted

# Explicit conversion
_str_to_int   = int("42")      # 42
_str_to_float = float("3.14")  # 3.14
_int_to_str   = str(100)       # "100"
_int_to_bool  = bool(0)        # False
_tuple_to_list = list((1, 2))  # [1, 2]


# ── CONSTANTS (convention only — Python has no const keyword) ─────────────────

MAX_RETRIES     = 3
DEFAULT_TIMEOUT = 30.0
API_BASE_URL    = "https://api.example.com"


# ── EXPORTED FUNCTION (used by tests) ─────────────────────────────────────────

def demonstrate_types() -> dict:
    """Returns one instance of each core built-in type."""
    return {
        "int":     42,
        "float":   3.14,
        "complex": 1 + 2j,
        "str":     "hello",
        "bool":    True,
        "none":    None,
    }


# ── DEMO ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    for type_name, val in demonstrate_types().items():
        print(f"{type_name:>8}: {val!r:<20}  type={type(val).__name__}")

    print(f"\nSlicing 'Python': {t[1:4]!r}, reversed: {t[::-1]!r}")
    print(f"Division: 7/2={7/2}, 7//2={7//2}, 7%2={7%2}, 2**8={2**8}")
    print(f"f-string: {greeting!r}")
    print(f"Aligned:  {aligned!r}")
