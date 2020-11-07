
def solve(arr):

	#in satck we can pop till value of top != -1 but as we are using 2 stacks in one arr, we 
	#can't meet that condition here because if we try to do so we will end up deleting elem from 
	#stack1. What we can do here is that we can store the min top values of stacks in a top array.
	top = [4, 9]
	#top[0] -> initial value of top for stack 1
	#top[1] -> initial value of top for stack 2
	#and so on in case we need more stacks
	
	#lets pop 2 elem from stack1 and store it in temp array
	operations = ['d1', 'd1', 'd2', 'd2', ['i1', 55], ['i2', 99], 'p1', 'p2']
	temp = []

	for op in operations:
		if op[0] == 'd':
			indx = int(op[1])-1#-1 is done for converting top to 0 based index.
			x = arr.pop(top[indx])
			temp.append(x)
			#decrese all the top value by 1 for all stacks that follwos current stack 
			for i in range(indx,len(top)):
				top[i] -= 1

		elif op[0] == 'p':
			indx = int(op[1])-1
			if indx == 0:
				print(f'Number of elem in stack{indx+1} is {top[indx]+1}')
				for i in range(top[indx]+1):
					print(arr[i], end=' ')
			else:
				print(f'Number of elem in stack{indx+1} is {top[indx]-top[indx-1]}')
				for i in range(top[indx-1]+1, top[indx]+1):
					print(arr[i], end=' ')
			print()
		else:
			#as all delete operation is over we are printing its value
			indx = int(op[0][1])-1
			arr.insert(top[indx]+1, op[1])
			for i in range(indx, len(top)):
				top[i] += 1
        
        #printing deleted values in sorted order
	temp.sort()				
	print('Deleted elements are: ')
	print(*temp)
	

#creating an array
arr = [8, 5, 7, 6, 4, 12, 15, 17, 16, 14]
#calling function solve with arr as argument
solve(arr)
