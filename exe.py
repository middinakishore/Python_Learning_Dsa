'''x= int(input())
y= int(input())
try:
    print(x/y)
except ZeroDivisionError as e :
    print(e)
except ValueError as e:
    print(e)
finally:
    print("done")'''

for i in range(5):
    if i == 4:
        break
    print(i)
else:
    print("done")


