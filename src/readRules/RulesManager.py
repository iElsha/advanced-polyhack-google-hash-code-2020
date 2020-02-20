class RulesManager:
	"""
	Ne pas lire 2 fois le même fichier
	"""

	def __init__(self):
		self.dictAlreadyRead = {}

	def add_to_already_read(self, book_id):
		"""

		:param book: the id of the book
		:return: 0 if ok, 1 if it was already inside
		"""
		if book_id in self.dictAlreadyRead:
			return 1  # WARNING
		else:
			self.dictAlreadyRead[book_id] = True
			return 0

	def is_read(self, book_id):
		"""
		est ce que le livre a déja été lu ?
		:param book_id:
		:return: true si oui, sinon False
		"""
		return book_id in self.dictAlreadyRead
