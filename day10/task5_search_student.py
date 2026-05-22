students = [
    {"Name": "aaysha", "Marks": 85},
    {"Name": "aksha", "Marks": 92},
    {"Name": "alfiya", "Marks": 78}
]

search_name = input("Enter student name to search: ")
found = False

for student in students:
    # We use .lower() to make the search case-insensitive
    if student["Name"].lower() == search_name.lower():
        print("Student Found")
        print(f"Marks: {student['Marks']}")
        found = True
        break # Exit loop once found

if not found:
    print("Student Not Found")