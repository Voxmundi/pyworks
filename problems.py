# swap to variables

def swap():
	x = 5
	y = 10
	temp = x
	x = y
	y = temp
	print(x,y)
	x,y = y,x
	print(x,y)


#swap()

def prime_number(num):

	if num < 2:
		return False

	for i in range(2,int(num**0.5)+1):
		if num % i == 0:
			return False

	return True


# print(prime_number(12))


# ----------------------factorial-----------------------

def factorial (num):

	fact = 1

	if num < 0:
		print (f'{num} is a negative number')

	elif num == 0:
		print(f'Factorial of {num} is 1')

	else:
		for item in range(1,num+1):
			fact  = fact*item

		print(f'Factorial is {fact}')

# factorial (-4)


store ={}
def fact_dict(n):

	if n == 0:
		return 1

	if n in store:
		return store[n]

	store[n] = n*fact_dict(n-1)

	return store[n]


# print(fact_dict(6))


# ----------------------random Number-----------------------
from random import random, uniform, randint, randrange, sample

def random_number():
	# random float  0 to 1
	x = random()
	print (x)

	# random float in range
	x = uniform(1,10)
	print (x)

	x= randint(1,3)
	print (x)

	x = randrange(0,10,2)
	print (x)

	y = sample(range(10),3)
	print(y)


# random_number()



# ----------------------distubution-----------------------

def distribution(pirates,gold):
	sum_of_list = 0

	while sum_of_list != gold:
		dist_array = [randint(0,3) for pirate in range(pirates)]
		sum_of_list = sum(dist_array)

	return  dist_array





def voting(pirates,gold):

	# if 0 in distribution(pirates,gold):
	# 	print ('Fail')
	# 	return False

	# print ('OK')
	# return True

	dist = distribution(pirates,gold)
	voting_array = sum([randint(0,1) for pirate in range(pirates)])

	if voting_array == pirates/2:
		print(voting_array, 'Tied')
		return 'Tied'

	elif voting_array > pirates/2:
		print(voting_array, 'Accepted')
		print(dist)
		return dist

	else:
		print(voting_array, 'Rejected')
		return 'Rejected'




def pirate_ship(pirates,gold):

	distribution_dict = {}

	if pirates == 1:
		distribution_dict[0] = gold
		print(distribution_dict)

	else:

		voting(pirates,gold)



	

# ----------------------distubution-----------------------

def fibo(num):
	a,b = 0,1

	if num < 1:
		print (None)

	elif num == 1:
		print (a)

	elif num == 2:
		print(a)
		print(b)

	elif num > 2:
		print(a)
		print(b)

		for i  in range(num-2):
			c = a+b
			a,b = b,c
			print(c)


# fibo(10)




# ----------------------Contains Duplicate # ----------------------

def contains_duplicate(nums):
	for item in nums:
		if nums.count(item)>1:
			return True
	return False


def contains_duplicate2(nums):
	return len(set(nums)) != len(nums)


nums1 = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,3,3,4,3,2,4,2]
# print (contains_duplicate2(nums2))


# ----------------------Valid Anagram # ----------------------


s = "anagram"
t = "nagaram"

def is_anagram(t,s):
	return sorted(t) == sorted(s)


# print (is_anagram(t,s))
# print(sorted(s))







# ----------------------Valid Anagram # ----------------------
nums = [3,3,3]
target = 6


def two_sum(nums,target):
	for i in range(len(nums)):
		diff = target-nums[i]
		if diff in nums and  diff != nums[i]:
			return [i,nums.index(diff)]
	return 'No Solution'



def two_sum2(nums,target):
	dic = {}
	for i,n in enumerate(nums):
		if n in dic:
			return dic[n],i
		else:
			dic[target-n]=i
	return (False)
	

def two_sum3(nums,target):	
	num_indices = {}

	for i, num in enumerate(nums):

		dif = target - num

		if dif in num_indices:
			return [num_indices[dif], i]

		num_indices[num] = i

	return []


# print (two_sum3(nums,target))



# ----------------------Group Anagrams # ----------------------

strs = ["eat","tea","tan","ate","nat","bat"]


def group_anagrams(strs):

	dic = {}
	final_list =[]
	for item in strs:
		sorted_word = "".join(sorted(item))
		if sorted_word in dic:
			dic[sorted_word].append(item)
		else:
			dic[sorted_word] = [item]

	# for item in dic:
	# 	final_list.append(dic[item])

	# return final_list

	return list(dic.values())


# print (group_anagrams(strs))


# ----------------------K eelements  # ----------------------
nums = [1,1,1,2,2,3]
k = 2


def most_frequent(nums,key):
	arr = list(set((nums.count(item),item) for item in nums))
	arr.sort(reverse=True)
	result = [item[1] for item in arr[:key]]
	return result
	

# print (most_frequent(nums,k))


# arr  = list({2:1,3:2,4:1})
# print (arr)



# ----------------------Product of Array Except Self ----------------------

arr =  [1,2,3,4]

def product_self(arr):
	arx =[]
	for i,n in enumerate(arr):
		arr.remove(n)
		res = 1
		for k in arr:
			res*=k
		arx.append(res)
		arr.insert(i,n)
	return arx


# print(product_self(arr))



# ----------------------Binary search algorithm----------------------
"""
Binary search works by repeatedly dividing the search interval in half. 
If the value of the target is less than the value in the middle of the interval,
the search continues in the lower half, or if the value is greater, it continues in the upper half.

"""

def binary_search(A, target):
    left, right = 0, len(A) - 1

    return (left, right)

    
    # while left <= right:
    #     mid = left + (right - left) // 2
        
    #     if A[mid] == target:
    #         return mid
    #     elif A[mid] < target:
    #         left = mid + 1
    #     else:
    #         right = mid - 1
    
    # return -1

# Example usage:
A = [1, 2, 3, 4, 5,  6, 7, 8, 9,10]
target = 9
print(binary_search(A, target))  # Output: 4

target = 10
print(binary_search(A, target))  # Output: -1




def binary_s(arr,target):

	left,right = 0,len(arr)-1

	while left <= right:
		mid = left + (right-left) // 2

		if arr[mid] == target:

			return target

		elif arr [mid] < target:
			left = mid+1

		else:
			right = mid-1

	return -1







# ----------------------Valid Sudoku----------------------

board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


def valid_sudoku():

	for i in board:
		# case 1 
		for j in i:













