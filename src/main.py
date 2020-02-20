#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.solver.solver import solve
from src.utils.FileManager import *
import sys


def main(path_to_file):
	data = parse(path_to_file)

	output(path_to_file, data)


if __name__ == '__main__':
	solve("testFile")
	# solve("a_example")
	# solve("b_narrow")
	# solve("c_urgent")
	# solve("d_typical")
	# solve("e_intriguing")
	# solve("f_big")
