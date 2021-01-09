def widestGap(n, start, finish):
	count = len(start)
	d = dict(zip(start, finish))
	d = sorted(d.items())
	pr = d[0][1]
	for i in range(1, count):
		v = (d[i][0]-pr-1)
		if v > ans:
			ans = v
		pr = max(pr, d[i][1])
	return ans
