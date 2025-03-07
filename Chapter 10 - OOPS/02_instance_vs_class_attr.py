# class Employee:
#     language = "Py" # This is a class attribute
#     salary = 1200000


# satyam = Employee()
# satyam.name = "Satyam"   # This is an object attribute
# print(satyam.name, satyam.language, satyam.salary)

# singh = Employee()
# singh.name = "Singh"
# print(singh.name, singh.salary, singh.language)


# # Here name is object attribute and salary and language are 
# # class attributes as they directly belong to the class.



class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000


satyam = Employee()
satyam.language = "React"   # This is an instance attribute
print(satyam.language, satyam.salary)
