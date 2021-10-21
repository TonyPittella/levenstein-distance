import csv
import pytest
from edit_distance import easy_leven


def test_same_word():
    assert easy_leven("this", "this") == 0


def test_w1_shorter_than_w2():
    assert easy_leven("the", "that is correct") == 13


def test_w1_larger_than_w2():
    assert easy_leven("that is correct", "the") == 13


def test_w1_larger_than_w2_v2():
    assert easy_leven("the", "that") == 2


def test_same_length():
    assert easy_leven("this", "that") == 2


def test_examples():
    with open('data/examples.csv', newline='') as csvfile:
        examples = csv.reader(csvfile)
        for row in examples:
            assert easy_leven(row[0], row[1]) == int(row[2])


