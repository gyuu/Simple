

# abstract classes.

class BinaryOperation(object):
	"""
	Base class for binary Arithmetic and Logic operations.
	"""
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def __str__(self):
		raise NotImplemented

	def __repr__(self):
		return self.__str__()

	def evaluate(self, environment):
		raise NotImplemented