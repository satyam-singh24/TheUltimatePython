# st = "Hey Harry you are amazing"

# f = open("myfile.txt", "a")

# f.write(st)

# f.close()


st = "Hey Harry you are amazing"

# Open file in append mode and write
with open("myfile.txt", "a") as f:
    f.write(st)  

# Read and print the contents of the file to verify
with open("myfile.txt", "r") as f:
    print(f.read())  # This will display the file content
