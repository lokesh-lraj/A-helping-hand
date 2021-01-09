def widestGap(n, start, finish):
	count = len(start)
	ans = start[0]-1
	for i in range(1, count):
		if (start[i]-finish[i-1]-1) > ans:
			ans = (start[i]-finish[i-1]-1)
	ans = max(ans, n-finish[-1]-1)
	return ans
