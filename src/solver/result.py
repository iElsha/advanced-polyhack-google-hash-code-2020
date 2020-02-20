#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['get_result']

from src.readRules.RulesManager import RulesManager

rules = RulesManager()


def get_result(obj):
	libs = []
	processing = None
	for i in range(obj.nb_days):
		print("jour", i)
		if processing is not None and processing[0].nb_days < (i+1 - processing[1]):
			processing = None

		if processing is None:
			temp = obj.next_lib(obj.nb_days - i, rules)
			if temp is not None:
				processing = [temp, i, []]
				libs.append(processing)

		for lib in libs:
			print(lib[0].num, lib[0].nb_days, i, lib[1], processing)
			if lib[0].nb_days < (i+1 - lib[1] ):
				tmp = lib[0].next_books(rules)
				print(tmp)
				if tmp is not None:
					lib[2].append(tmp)
	res = [[len(libs)]]

	for lib in libs:
		lib[2] = sum(lib[2], [])
		print(lib[0].num, lib[2])

		res.append([lib[0].num, len(lib[2])])
		res.append(lib[2])
	return res
