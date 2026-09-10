"""
Built-in Collections: list, tuple, dict, set
=============================================
Run this file directly to see all output:
    python examples/data_structures/collections.py
"""
from collections import Counter, defaultdict, namedtuple


# ── LIST ──────────────────────────────────────────────────────────────────────
# Ordered, mutable, allows duplicates.

nums = [3, 1, 4, 1, 5, 9, 2, 6]

# Indexing and slicing — same rules as strings
_first    = nums[0]      # 3
_last     = nums[-1]     # 6
_slice    = nums[2:5]    # [4, 1, 5]
_reversed = nums[::-1]   # new reversed list (does not mutate nums)

# In-place mutation methods
nums.append(7)           # add one element to the end
nums.extend([8, 9])      # add multiple elements
nums.insert(0, 0)        # insert value at index
nums.remove(1)           # removes the first occurrence of value
popped = nums.pop()      # removes and returns the last element
nums.sort()              # in-place ascending sort
nums.sort(reverse=True)  # in-place descending

# Non-mutating operations — return a new object
_sorted_copy   = sorted(nums)
_reversed_copy = list(reversed(nums))
_count         = nums.count(4)     # how many times 4 appears
_index         = nums.index(3)     # index of first occurrence of 3

# List comprehension: [expression for item in iterable if condition]
squares  = [x ** 2 for x in range(10)]
evens    = [x for x in range(20) if x % 2 == 0]
flat     = [x for row in [[1, 2], [3, 4]] for x in row]  # nested loops
# Equivalent to: result=[]; for row in ...: for x in row: result.append(x)


# ── TUPLE ─────────────────────────────────────────────────────────────────────
# Ordered, immutable, allows duplicates. Used for fixed-size heterogeneous data.

point = (3.0, 4.0)
px, py = point           # unpacking

# Single-element tuple requires a trailing comma — (42) is just parentheses
singleton = (42,)

# namedtuple: adds named attribute access while keeping immutability
Color = namedtuple("Color", ["red", "green", "blue"])
white = Color(255, 255, 255)
_r    = white.red        # 255  (attribute access)
_r2   = white[0]         # 255  (index access still works)


# ── DICTIONARY ────────────────────────────────────────────────────────────────
# Ordered (insertion order, Python 3.7+), mutable, keys must be hashable.

person = {"name": "Alice", "age": 30}

# Access
_name   = person["name"]                # KeyError if key missing
_email  = person.get("email", "N/A")    # safe get with a default

# Mutation
person["city"] = "Berlin"
person.update({"age": 31, "country": "DE"})
del person["city"]

# Iteration patterns
_keys    = list(person.keys())
_values  = list(person.values())
_items   = list(person.items())         # list of (key, value) tuples

# Dict comprehension
squared    = {x: x ** 2 for x in range(6)}
evens_only = {k: v for k, v in squared.items() if k % 2 == 0}

# Merge two dicts (Python 3.9+) — right-side values win on collision
defaults = {"color": "red", "size": 10}
custom   = {"size": 20, "weight": 5}
merged   = defaults | custom            # {"color": "red", "size": 20, "weight": 5}

# defaultdict: missing keys are auto-created using the given factory
by_length: defaultdict = defaultdict(list)
for word in ["hi", "hello", "hey", "bye"]:
    by_length[len(word)].append(word)   # no KeyError on first access
# {2: ['hi'], 5: ['hello'], 3: ['hey', 'bye']}

# Counter: counts hashable elements
votes   = Counter(["alice", "bob", "alice", "alice", "bob"])
_top2   = votes.most_common(2)          # [('alice', 3), ('bob', 2)]
_total  = sum(votes.values())           # 5


# ── SET ───────────────────────────────────────────────────────────────────────
# Unordered, mutable, no duplicates. Items must be hashable.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

_union        = a | b    # {1, 2, 3, 4, 5, 6}
_intersection = a & b    # {3, 4}
_difference   = a - b    # {1, 2}
_sym_diff     = a ^ b    # {1, 2, 5, 6}
_member       = 2 in a   # True — O(1) average lookup

# frozenset: immutable set — can be used as a dict key or set member
fs = frozenset([1, 2, 3])


# ── EXPORTED FUNCTIONS (used by tests) ────────────────────────────────────────

def word_frequency(text: str) -> dict[str, int]:
    """Count occurrences of each whitespace-delimited word (case-insensitive)."""
    return dict(Counter(text.lower().split()))


def flatten(nested: list) -> list:
    """Recursively flatten a nested list of arbitrary depth."""
    result: list = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def invert_dict(d: dict) -> dict:
    """Swap keys and values. Assumes values are unique and hashable."""
    return {v: k for k, v in d.items()}


# ── DEMO ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(word_frequency("the cat sat on the mat the cat"))
    print(flatten([[1, 2], [3, [4, 5]], 6]))
    print(invert_dict({"a": 1, "b": 2, "c": 3}))
    print(f"Top votes: {votes.most_common(2)}")
    print(f"Merge: {merged}")
    print(f"Set ops: union={a | b}, diff={a - b}")
