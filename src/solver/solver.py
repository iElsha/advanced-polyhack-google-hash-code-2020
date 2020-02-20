#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	Module to solve the problem of file compilation optimization problem asked for the Poly# challenge
"""
__all__ = ['solve']

from .result import *
from src.utils.FileManager import *
import time


def solve(file_name):
    """
    Resolve function
    :param file_name: the name of the file to solve
    """
    data = parse(f"./in/{file_name}.txt")

    obj = getObject(data)

    # result = get_result()

    # print(f"score of {file_name}: {str(score)}")

    output(f"./out/{file_name}.{time.strftime('%H-%M-%S')}.out", data)


def solve_erwan(obj):
    dic_library = {}
    list_lib_read = []
    dic_library_book = {}
    book_read = {}
    waiting = 0
    for i in range(0, obj.nb_days):
        for idlib in dic_library.keys():
            if dic_library[idlib] > i:
                list_lib_book = []  # getsortlivre()
                nb_read = obj.libraries[idlib].nb_per_day
                if nb_read > len(list_lib_book):
                    nb_read = len(list_lib_book)
                for k in range(0, nb_read):
                    book_read[list_lib_book[k]] = 0
                    dic_library_book[idlib].append(list_lib_book[k])

		idbestlib = 0
		effmax = 0
		# regard si peut lire new lib
		if waiting == i:
			for idlib in range(0, obj.nb_lib):
				if not idlib in dic_library:
					nb_day_to_read = i - obj.libraries[idlib].nb_days
					if nb_day_to_read > 0:
						nb_book_read = obj.libraries[idlib].nb_per_day * nb_day_to_read
						list_book = []  # getsortlivre()
						if len(list_book) < nb_book_read:
							nb_book_read = len(list_book)
						sum = 0
						for j in range(0, nb_book_read):
							sum += obj.book_scores[list_book[j]]
						eff = sum / obj.libraries[idlib].nb_per_day
						if (eff > effmax):
							effmax = eff
							idbestlib = idlib

			dic_library[idbestlib] = i + obj.libraries[idlib].nb_days
			dic_library_book[idbestlib] = []
			list_lib_read.append(idbestlib)
