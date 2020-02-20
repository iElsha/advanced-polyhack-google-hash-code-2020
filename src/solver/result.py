#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['get_result']


def get_result(obj):
	libs = []
	for i in range(obj.nb_days):
		libs.append([obj.nextLib(), i, []])

		for lib in libs:
			if lib[0].nb_days < i-lib[1]:
				lib[2].append(lib[0].nextBook())
	res = [[len(libs)]]
	for lib in libs:
		res.append([lib[0].num, len(lib[2])])
		res.append(lib[2])
	return res






