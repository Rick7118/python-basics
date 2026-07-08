A = {1, 2, 3}

B = {2, 3, 4}

numbers = {1, 2, 2, 3, 4, 4, 5}
print(numbers) #only unique numbers get printed


# nums = [1, 2, 2, 3, 4, 4, 5]
# unique = set(nums)
# print(unique)                         this is how you easily remove duplicates from a list using sets

nums = [1,5,7,3,9]
lookup = set(nums)

if 7 in lookup:
    print("Found!")

    