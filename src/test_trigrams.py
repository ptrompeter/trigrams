# _*_ coding: utf-8 _8

import io


f = io.open('src/sherlock_small.txt', mode='r')


testbook = f.read()


def test_is_open():
    if f:
        print(f)
        return f


def test_testbook():
    print(testbook)
    return testbook
