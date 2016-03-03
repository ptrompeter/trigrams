# _*_ coding: utf-8 _8

import io


f = io.open('src/sherlock_small.txt', mode='r')


testbook = f.read()

wordlst = testbook.split()
