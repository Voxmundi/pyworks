
# ----------------------Valid Sudoku----------------------

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

import collections
def valid_sudoku(board):
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    box = collections.defaultdict(set)
    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue 
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or 
                board[r][c] in box[(r//3,c//3)]):
                return False
            rows[r].add(board[r][c])
    return True

# print(valid_sudoku(board))



# ----------------------LONGEST CONSECUTIVE SEQUENCE----------------------
nums = [100,4,200,1,3,2,5]

def longest(nums):
    numset = set(nums)
    longest = 0

    for n in nums:
        if (n-1) not in numset:
            lenght = 0
            while (n+lenght) in numset:
                lenght += 1
            longest = max(lenght,longest)
    return longest



# print(longest(nums))


s = "Was it a car or a cat I saw?"
k = ''
def valid_palin(s):
    arr = [item.lower() for item in s if item.isalpha()]
    return arr == arr[::-1]
        

# print(valid_palin(s))


def val_pan(s):
    arr = [item.lower() for item in s if item.isalpha()]
    l,r = 0, len(arr)-1
    while l < r:
        if arr[l] != arr[r]:
            return False
        l,r = l+1,r-1
    return True


# ---------------------- Target Sum ----------------------
numbers = [2,7,11,15]
target = 17

def twosum (numbers, target):
    l,r = 0, len(numbers)-1

    while l < r:
        cursum = numbers[l]+numbers[r]

        if cursum > target:
            r-=1
        elif cursum < target:
            l+=1
        else:
            return [l,r]
    return[]

# print(twosum(numbers, target))



# ---------------------- 3 sum ----------------------

nums = [-1,0,1,2,-1,-4]

def tsum(nums):
    res = []
    nums.sort()

    for i,a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        

# ---------------------- Valid Paranthes ----------------------

s = "{}()[]"
def isval(s):
    stack = []
    closetoOpen = {')':'(', ']':'[','}':'{'}
    for c in s:
        if c in closetoOpen:
            if stack and stack[-1] == closetoOpen[c]:
                stack.pop()
            else:
                return False
        
        else:
            stack.append(c) 


# ---------------------- Binary search----------------------

nums = [-1,0,3,5,9,12]

def binser(nums, target):
    l,r = 0,len(nums)-1

    while l<=r:
        m = (l+r)//2
        if nums[m] > target:
            r = m-1
        elif nums[m] < target:
            l = m+1
        else: 
            return m

    return -1

# print(binser(nums,9))

import math
piles = [3,6,7,11]
h = 8 

def mineat(piles,h):
    l,r = 0, max(piles)
    res = r
    while l <= r:
        k = (l+r)//2
        hours = 0 
        for p in piles:
            hours += math.ceil(p/k)
        
        if hours <= h:
            res = min(res,k)
            r = k-1
        else:
            l = k+1
    
    return res

print(mineat(piles,h))






