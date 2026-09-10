import pytest

from examples.data_structures.collections import word_frequency, flatten, invert_dict


class TestWordFrequency:
    def test_counts_repeated_word(self, sample_text):
        freq = word_frequency(sample_text)
        assert freq["the"] == 2     # "the" appears twice in the fixture

    def test_counts_unique_word(self, sample_text):
        freq = word_frequency(sample_text)
        assert freq["fox"] == 1

    def test_empty_string_returns_empty_dict(self):
        assert word_frequency("") == {}

    def test_case_insensitive(self):
        freq = word_frequency("Hello hello HELLO")
        assert freq["hello"] == 3

    def test_all_words_present(self, sample_text):
        freq = word_frequency(sample_text)
        for word in ["quick", "brown", "jumps", "lazy", "dog"]:
            assert word in freq


class TestFlatten:
    def test_already_flat_list(self):
        assert flatten([1, 2, 3]) == [1, 2, 3]

    def test_single_level_nesting(self):
        assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]

    def test_deeply_nested(self):
        assert flatten([[1, [2, [3]]], [4]]) == [1, 2, 3, 4]

    def test_empty_list(self):
        assert flatten([]) == []

    def test_mixed_depth(self):
        assert flatten([1, [2, 3], 4]) == [1, 2, 3, 4]

    def test_preserves_order(self):
        assert flatten([[3, 1], [4, 1], [5]]) == [3, 1, 4, 1, 5]


class TestInvertDict:
    def test_basic_inversion(self):
        assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}

    def test_empty_dict(self):
        assert invert_dict({}) == {}

    def test_string_values(self):
        assert invert_dict({"x": "alpha", "y": "beta"}) == {"alpha": "x", "beta": "y"}

    def test_double_inversion_is_identity(self):
        original = {"a": 1, "b": 2, "c": 3}
        assert invert_dict(invert_dict(original)) == original
