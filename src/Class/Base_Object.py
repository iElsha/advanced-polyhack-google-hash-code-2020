__all__ = ['Base_Object']


class Base_Object:
	def __init__(self):
		self.nb_books = None
		self.nb_lib = None
		self.nb_days = None
		self.book_scores = None
		self.libraries = []

	def sort_lib_by_lower_acces_time(self):
		self.libraries = sorted(self.libraries, key=lambda lib: lib.nb_days, reverse=False)
