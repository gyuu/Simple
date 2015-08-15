

class Statement(object):
	def __str__(self):
		raise NotImplemented

	def __repr__(self):
		return self.__str__()

	def evaluate(self, environment):
		raise NotImplemented


class DoNothing(Statement):
	def __str__(self):
		return "Do Nothing."

	def evaluate(self, environment):
		return environment


class Assign(Statement):
	def __init__(self, variable, expression):
		self.variable = variable
		self.expression = expression

	def __str__(self):
		return "{} = {}".format(self.variable, self.expression)

	def evaluate(self, environment):
		expression = self.expression.evaluate(environment)
		environment[self.variable.name] = expression
		return environment


class If(Statement):
	"""
	`if (condition) {consequence} else {alternative}`
	condition must be a expression,
	consequence and alternative must be statements.
	"""
	def __init__(self, condition, consequence, alternative):
		self.condition = condition
		self.consequence = consequence
		self.alternative = alternative

	def __str__(self):
		return "if ({0.condition}) {{ {0.consequence} }} "\
		"else {{ {0.alternative} }}".format(self)

	def evaluate(self, environment):
		condition = self.condition.evaluate(environment)
		if condition == True:
			return self.consequence.evaluate(environment)
		else:
			return self.alternative.evaluate(environment)


class Sequence(Statement):
	"""
	combine 2 statemtns together.
	example:
	`x = 2; y = x + 1;`
	"""
	def __init__(self, first, second):
		self.first = first
		self.second = second

	def __str__(self):
		return "{0.first}; {0.second}".format(self)

	def evaluate(self, environment):
		pass


class While(Statement):
	def __init__(self, condition, consequence):
		self.condition = condition
		self.consequence = consequence

	def __str__(self):
		return "while({0}) {{ {1} }}".format(
			self.condition, self.consequence, 
			)

	def reduce(self, environment):
		"""
		span the while loop into an if statement.
		"""
		return If(
			self.condition,
			Sequence(
				self.consequence,
				While(
					self.condition,
					self.consequence,
					)
				),
			DoNothing(),
			)