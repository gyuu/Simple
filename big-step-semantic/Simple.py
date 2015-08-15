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


def main():
	exp = Add(
		Multiply(
			Variable('x'),
			Number(3),
			),
		Add(
			Variable('y'),
			Number(4),
			),
		)
	env = {
		'x':Number(2),
		'y':Number(4),
		}
	res = exp.evaluate(env)
	print("expression:{}, environment:{}, result:{}".format(
		exp, env, res,
		)
	)


if __name__=='__main__':
	main()