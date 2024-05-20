# Writing to a file
with open('example.txt', 'w') as file:
    file.write('This is a test.\n')
    file.write('Writing to a file in Python.\n')

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Appending to a file
with open('example.txt', 'a') as file:
    file.write('Appending additional content.\n')

# Reading line by line
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # Remove newline character

# Reading file using a loop
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Remove newline character
