# _*_ coding: utf-8 _8

import io
import random
import math
import sys


def get_text(filename):
    """Open, read, and return the contents from a text file."""
    f = io.open(filename)
    long_list = f.read().split()
    f.close()
    return long_list


def create_dict(lst):
    """Generate a trigrams dictionary for a given list."""
    tri = {}
    for i in range(len(lst) - 2):
        tri.setdefault((lst[i], lst[i + 1]), []).append(lst[i + 2])
    return tri


def make_snippet(lst, dict, sniplen):
    """Return snippet based upon trigram analysis of source text."""
    rand = math.floor(((len(lst) - 2) * random.random()))
    snippet = []
    snippet.append(lst[rand])
    snippet.append(lst[rand + 1])
    while (len(snippet) < sniplen):
        k = (snippet[-2], snippet[-1])
        snippet.append(
            dict[k][math.floor(len(dict[k]) * random.random())]
        )
    snippet = " ".join(snippet)
    return snippet


def output_file(snippet):
    """Write an imput to src/output.txt."""
    f = io.open("src/output.txt", mode='w')
    f.write(snippet)
    f.close()


def main(filename, sniplen):
    """Generate a story in the src/output.txt file."""
    long_dict = create_dict(get_text(sys.argv[1]))
    textchunk = make_snippet(get_text(sys.argv[1]), long_dict, int(sys.argv[2]))
    output_file(textchunk)
    print(textchunk)
    return textchunk


if __name__ == '__main__':
    print(sys.argv)
    main(sys.argv[1], sys.argv[2])
