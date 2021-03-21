sum=0
count=3
while(count<1000):
	if(count%3==0 or count%5==0):
		sum=sum+count
	count=count+1
print(sum)

# Better solution is SumDivisibleBy(3)+SumDivisibleBy(5)-SumDivisibleBy(15),
# where SumDivisibleBy(n) for n = 3 for example would be 3+6+9+12+......+999 = 3*(1+2+3+4+...+333) = 3*p*(p+1)/2, where p = 333 in this case. Similar for 5 and 15.
# p can be found by floor(max/n), so for 3, floor(1000/3) = 333.