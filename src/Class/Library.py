__all__ = ['Library']


class Library:

	def __init__(self, nb_books, nb_days, nb_per_day, books, num):
		self.nb_books = nb_books
		self.nb_days = nb_days
		self.nb_per_day = nb_per_day
		self.books = books
		self.score = 0
		self.num = num
		self.sort_books()

	def sort_books(self):
		self.books = sorted(self.books, key=lambda b: b[1], reverse=True)

	def calc_score(self, rest_days, rules):
		for i in range(len(self.books) - 1):
			if rules.is_read(self.books[i][0]):
				self.books.pop(i)

		cur_nb_books_max = (rest_days - self.nb_days) * self.nb_per_day
		tmp_books = self.books[:cur_nb_books_max]
		tmp_score = 0
		for i in tmp_books:
			tmp_score += i[1]

		self.score = tmp_score

	def next_books(self, rules):
		best_books = self.books[:self.nb_per_day - 1]
		self.books = self.books[self.nb_per_day - 1:]

		for book in best_books:
			rules.add_to_already_read(book[0])

		return [i[0] for i in best_books]
