#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.solver.solver import solve
from src.utils.FileManager import *
import sys

if __name__ == '__main__':
    # files = ["a_example", "b_small", "c_medium", "d_quite_big", "e_also_big"]
    files = ["a_", "b_", "c_", "d_", "e_", "f_"]  # don't put the .in just the name

    # solve("testFile") # check working dir is not src if you can run it it's good

	for file in files:
		solve(file)
	# solve("testFile")
	# solve("a_example")
	# solve("b_narrow")
	# solve("c_urgent")
	# solve("d_typical")
	# solve("e_intriguing")
	# solve("f_big")
