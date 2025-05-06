try:
    file = open("hello.txt")  # Trying to open a file that doesn't exist
    content = file.read()
    file.close()
except FileNotFoundError:
    print("Error: The file was not found!")
