# _*_ coding: utf-8 _8

import io
import random
import math
import sys

f = io.open(sys.argv[1])
long_list = f.read().split()
f.close()


def create_dict(lst):
    """Generate a trigrams dictionary for a given list."""
    tri = {}
    for i in range(len(lst) - 2):
        tri.setdefault((lst[i], lst[i + 1]), []).append(lst[i + 2])
    return tri

long_dict = create_dict(long_list)

def make_snippet(lst, dict, sniplen):
    """Return snippet based upon trigram analysis of source text given snippet length."""
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

snippet = make_snippet(long_list, long_dict, int(sys.argv[2]))


def output_file(snippet):
    """Write an imput to src/output.txt."""
    f = io.open("src/output.txt", mode='w')
    f.write(snippet)
    f.close()

if __name__ == '__main__':
    print(sys.argv)
    output_file(snippet)
