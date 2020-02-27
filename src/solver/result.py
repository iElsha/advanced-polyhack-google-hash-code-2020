#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['get_result']

from src.readRules.RulesManager import RulesManager

rules = RulesManager()


def get_result(obj):
	libs = []
	processing = 0
	temp_lib = None
	# print(obj.nb_days)
	for i in range(obj.nb_days):
		# print("\njour:", i)
		if processing == 0:
			if temp_lib is not None:
				libs.append([temp_lib, []])

			temp_lib = obj.next_lib(obj.nb_days - i, rules)
			if temp_lib is not None:
				# print("prend lib", temp_lib.num)
				processing = temp_lib.nb_days

		for lib in libs:
			book = lib[0].next_books(rules)
			if book is not None:
				# print("lib", lib[0].num, "prend livre", book)
				lib[1].append(book)

		processing -= 1

	res = [
		[len(libs)]
	]

	score = 0
	for lib in libs:
		lib[1] = sum(lib[1], [])

		# print(lib[0].num, lib[2])

		res.append([lib[0].num, len(lib[1])])
		res.append(lib[1])

		for book in lib[1]:
			score += obj.book_scores[book]

	return res, score
