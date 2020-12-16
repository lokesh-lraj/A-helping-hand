n = int(input())
val = 0
if n<0:
	print('Wrong')
elif n == 0:
	print(0)
elif 1 <= n <= 199:
	val = n*2.0
elif 200 <= n <= 399:
	val = n*3.5
elif 400 <= n <= 599:
	val = n*5.8
elif n >= 600:
	val = n*7.0
if val == 2000:
	val = 21*(val/20)
print(val)