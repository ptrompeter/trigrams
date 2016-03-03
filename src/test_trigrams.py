# _*_ coding: utf-8 _8

import io

test1 = ['words', 'are', 'in', 'this', 'list']
test3 = " ".join(test1)


def test_create_dict():
    from trigrams import create_dict
    assert len(create_dict(test1)) == 3


def test_make_snippet():
    from trigrams import make_snippet
    from trigrams import create_dict
    assert type(make_snippet(test1, create_dict(test1), 1)) == str


def test_output_file():
    from trigrams import output_file
    g = io.open("src/output.txt", mode='w')
    g.write("")
    g.close()
    output_file(test3)
    fileguts = io.open("src/output.txt", mode='r').read()
    assert fileguts is not None
