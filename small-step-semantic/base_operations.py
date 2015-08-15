from data_types import (
	Number,
	Boolean,
	)

# abstract classes.

class BinaryOperation(object):
	"""
	Base class for binary Arithmetic and Logic operations.
	"""
	result_cls = None

	def __init__(self, left, right):
		self.left = left
		self.right = right

	def is_reducible(self):
		return True

	def operate(self):
		raise NotImplemented

	def reduce(self, environment):
		cls = self.__class__
		result_cls = cls.result_cls
		if self.left.is_reducible():
			return cls(self.left.reduce(environment), self.right)
		elif self.right.is_reducible():
			return cls(self.left, self.right.reduce(environment))
		else:
			return result_cls(self.operate())

	def __str__(self):
		raise NotImplemented

	def __repr__(self):
		return self.__str__()


class ArithmeticBinaryOperation(BinaryOperation):
	result_cls = Number


class LogicBinaryOperation(BinaryOperation):
	result_cls = Boolean