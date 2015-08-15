from base_operations import (
	ArithmeticBinaryOperation,
	LogicBinaryOperation,
	)

# operations.

class Add(ArithmeticBinaryOperation):
	def operate(self):
		return self.left.value+self.right.value

	def __str__(self):
		return "{} + {}".format(self.left, self.right)


class Multiply(ArithmeticBinaryOperation):
	def operate(self):
		return self.left.value*self.right.value

	def __str__(self):
		return "{} * {}".format(self.left, self.right)


class LessThan(LogicBinaryOperation):
	def operate(self):
		return self.left.value < self.right.value

	def __str__(self):
		return "{} < {}".format(self.left, self.right)