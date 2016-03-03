# _*_ coding: utf-8 _8

import io


f = io.open('src/sherlock_small.txt', mode='r')
lst = []

testbook = f.read()


def test_is_open():
    if f:
        print(f)
        return f


def test_testbook():
	from src.trigrams import testbook 
	assert testbook is not None

def test_islist():
	from src.trigrams import wordlst
	assert type(lst) == list
