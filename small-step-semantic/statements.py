

class Statement(object):
	def __str__(self):
		raise NotImplemented

	def __repr__(self):
		return self.__str__()

	def is_reducible(self):
		"""
		nearly all statements are reducible,
		except DoNothing.
		"""
		return True

	def reduce(self, environment):
		raise NotImplemented


class DoNothing(Statement):
	def __str__(self):
		return "Do Nothing."

	def is_reducible(self):
		return False


class Assign(Statement):
	def __init__(self, variable, expression):
		self.variable = variable
		self.expression = expression

	def __str__(self):
		return "{} = {}".format(self.variable, self.expression)

	def reduce(self, environment):
		"""
		The strategy used in the book cannot handle 
		expressions and statements at the same time,
		due to the different return values of statement and expression.
		So here I change the environment in place and
		only return the resulting expression,
		instead of [result, environment].
		"""
		if self.expression.is_reducible():
			expression = self.expression.reduce(environment)
			return Assign(self.variable, expression)
		else:
			environment[self.variable.name] = self.expression
			return DoNothing()


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

	def reduce(self, environment):
		if self.condition.is_reducible():
			return If(
				self.condition.reduce(environment),
				self.consequence,
				self.alternative
			)
		else:
			if self.condition.value == True:
				return self.consequence
			else:
				return self.alternative


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

	def reduce(self, environment):
		if self.first.is_reducible():
			return Sequence(
				self.first.reduce(environment),
				self.second,
				)
		else:
			return self.second


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