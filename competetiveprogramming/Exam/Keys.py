def function(list1):
	list2=[]
	
	for i in range(1,len(list1)):
		list2.append(i)

	for i in range(len(list1)):
		for j in list1[i]:
			if j in list2 and j!=i:
				list2.remove(j)
	return len(list2)==0

print(function([[1], [0,2], [3]]))
print(function([[1,3], [3,0,1], [2], [0]]))
print(function([[1,2,3], [0], [0], [0]]))
print(function([[1], [0,2,4], [1,3,4], [2], [1,2]]))
print(function([[1], [2,3], [1,2], [4], [1], [5]]))
print(function([[4], [0], [1], [2], [3]]))
print(function([[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]]))
