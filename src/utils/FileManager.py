#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from random import random
from src.Class.Base_Object import Base_Object
from src.Class.Library import Library

__all__ = ['parse', 'output', 'getObject']  # Add in the list every symbols that you want to import


def parse(path):
	with open(path) as file:
		data = []
		for row in file.read().split("\n"):
			object = []
			for col in row.strip().split(" "):
				if col.isdigit():
					object.append(int(col))
				elif col.isdecimal():
					object.append(float(col))
				else:
					object.append(col)
			data.append(object)
		return data


def getObject(data):
	obj = Base_Object()
	obj.nb_books = data[0][0]
	obj.nb_lib = data[0][1]
	obj.nb_days = data[0][2]

	score_books = data[1]

	nb_lib = 0
	for i in range(2, (obj.nb_lib * 2) + 2, 2):
		lib = Library()
		lib.nb_books = data[i][0]
		lib.nb_days = data[i][1]
		lib.nb_per_day = data[i][2]
		lib.books = []
		for book in data[i + 1]:
			lib.books.append((book, score_books[book]))

		lib.num = nb_lib
		obj.libraries.append(lib)
		nb_lib += 1
	return obj


def output(path, data):
	if not os.path.exists('./out'):
		os.makedirs('./out')

	tmp = ""
	with open(path, "w+") as out:
		for row in data:
			tmp += ' '.join([str(x) for x in row]) + "\n"

		out.write(tmp)
