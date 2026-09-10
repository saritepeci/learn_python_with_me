import math

import pytest

from examples.oop.classes import BankAccount, Circle, Rectangle, Point, Student


class TestBankAccount:
    def test_initial_balance(self, bank_account):
        assert bank_account.balance == 100.0

    def test_deposit_increases_balance(self, bank_account):
        bank_account.deposit(50.0)
        assert bank_account.balance == 150.0

    def test_withdraw_decreases_balance(self, bank_account):
        bank_account.withdraw(40.0)
        assert bank_account.balance == 60.0

    def test_withdraw_all_funds(self, bank_account):
        bank_account.withdraw(100.0)
        assert bank_account.balance == 0.0

    def test_withdraw_insufficient_raises(self, bank_account):
        with pytest.raises(ValueError, match="Insufficient funds"):
            bank_account.withdraw(999.0)

    def test_negative_deposit_raises(self, bank_account):
        with pytest.raises(ValueError):
            bank_account.deposit(-10.0)

    def test_negative_initial_balance_raises(self):
        with pytest.raises(ValueError):
            BankAccount("Bad", -50.0)

    def test_repr_contains_owner_and_balance(self, bank_account):
        r = repr(bank_account)
        assert "Alice" in r
        assert "100" in r

    def test_str_is_human_friendly(self, bank_account):
        s = str(bank_account)
        assert "Alice" in s

    def test_equality(self):
        a = BankAccount("Bob", 200.0)
        b = BankAccount("Bob", 200.0)
        assert a == b

    def test_inequality(self):
        a = BankAccount("Alice", 100.0)
        b = BankAccount("Alice", 200.0)
        assert a != b

    def test_classmethod_tracks_new_account(self):
        before = BankAccount.total_accounts()
        BankAccount("Temp", 0.0)
        assert BankAccount.total_accounts() == before + 1

    def test_staticmethod_validates_amount(self):
        assert BankAccount.is_valid_amount(50.0) is True
        assert BankAccount.is_valid_amount(0.0)  is False
        assert BankAccount.is_valid_amount(-1.0) is False


class TestCircle:
    def test_area(self):
        c = Circle(5.0)
        assert math.isclose(c.area(), math.pi * 25, rel_tol=1e-9)

    def test_perimeter(self):
        c = Circle(3.0)
        assert math.isclose(c.perimeter(), 2 * math.pi * 3, rel_tol=1e-9)

    def test_zero_radius_raises(self):
        with pytest.raises(ValueError):
            Circle(0.0)

    def test_negative_radius_raises(self):
        with pytest.raises(ValueError):
            Circle(-1.0)

    def test_describe_contains_classname(self):
        assert "Circle" in Circle(1.0).describe()


class TestRectangle:
    def test_area(self):
        assert Rectangle(4.0, 5.0).area() == 20.0

    def test_perimeter(self):
        assert Rectangle(4.0, 5.0).perimeter() == 18.0

    def test_square_area(self):
        assert Rectangle(3.0, 3.0).area() == 9.0


class TestPoint:
    def test_creation(self):
        p = Point(1.0, 2.0)
        assert p.x == 1.0
        assert p.y == 2.0

    def test_distance_3_4_5(self):
        p1 = Point(0.0, 0.0)
        p2 = Point(3.0, 4.0)
        assert math.isclose(p1.distance_to(p2), 5.0)

    def test_distance_to_self_is_zero(self):
        p = Point(3.0, 7.0)
        assert p.distance_to(p) == 0.0

    def test_add_points(self):
        result = Point(1.0, 2.0) + Point(3.0, 4.0)
        assert result == Point(4.0, 6.0)


class TestStudent:
    def test_add_subject(self):
        s = Student("Eve", 10)
        s.add_subject("Math")
        assert "Math" in s.subjects

    def test_default_subjects_list_is_independent(self):
        s1 = Student("Alice", 9)
        s2 = Student("Bob", 10)
        s1.add_subject("Science")
        assert "Science" not in s2.subjects  # each instance gets its own list
