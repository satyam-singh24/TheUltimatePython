# f = open("file.txt")
# print(f.read())
# f.close()


# # The same can be written using with statement like this:
# with open("file.txt") as f:
#     print(f.read())

# # You dont have to explicitly close the file




f = open(r"E:\TheUltimatePython\Chapter 9\file.txt")
print(f.read())
f.close()

with open("file.txt", "w") as f:
    f.write("Hello, this is a test file.")

with open("file.txt", "r") as f:
    print(f.read())
