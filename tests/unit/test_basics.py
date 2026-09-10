import pytest

from examples.basics.variables_and_types import demonstrate_types
from examples.basics.control_flow import fizzbuzz, describe_number
from examples.basics.functions import add, greet, factorial, make_adder


class TestVariablesAndTypes:
    def test_all_core_types_present(self):
        result = demonstrate_types()
        assert set(result) == {"int", "float", "complex", "str", "bool", "none"}

    def test_types_are_correct_instances(self):
        result = demonstrate_types()
        assert isinstance(result["int"],     int)
        assert isinstance(result["float"],   float)
        assert isinstance(result["complex"], complex)
        assert isinstance(result["str"],     str)
        assert isinstance(result["bool"],    bool)
        assert result["none"] is None

    def test_bool_is_subclass_of_int(self):
        result = demonstrate_types()
        assert isinstance(result["bool"], int)   # bool IS an int in Python


class TestFizzBuzz:
    @pytest.mark.parametrize("n, expected", [
        (15, "FizzBuzz"),
        (30, "FizzBuzz"),
        ( 3, "Fizz"),
        ( 9, "Fizz"),
        ( 5, "Buzz"),
        (10, "Buzz"),
        ( 7, "7"),
        ( 1, "1"),
    ])
    def test_fizzbuzz_cases(self, n, expected):
        assert fizzbuzz(n) == expected

    def test_describe_zero(self):
        assert describe_number(0) == "zero"

    def test_describe_positive(self):
        assert describe_number(42) == "positive"

    def test_describe_negative(self):
        assert describe_number(-5) == "negative"


class TestFunctions:
    def test_add_two_numbers(self):
        assert add(2, 3) == 5

    def test_add_with_default_b(self):
        assert add(7) == 7

    def test_add_zero(self):
        assert add(0, 0) == 0

    def test_greet_default_greeting(self):
        assert greet("Alice") == "Hello, Alice!"

    def test_greet_custom_greeting(self):
        assert greet("Bob", "Hi") == "Hi, Bob!"

    def test_factorial_zero(self):
        assert factorial(0) == 1

    def test_factorial_one(self):
        assert factorial(1) == 1

    def test_factorial_five(self):
        assert factorial(5) == 120

    def test_factorial_negative_raises(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_make_adder_closure(self):
        add5 = make_adder(5)
        assert add5(0)  == 5
        assert add5(10) == 15

    def test_make_adder_closures_are_independent(self):
        add3 = make_adder(3)
        add7 = make_adder(7)
        assert add3(1) == 4
        assert add7(1) == 8   # each closure captures its own 'n'
