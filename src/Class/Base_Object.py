__all__ = ['Base_Object']


class Base_Object:
	def __init__(self):
		self.nb_books = None
		self.nb_lib = None
		self.nb_days = None
		self.book_scores = None
		self.libraries = []

	def next_lib(self, rest_day, rules):
		for lib in self.libraries:
			lib.calc_score(rest_day, rules)

		self.libraries = sorted(self.libraries, key=lambda tmp_lib: tmp_lib.score, reverse=True)

		best_lib = self.libraries[0]
		self.libraries.pop(0)

		return best_lib
