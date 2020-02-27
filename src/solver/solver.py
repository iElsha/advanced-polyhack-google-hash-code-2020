#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	Module to solve the problem of file compilation optimization problem asked for the Poly# challenge
"""
__all__ = ['solve']

from .result import *
from src.utils.FileManager import *
import time

from ..Class.World import World
from ..readRules.RulesManager import RulesManager


def solve(file_name, best_score):
	"""
	Resolve function
	:param best_score:
	:param file_name: the name of the file to solve
	"""
	data = parse(f"./in/{file_name}.txt")

	obj = getObject(data)
	# data = solve_erwan(obj)
	result, score = get_result(obj)

	# print(f"score of {file_name}: {str(score)}")

	print(file_name, ":", score)
	if score > best_score:
		print("NEW:", file_name)
		output(f"./out/{file_name}.{score}.out", result)

# def sort_book_by_lib(obj: Base_Object, idlib, nb_book, read: dict):
# 	list_book = []
# 	dic_book = {}
# 	nb_parcour = len(obj.libraries[idlib].books)
# 	if nb_parcour > nb_book:
# 		nb_parcour = nb_book
#
# 	for i in range(0, nb_parcour):
# 		idbestbook = -1
# 		for k in range(0, len(obj.libraries[idlib].books)):
# 			idbook = obj.libraries[idlib].books[k]
# 			print(idbook[0])
# 			if not idbook[0] in read and not idbook[0] in dic_book:
# 				if idbestbook == -1:
# 					idbestbook = idbook
# 				else:
# 					if idbook[1] > idbestbook[1]:
# 						idbestbook = idbook
# 		dic_book[idbestbook[0]] = 0
# 		list_book.append(idbestbook)
# 	return list_book


# def solve_erwan(obj: Base_Object):
# 	dic_library = {}
# 	list_lib_read = []
# 	dic_library_book = {}
# 	book_read = {}
# 	waiting = 0
# 	for i in range(0, obj.nb_days):
# 		for idlib in dic_library.keys():
# 			if dic_library[idlib] <= i:
# 				nb_read = obj.libraries[idlib].nb_per_day
# 				list_lib_book = sort_book_by_lib(obj, idlib, list_lib_book, book_read)
# 				if nb_read > len(list_lib_book):
# 					nb_read = len(list_lib_book)
# 				for k in range(0, nb_read):
# 					book_read[list_lib_book[k][0]] = True
# 					dic_library_book[idlib].append(list_lib_book[k])
#
# 		idbestlib = 0
# 		effmax = 0
# 		# regard si peut lire new lib
# 		if waiting == i:
# 			for idlib in range(0, obj.nb_lib):
# 				if not idlib in dic_library:
# 					nb_day_to_read = obj.nb_days - obj.libraries[idlib].nb_days - i
# 					if nb_day_to_read > 0:
# 						nb_book_read = obj.libraries[idlib].nb_per_day * nb_day_to_read
# 						list_book = sort_book_by_lib(obj, idlib, nb_book_read, book_read)
# 						if len(list_book) < nb_book_read:
# 							nb_book_read = len(list_book)
# 						sum = 0
# 						for j in range(0, nb_book_read):
# 							sum += list_book[j][1]
# 						eff = sum / obj.libraries[idlib].nb_per_day
# 						if eff > effmax:
# 							effmax = eff
# 							idbestlib = idlib
#
# 			dic_library[idbestlib] = i + obj.libraries[idlib].nb_days
# 			dic_library_book[idbestlib] = []
# 			waiting = i + obj.libraries[idbestlib].nb_days
# 			list_lib_read.append(idbestlib)
# 	print("test")
# 	return waiting
