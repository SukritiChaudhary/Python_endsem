try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print(f"Result: {result}")
    data = {"name": "Alice", "age": 25}
    print(data["city"])  
    
    numbers = [10, 20, 30]
    print(numbers[5])  

   
    class Person:
        def __init__(self):
            self.name = "Bob"

    person = Person()
    print(person.age)  

   
    file = open("non_existent_file.txt", "r")

   
    import hello_module

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except KeyError:
    print("Error: Key not found in the dictionary.")
except IndexError:
    print("Error: List index out of range.")
except AttributeError:
    print("Error: The specified attribute does not exist.")
except FileNotFoundError:
    print("Error: The specified file was not found.")
except ModuleNotFoundError:
    print("Error: The specified module was not found.")
except ValueError:
    print("Error: Invalid input! Please enter a valid integer.")
except Exception as e:  
    print(f"Unexpected Error: {e}")