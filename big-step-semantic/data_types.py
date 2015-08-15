# data types.

class Number(object):
	def __init__(self, value):
		# self.value should be a public member, because it's
		# gonna be used in operations like Add and Mul.
		self.value = value

	def __str__(self):
		return str(self.value)

	def __repr__(self):
		return self.__str__()

	def __bool__(self):
		return bool(self.value)

	def evaluate(self, environment):
		return self


class Boolean(object):
	def __init__(self, value):
		self.value = bool(value)

	def __str__(self):
		return str(self.value)

	def __repr__(self):
		return self.__str__()

	def evaluate(self, environment):
		return self


class Variable(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.__str__()

	def evaluate(self, environment):
		return environment[self.name]