#!/usr/bin/python


def check_brackets(case):
	direct = {'(', '[', '{'}git 
	reverse = {')', ']', '}'}

	brackets_d = dict()
	brackets_r = dict()

	for i in zip(direct, reverse):
		brackets_d.update(dict.fromkeys(i[0], i[1]))
		brackets_r.update(dict.fromkeys(i[1], i[0]))
	s = list()
	n = list()
	for num, i in enumerate(case, start=1):
		if i in direct.union(reverse):
			try:
				if i == brackets_d[s[-1]]:
					s.pop()
					n.pop()
				else:
					s.append(i)
					n.append(num)
			except IndexError:
				s.append(i)
				n.append(num)
			except KeyError:
				pass
	return (s, n)


print(check_brackets('([](){([])})'))
