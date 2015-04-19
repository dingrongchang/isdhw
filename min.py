import time
for i in range(1,10):
	s=" "
	y=" "
	for j in range(i,10):
		s+=str.format("{0:1}*{1:1}={2:<3}",i,j,i*j)
	print(((i*7)-7)*y,s)
time.sleep(5)
