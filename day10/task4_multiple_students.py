students = [
    {"Name": "aaysha", "Marks": 85},
    {"Name": "aksha", "Marks": 92},
    {"Name": "shana", "Marks": 78}
]

# Loop through the list
for student in students:
    name = student["Name"]
    marks = student["Marks"]
    print(f"Student: {name}, Marks: {marks}")