def function(s):
	mydict={}

	for x in s:
		if x==" ":
			continue
		elif x not in mydict:
			mydict[x]=1
		else:
			mydict[x]+=1

	return mydict

s1=input().lower()
s2=input().lower()
s3=function(s1)
s4=function(s2)
if(s3==s4):
	print("true")
else:
	print("false")