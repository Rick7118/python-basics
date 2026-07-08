student = {
    "name": "Subhayu",
    "age": 22,
    "cgpa": 7.95
}

print(student["name"])


print(student.get("height"))  #returns none, use when you dont know if a key exists or not

print(student.get("cgpa", 0)) #you can return a default value if key doest exist

for key, value in student.items():
    print(key,value)


students = {
    "Subhayu": 8.2,
    "Ashmi": 9.1,
    "Rick": 7.8
}

del students["Ashmi"]
print(students)

#safer alternative

print(students.pop("Rick"))



