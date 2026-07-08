items = ["Book", "Bottle", "Laptop", "Notebook"]
print(items[0])
print(items[2])

print(items[-1])

fruits = ["apple", "banana", "orange"]
fruits[1] = "mango"             #mutable
print(fruits)

# append

fruits.append("guava")
print(fruits)


a = [1, 2]
b = a.copy()  #creates a new list in memory
c = a         #does not create a new list in memory

c.append(3)   
b.append(4)

print(a)    # 1 2 3
print(b)    # 1 2 4
print(c)    # 1 2 3

#insert

numbers = [ 10, 20, 40]
numbers.insert( 2, 30)
print(numbers)

nums = [1, 2, 3, 4]
nums.insert(-2, 100)
print(nums) # 1,2,100,3,4

#remove-----> removes by value

nums_1 = [ 10, 20, 30, 40]
nums_1.remove(30)
print(nums_1)

numps = [1, 2, 3, 2, 4]
if 2 in numps:
    numps.remove(2)
print(numps)    #1,3,2,4

#pop------> removes the value by index from the list and returns it

numsy = [10, 20, 30]
x = numsy.pop()
print(x) #30
print(numsy) #10 ,20 

# you can also pop by index 
