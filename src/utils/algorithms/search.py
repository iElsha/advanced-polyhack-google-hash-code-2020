def linear_search(sequence, target):
	"""Pure implementation of linear search algorithm in Python
	:param sequence: some sorted collection with comparable items
	:param target: item value to search
	:return: index of found item or None if item is not found
	Examples:
	>>> linear_search([0, 5, 7, 10, 15], 0)
	# 0
	>>> linear_search([0, 5, 7, 10, 15], 15)
	# 4
	>>> linear_search([0, 5, 7, 10, 15], 5)
	# 1
	>>> linear_search([0, 5, 7, 10, 15], 6)
	"""
	for index, item in enumerate(sequence):
		if item == target:
			return index
	return None


def binary_search(a_list, item):
	"""
	DICHOTOMIC
	>>> test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
	>>> print(binary_search(test_list, 3))
	# False
	>>> print(binary_search(test_list, 13))
	True
	"""
	if len(a_list) == 0:
		return False
	midpoint = len(a_list) // 2
	if a_list[midpoint] == item:
		return True
	if item < a_list[midpoint]:
		return binary_search(a_list[:midpoint], item)
	else:
		return binary_search(a_list[midpoint + 1:], item)


def fibonacci_search(arr, val):
	"""
	>>> fibonacci_search([1,6,7,0,0,0], 6)
	# 1
	>>> fibonacci_search([1,-1, 5, 2, 9], 10)
	# -1
	>>> fibonacci_search([], 9)
	# 0
	"""
	fib_N_2 = 0
	fib_N_1 = 1
	fibNext = fib_N_1 + fib_N_2
	length = len(arr)
	if length == 0:
		return 0
	while fibNext < len(arr):
		fib_N_2 = fib_N_1
		fib_N_1 = fibNext
		fibNext = fib_N_1 + fib_N_2
	index = -1
	while fibNext > 1:
		i = min(index + fib_N_2, (length - 1))
		if arr[i] < val:
			fibNext = fib_N_1
			fib_N_1 = fib_N_2
			fib_N_2 = fibNext - fib_N_1
			index = i
		elif arr[i] > val:
			fibNext = fib_N_2
			fib_N_1 = fib_N_1 - fib_N_2
			fib_N_2 = fibNext - fib_N_1
		else:
			return i
	if (fib_N_1 and index < length - 1) and (arr[index + 1] == val):
		return index + 1
	return -1
