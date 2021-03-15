import math
import pytest

from average_word_length import average_word_length
from check_palindrome import check_palindrome
from check_duplicates import check_duplicates
from number_of_words import number_of_words
from reverse_digits import reverse_digits
from reverse_number import reverse_number
from reverse_string import reverse_string


def test_reverse_string():
    assert reverse_string("") == ""
    assert reverse_string("t") == "t"
    assert reverse_string("to") == "ot"
    assert reverse_string("toto") == "otot"
    assert reverse_string("simplon") == "nolpmis"


def test_check_palindrome():
    assert check_palindrome('') == True
    assert check_palindrome('ete') == True
    assert check_palindrome('kayak') == True
    assert check_palindrome('aaaaaaaaaa') == True
    assert check_palindrome('aaabbbaaa') == True
    assert check_palindrome('abc') == False


def test_reverse_digits():
    assert reverse_digits(123) == 321
    assert reverse_digits(0) == 0
    assert reverse_digits(-123) == -321
    assert reverse_digits(-0) == 0
    assert reverse_digits(-100) == -1


def test_reverse_number():
    assert reverse_number(0) == 0
    assert reverse_number(123) == -123
    assert reverse_number(-1789) == 1789


def test_check_duplicates():
    assert check_duplicates([]) == []
    assert check_duplicates([1, 2, 3]) == []
    assert check_duplicates([1, 1, 2, 2, 3]) == [1, 2]
    assert check_duplicates(['a', 'a', 'b', '', 'x', 'x', '']) == ['a', '', 'x']


def test_number_of_words():
    assert number_of_words("Hello World") == 2
    assert number_of_words("Hello World !!!!") == 2
    assert number_of_words("Dude where's my car ??") == 4
    assert number_of_words("Ici, c'est Simplon !") == 3
    assert number_of_words("") == 0

def test_average_word_length():
    assert average_word_length("") == 0
    assert average_word_length("!!!!") == 0
    assert average_word_length("A") == 1
    assert average_word_length("Hello") == 5
    assert average_word_length("Hello World !!") == 5
    assert average_word_length("HelloYou") == 8
    assert math.ceil(average_word_length("Ici, c'est Simplon !")) == 5
