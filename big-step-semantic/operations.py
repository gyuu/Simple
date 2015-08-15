from base_operations import (
	BinaryOperation,
	)

from data_types import (
	Number,
	Boolean,
	)

# operations.

class Add(BinaryOperation):
	def __str__(self):
		return "{} + {}".format(self.left, self.right)

	def evaluate(self, environment):
		return Number(
			self.left.evaluate(environment).value + \
			self.right.evaluate(environment).value
			)


class Multiply(BinaryOperation):
	def __str__(self):
		return "{} * {}".format(self.left, self.right)

	def evaluate(self, environment):
		return Number(
			self.left.evaluate(environment).value * \
			self.right.evaluate(environment).value
			)


class LessThan(BinaryOperation):
	def __str__(self):
		return "{} < {}".format(self.left, self.right)

	def evaluate(self, environment):
		return Boolean(
			self.left.evaluate(environment).value < \
			self.right.evaluate(environment).value
			)