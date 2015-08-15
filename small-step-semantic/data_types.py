# data types.

class Number(object):
	def __init__(self, value):
		# self.value should be a public member, because it's
		# gonna be used in operations like Add and Mul.
		self.value = value

	def is_reducible(self):
		return False

	def __str__(self):
		return str(self.value)

	def __repr__(self):
		return self.__str__()

	def __bool__(self):
		return bool(self.value)


class Boolean(object):
	def __init__(self, value):
		self.value = bool(value)

	def is_reducible(self):
		return False

	def __str__(self):
		return str(self.value)

	def __repr__(self):
		return self.__str__()


class Variable(object):
	def __init__(self, name):
		self.name = name

	def is_reducible(self):
		return True

	def reduce(self, environment):
		return environment[self.name]

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.__str__()