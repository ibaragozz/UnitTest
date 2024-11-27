import pytest

def count_vowels(s):
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for char in s if char in vowels)

# Тесты
def test_only_english_vowels():
    assert count_vowels("aeiou") == 5

def test_only_russian_vowels():
    assert count_vowels("аеёиоуыэюя") == 10

def test_no_vowels():
    assert count_vowels("bcdfg") == 0

def test_mixed_case_vowels():
    assert count_vowels("Привет Мир") == 4

def test_mixed_languages():
    assert count_vowels("Hello Мир") == 5
