import random
def Direction(arr, n):
	n = len(arr)
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

def main():
	n = int(input())	
	arr = list(map(int, input().split()))
	print(Direction(arr, n))

def inp():
	n = int(input())
	s, e = map(int, input().split())
	rand = []
	for _ in range(n):
		rand.append(random.randint(s, e))
	print(*rand)
	print(Direction(rand, n))

if __name__ == '__main__':
	inp()
