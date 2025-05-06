# Make index error handler with built in exceptions
Numbers = [10, 20, 30]
try:
    print(Numbers[4]) 
except IndexError:
    print("Error: Index out of range")