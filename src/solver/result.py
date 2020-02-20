#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['get_result']


def get_result(obj):
	libs = []
	processing = None
	for i in range(obj.nb_days):

		if processing is None:
			processing = [obj.next_lib(obj.nb_days - i), i, []]
			libs.append(processing)

		if processing[0].nb_days < i-processing[1] - 1:
			processing = None

		for lib in libs:
			if lib[0].nb_days < i-lib[1]:
				lib[2].append(lib[0].next_book())
	res = [[len(libs)]]
	for lib in libs:
		res.append([lib[0].num, len(lib[2])])
		res.append(lib[2])
	return res






