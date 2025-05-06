class Person:
    def __init__(student):
        student.name = "Sukriti"
person = Person()
try:
    print(person.age)  # 'age' attribute does not exist
except AttributeError:
    print("Error: The specified attribute does not exist in the object!")
   