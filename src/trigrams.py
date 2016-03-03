# _*_ coding: utf-8 _8

import io


f = io.open('src/sherlock_small.txt', mode='r')


testbook = f.read()

wordlst = testbook.split()


def create_dict(wordlst):
	count = 0
	trigrams = {}
	for index in range(len(wordlst) - 2):
		trigrams[(wordlst[index], wordlst[index + 1])] = wordlst[index +2]
	return trigrams 
