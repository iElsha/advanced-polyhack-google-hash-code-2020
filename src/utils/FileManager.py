#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from random import random
from src.Class.World import World
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
	nb_books = data[0][0]
	nb_lib = data[0][1]
	nb_days = data[0][2]
	libraries = []
	score_books = data[1]

	id_lib = 0
	for i in range(2, (nb_lib * 2) + 2, 2):
		lib_nb_books = data[i][0]
		lib_nb_days = data[i][1]
		lib_nb_per_day = data[i][2]
		books = []
		for book in data[i + 1]:
			books.append((book, score_books[book]))

		num = id_lib
		lib = Library(lib_nb_books, lib_nb_days, lib_nb_per_day, books, num)
		libraries.append(lib)
		id_lib += 1

	obj = World(nb_books, nb_lib, nb_days, score_books, libraries)
	return obj


def output(path, data):
	if not os.path.exists('./out'):
		os.makedirs('./out')

	tmp = ""
	with open(path, "w+") as out:
		for row in data:
			tmp += ' '.join([str(x) for x in row]) + "\n"

		out.write(tmp[:-1])
