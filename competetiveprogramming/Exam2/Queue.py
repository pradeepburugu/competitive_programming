def function(list1):
	for i in range(len(list1)):
		for j in range(i+1,len(list1),1):

			if(list1[i][1]<list1[j][1]):
				continue
			elif(list1[i][1]==list1[j][1]):
				if(list1[i][0]<=list1[j][0]):
					continue
				else:
					temp=list1[i]
					list1[i]=list1[j]
					list1[j]=temp
				
			else:
				temp=list1[i]
				list1[i]=list1[j]
				list1[j]=temp
	return list1



print(function([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
print(function([[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]]))
print(function([[2,4], [5,1], [3,3], [1,5], [4,2], [6,0]]))