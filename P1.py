'''for i in range(3):
    print("Hello World")
'''
'''n = int(input("enter number:"))
if n%2 == 0:
    print("Even")
else:
    print("odd")'''
'''def count(*args):
    print(type(args))
count(1,2,3,4,5)'''
'''x = "kishore"
print(x[1:6])'''
'''while True:
    print("hi")'''
'''n= int(input("enter number:"))
x = 0
for i in range(n+1):
    x += i
print(x)'''
'''n= int(input("enter number:"))
x = 0
i = 0
while i <= n:
    x +=i
    i +=1
print(x)'''
'''nums = [35, 30, 25, 28, 20, 22, 40]
ans = []
for i in range(len(nums)):
    count = 1
    for j in range(i-1,-1,-1):
        if nums[j] >= nums[i]:
            count +=1
        else:
            break
    ans.append(count)
print(ans)'''

'''nums = [35, 30, 25, 28, 20, 22, 40]
stack = []
ans = []
for price in nums:
    count = 1
    while stack and stack[-1][0] >= price:
        p,s = stack.pop()
        count += s
    ans.append(count)    
    stack.append((price,count))
print(ans)'''

'''nums = [4, 8, 5, 2, 25]
stack = []
nse={}
ans = []
for num in nums:
    while stack and num <= stack[-1]:
        nse[stack.pop()] = num
    stack.append(num)
while stack:
    nse[stack.pop()] = -1
for num in nums:
    ans.append(nse[num]) 
print(ans)'''

'''nums = [11,7,2,15]
count= 0
maxi = nums[0]
mini = nums[0]
for i in range(len(nums)):
    if nums[i] < mini:
        mini = nums[i]
    if nums[i] > maxi:
        maxi =nums[i]
        
for num in nums:
    if mini < num < maxi:
        count +=1
    
print(count)
     '''
     
