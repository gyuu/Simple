from data_types import (
	Number,
	Boolean,
	Variable,
	)

from operations import (
	Add,
	Multiply,
	LessThan,
	)

from statements import (
	Assign,
	If,
	Sequence,
	While,
	)

# virtual machine.

class Machine(object):
	def __init__(self, expression, environment):
		self.expression = expression
		self.environment = environment

	def step(self):
		self.expression = self.expression.reduce(self.environment)

	def run(self):
		print('begin:')
		info_str = "expression:{}, env:{}"
		while self.expression.is_reducible():
			print(
				info_str.format(self.expression, self.environment)
			)
			self.step()
		print(
			info_str.format(self.expression, self.environment)
		)
		print('over.')


def main():

	# test while, and test all the operations and statements.
	exp = While(
		LessThan(Variable('x'), Number(10)),
		Sequence(
			Assign(
				Variable('y'),
				Multiply(Variable('y'), Number(2)),
				),
			Assign(
				Variable('x'),
				Add(Variable('x'), Number(1)),
				),
			),
		)
	env = {'x':Number(7), 'y':Number(1)}
	m = Machine(exp, env)
	m.run()

# 注意给出 environment 时，内含的数据必须是 Number 类型。
# 因为 Simple 表达式返回的结果应该全都是 Simple 的数据类型。
# 而不是 python 的数据类型。
# 当我使用 environment = {'x':1, 'y':2} 时，给出的错误： 
#
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/suffocafe/lab/Simple/Simple.py", line 50, in main
#     m.run()
#   File "/home/suffocafe/lab/Simple/Simple.py", line 24, in run
#     self.environment
#   File "/home/suffocafe/lab/Simple/base_operations.py", line 27, in reduce
#     if self.left.is_reducible():
# AttributeError: 'int' object has no attribute 'is_reducible'

if __name__=='__main__':
	main()