def widestGap(n, start, finish):
	count = len(start)
	d = dict()
	for i, elem in enumerate(start):
		if elem in d:
			d[elem] = max(d[elem], finish[i])
		else:
			d[elem] = finish[i]

	d = sorted(d.items())

	pr = None
	ans = 0
	for car in d:
		if pr == None:
			pr = car[1]
		else:
			v = (car[0]-pr-1)
			if v > ans:
				ans = v
			pr = max(pr, car[1])
	return ans
