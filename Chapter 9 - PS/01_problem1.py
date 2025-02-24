# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

try:
    with open("poem.txt", "r") as f:  # Open file safely using 'with'
        content = f.read()

    if "twinkle" in content:
        print("The word 'twinkle' is present in the content.")
    else:
        print("The word 'twinkle' is not present in the content.")

except FileNotFoundError:
    print("Error: The file 'poem.txt' was not found!")
