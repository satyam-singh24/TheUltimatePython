marks = {
    "Satyam": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Satyam"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Satyam": 99, "Renuka": 100})
# print(marks)

print(marks.get("Satyam")) 
print(marks["Satyam"]) 

print(marks.get("Satyam2")) # Prints None
print(marks["Satyam2"]) # Returns an error