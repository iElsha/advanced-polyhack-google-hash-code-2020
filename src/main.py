#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.solver.solver import solve
from src.utils.FileManager import *
import sys

if __name__ == '__main__':
	# files = ["a_example", "b_small", "c_medium", "d_quite_big", "e_also_big"]
	files = ["a_example", "b_read_on", "c_incunabula", "d_tough_choices", "e_so_many_books", "f_libraries_of_the_world"]  # don't put the .in just the name
	# files = [ "b_read_on", "c_incunabula", "d_tough_choices", "e_so_many_books", "f_libraries_of_the_world"]  # don't put the .in just the name

	# solve("testFile") # check working dir is not src if you can run it it's good

	for file in files:
		solve(file)
	# solve("testFile")
	# solve("a_example")
	# solve("b_read_on")
	# solve("c_incunabula")
	# solve("d_tough_choices")
	# solve("e_so_many_books")
	# solve("f_libraries_of_the_world")
