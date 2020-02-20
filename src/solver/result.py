#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['get_result']

from src.utils.FileManager import *
from src.readRules.RulesManager import *


def get_result(manager, book_scores):
	compiled_lib = []
	manager.sort_lib_by_lower_acces_time()

	rules_manager = RulesManager()
	for lib in manager.libraries:
		compilation = []  # books reads
		for book in lib.books:
			if rules_manager.is_read(book) is False:
				rules_manager.add_to_already_read(book)
				compilation.append(book)
		# lib.sort_book_by_desc()  #TODO sort by score (retrieve the score)
		if(len(compilation) > 0):
			compiled_lib.append([lib.num, len(compilation)])
			compiled_lib.append(compilation)
	compiled_lib.insert(0, [len(manager.libraries)])
	return compiled_lib
