sum=0
count=3
while(count<1000):
	if(count%3==0 or count%5==0):
		sum=sum+count
	count=count+1
print(sum)