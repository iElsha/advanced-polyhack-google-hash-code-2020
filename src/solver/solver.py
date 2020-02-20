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

	obj, book_scores = getObject(data)

	result = get_result(obj)

	# print(f"score of {file_name}: {str(score)}")

	output(f"./out/{file_name}.{time.strftime('%H-%M-%S')}.out", data)
