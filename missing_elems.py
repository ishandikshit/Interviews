#--missing numbers
# a = [10, 12, 11, 15]
# low = 10
# high = 15
# b={}
# for i in range(low, high):
# 	if i in a:
# 		b[i] = a
# 	else:
# 		print i


#-- largest subarray with 0 sum
# a = [15, -2, 2, -8, 1, 7, 10, 23]
# h = {}
# sum = 0
# l = 0
# r = 0
# for i in range(0, len(a)):
# 	sum = sum+a[i]
# 	if sum in h:
# 		r = i
# 		l = h[sum]+1
# 	else:
# 		h[sum] = i
# print r-l+1


#--longest consecutive subsequence

a =[36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
h={}
for i in range(0, len(a)):
	h[a[i]] = 0

count=0
for x in range (min(a), max(a)+1):
	if x in h:
		count=count+1
		h[x]=count
	else:
		count = 0

print max(h.values())
