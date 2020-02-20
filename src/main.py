#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.solver.solver import solve
from src.utils.FileManager import *
import sys


def main(path_to_file):
	data = parse(path_to_file)

	output(path_to_file, data)


if __name__ == '__main__':
	solve("a_example")
	solve("b_small")
	solve("c_medium")
	solve("d_quite_big")
	solve("e_also_big")
