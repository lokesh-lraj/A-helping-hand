def Direction(arr, n):
	
	dirc = {0:'N', 90:'E', 180:'S', 270:'W'}
	ans = 0
	for elem in arr:
		if elem>0:
			ans += 90
			ans = ans%360

		elif elem < 0:
			if ans!=0:
				ans -= 90
			else:
				ans = 270
	return dirc[ans]
