for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().strip().split()))
	win, lose = 0, 0
	for elem in arr:
		if elem%5 == 0 or elem%5 == 3:
			win += 1
		elif elem > 0:
			lose += 1
	print(f'Bob wins in the game {win} times.')
	print(f'Bob loses in the game {lose} times.')
