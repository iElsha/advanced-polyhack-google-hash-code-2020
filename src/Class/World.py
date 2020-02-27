__all__ = ['World']


class World:
	def __init__(self, nb_books, nb_lib, nb_days, book_scores, libraries):
		self.nb_books = nb_books
		self.nb_lib = nb_lib
		self.nb_days = nb_days
		self.book_scores = book_scores
		self.libraries = libraries

		for lib in self.libraries:
			lib.calc_score2(nb_days)

		self.libraries = sorted(self.libraries, key=lambda tmp_lib: tmp_lib.score, reverse=True)

	def next_lib(self, rest_day, rules):
		if len(self.libraries) == 0:
			return None
		for lib in self.libraries:
			lib.calc_score(rest_day, rules)

		self.libraries = sorted(self.libraries, key=lambda tmp_lib: tmp_lib.score, reverse=True)

		best_lib = self.libraries.pop(0)

		# print("prend lib:", best_lib.num)
		return best_lib
