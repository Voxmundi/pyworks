import  sys

# x = [i**2 for i in range(100000000)]

y  = (i**2 for i in range(100000000))

# print(sys.getsizeof(x))
print(sys.getsizeof(y))



def zet ():
	for item in range(1000):
		yield item

z = zet()

print(z.__next__())



# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(y.__next__())

n=7
a = next(x for i,x in enumerate(y) if i==n)
print(a)


# ------------------ context Managers ------------------ 

file = open('file.txt','w')
file.write('hello world')
file.write('hello world2')
file.close()


with open('file.txt','w') as file:
	file.write('yaman')


