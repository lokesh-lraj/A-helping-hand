def widestGap(n, start, finish):
	count = len(start)
	ans = 0
	for i in range(1, count):
		if (start[i]-finish[i-1]-1) > ans:
			ans = (start[i]-finish[i-1]-1)
	return ans
