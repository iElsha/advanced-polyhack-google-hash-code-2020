#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['get_result']


def get_result(data):
	nb_max_pizza = data[0][0]
	nb_dif_pizza_type = data[0][1]
	nb_part = 0

	type = dict()
	result = []

	nb = 0
	for i in data[1]:
		type.__setitem__(nb, i)
		nb += 1

	type = dict(sorted(type.items(), key=lambda x: x[1], reverse=True))

	for i in type.items():
		if nb_max_pizza >= i[1]:
			nb_max_pizza -= i[1]
			nb_part += i[1]
			result.append(i[0])

	output = [[nb_part], [""]]

	for i in result:
		output[1][0] += str(i) + " "

	output[1][0] = output[1][0][:-1]
	# print(output)
	print(nb_part)

	return output
