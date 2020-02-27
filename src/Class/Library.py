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
		i = 0
		while i < len(self.books) - 1:
			# print(i)
			if rules.is_read(self.books[i][0]):
				self.books.pop(i)
			i += 1

		cur_nb_books_max = (rest_days - self.nb_days) * self.nb_per_day
		# print(cur_nb_books_max, self.books[:cur_nb_books_max])
		tmp_books = self.books[:cur_nb_books_max]
		tmp_score = 0
		for i in tmp_books:
			tmp_score += i[1]

		self.score = tmp_score / self.nb_days

	def calc_score2(self, rest_days):
		i = 0

		cur_nb_books_max = (rest_days - self.nb_days) * self.nb_per_day
		# print(cur_nb_books_max, self.books[:cur_nb_books_max])
		tmp_books = self.books[:cur_nb_books_max]

		# print(cur_nb_books_max, self.books[:cur_nb_books_max])
		tmp_score = 0
		for i in tmp_books:
			tmp_score += i[1]

		self.score = tmp_score / self.nb_days

	def next_books(self, rules):
		# print(self.num, "books=", self.books)
		best_books = []
		i = 0
		while i < self.nb_per_day:
			if len(self.books) == 0:
				return best_books
			book = self.books.pop(0)
			if not rules.is_read(book[0]):
				best_books.append(book[0])
				rules.add_to_already_read(book[0])
				i += 1

		# self.books[0:self.nb_per_day]
			# del self.books[0:self.nb_per_day]

		# for book in best_books:
		# 	rules.add_to_already_read(book[0])

		return best_books
